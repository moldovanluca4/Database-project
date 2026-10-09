import csv

import pytest

from tools.log_analysis.analyze_logs import client_identifier, export_logs


def test_log_exports_remove_private_identifiers(tmp_path):
    access = tmp_path / "access.log"
    errors = tmp_path / "error.log"
    output = tmp_path / "output"
    site = "https://campus.example/~private_user/"
    app_path = "/srv/private_app"
    access.write_text(
        "192.0.2.10 - - [14/Oct/2025:12:00:00 +0000] "
        '"GET /~private_user/search?password=private-value HTTP/1.1" 200 12 '
        f'"{site}" "Firefox/1.0 private-browser-detail"\n'
        "192.0.2.10 - - [14/Oct/2025:12:01:00 +0000] "
        '"GET /~private_user/search HTTP/1.1" 200 12 '
        f'"{site}" "Firefox/1.0"\n'
        "192.0.2.99 - - [14/Oct/2025:12:02:00 +0000] "
        '"GET /unrelated HTTP/1.1" 200 12 "https://other.example/" "Chrome/1.0"\n'
    )
    errors.write_text(
        "[Tue Oct 14 12:00:00.000000 2025] [app:error] [client 192.0.2.10:1234] "
        f"Access denied at {app_path}; password=private-value\n"
        f"[Tue Oct 14 12:01:00.000000 2025] [app:error] Resource not found at {app_path}\n"
    )

    export_logs(access, errors, site, app_path, output, b"test-only-key-" + b"x" * 32)

    access_text = (output / "statistics_access.csv").read_text()
    error_text = (output / "statistics_error.csv").read_text()
    for private_value in (
        "192.0.2.10",
        "private_user",
        "private-value",
        "private-browser-detail",
        app_path,
        site,
    ):
        assert private_value not in access_text + error_text
    access_rows = list(csv.DictReader(access_text.splitlines()))
    error_rows = list(csv.DictReader(error_text.splitlines()))
    assert len(access_rows) == 2
    assert len(error_rows) == 2
    assert access_rows[0]["IP Address"] == access_rows[1]["IP Address"]
    assert access_rows[0]["Page Accessed"] == access_rows[1]["Page Accessed"]
    assert access_rows[0]["IP Address"] == error_rows[0]["IP Address"]
    assert access_rows[0]["Browser"] == "Firefox"
    assert error_rows[0]["Error Message"] == "Access denied"
    assert error_rows[1]["Error Message"] == "Resource not found"


def test_client_pseudonyms_depend_on_private_key():
    first = client_identifier("192.0.2.10", b"a" * 32)
    second = client_identifier("192.0.2.10", b"b" * 32)
    assert first != second


def test_export_rejects_short_anonymization_key(tmp_path):
    with pytest.raises(ValueError, match="at least 32 bytes"):
        export_logs(tmp_path / "access", tmp_path / "errors", "site", "app", tmp_path, b"short")
