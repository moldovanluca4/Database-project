"""Export log statistics without exposing client identities or deployment details."""

import argparse
import csv
import hashlib
import hmac
import os
from pathlib import Path
import re
import secrets
from urllib.parse import urlsplit


ACCESS_PATTERN = re.compile(
    r"(?P<client>\S+) \S+ \S+ \[(?P<time>[^]]+)\] "
    r'"\S+ (?P<route>\S+) [^"]+" \d+ \S+ "[^"]*" "(?P<browser>[^"]*)"'
)
ERROR_PATTERN = re.compile(
    r"\[(?P<time>[^]]+)\] \[[^]]+\](?: \[client (?P<client>[^]]+)\])? (?P<message>.*)"
)


def pseudonym(value, key, prefix):
    digest = hmac.new(key, value.encode("utf-8"), hashlib.sha256).hexdigest()[:24]
    return f"{prefix}-{digest}"


def client_identifier(value, key):
    if value.startswith("[") and "]" in value:
        value = value[1 : value.index("]")]
    elif value.count(":") == 1:
        value = value.split(":", 1)[0]
    return pseudonym(value, key, "client")


def browser_family(user_agent):
    for marker, name in (
        ("Edg", "Edge"),
        ("Firefox", "Firefox"),
        ("Chrome", "Chrome"),
        ("Safari", "Safari"),
    ):
        if marker.lower() in user_agent.lower():
            return name
    return "Other"


def error_category(message):
    message = message.lower()
    if "not found" in message or "does not exist" in message:
        return "Resource not found"
    if "denied" in message or "forbidden" in message:
        return "Access denied"
    return "Server event"


def export_logs(access_log, error_log, site_url, app_path, output_dir, key):
    if len(key) < 32:
        raise ValueError("The anonymization key must contain at least 32 bytes")
    if not site_url or not app_path:
        raise ValueError("Provide explicit site URL and application path filters")
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with Path(access_log).open(encoding="utf-8", errors="replace") as source:
        with (output_dir / "statistics_access.csv").open(
            "w", encoding="utf-8", newline=""
        ) as destination:
            writer = csv.writer(destination, quoting=csv.QUOTE_ALL, lineterminator="\n")
            writer.writerow(["IP Address", "Timeline", "Page Accessed", "Browser"])
            for line in source:
                if site_url not in line:
                    continue
                match = ACCESS_PATTERN.search(line)
                if match:
                    # Strip query strings before pseudonymizing the resource identifier.
                    route = urlsplit(match["route"]).path
                    writer.writerow(
                        [
                            client_identifier(match["client"], key),
                            match["time"],
                            pseudonym(route, key, "route"),
                            browser_family(match["browser"]),
                        ]
                    )

    with Path(error_log).open(encoding="utf-8", errors="replace") as source:
        with (output_dir / "statistics_error.csv").open(
            "w", encoding="utf-8", newline=""
        ) as destination:
            writer = csv.writer(destination, quoting=csv.QUOTE_ALL, lineterminator="\n")
            writer.writerow(["IP Address", "Timeline", "Error Message"])
            for line in source:
                if app_path not in line:
                    continue
                match = ERROR_PATTERN.search(line)
                if match:
                    writer.writerow(
                        [
                            client_identifier(match["client"], key)
                            if match["client"]
                            else "Unknown client",
                            match["time"],
                            error_category(match["message"]),
                        ]
                    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--access-log", type=Path, required=True)
    parser.add_argument("--error-log", type=Path, required=True)
    parser.add_argument("--site-url", required=True)
    parser.add_argument("--app-path", required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("output"))
    args = parser.parse_args()
    configured_key = os.environ.get("LOG_ANONYMIZATION_KEY")
    key = configured_key.encode("utf-8") if configured_key else secrets.token_bytes(32)
    export_logs(args.access_log, args.error_log, args.site_url, args.app_path, args.output_dir, key)


if __name__ == "__main__":
    main()
