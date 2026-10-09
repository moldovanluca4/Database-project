import ast
from pathlib import Path
import runpy

import pytest
from mysql.connector import Error


@pytest.mark.parametrize("secret", [None, "", "too-short"])
def test_application_rejects_missing_or_short_signing_key(app_module, monkeypatch, secret):
    if secret is None:
        monkeypatch.delenv("FLASK_SECRET_KEY")
    else:
        monkeypatch.setenv("FLASK_SECRET_KEY", secret)
    with pytest.raises(RuntimeError, match="private FLASK_SECRET_KEY"):
        runpy.run_path(app_module.__file__)


def test_debug_mode_is_disabled(app_module):
    assert app_module.app.debug is False
    assert app_module.app.config["SESSION_COOKIE_HTTPONLY"] is True
    assert app_module.app.config["SESSION_COOKIE_SAMESITE"] == "Lax"


def test_database_error_does_not_reveal_private_details(client, database):
    _, cursor = database
    private_detail = "password=private-value; account=private-user; host=private-host"
    cursor.execute.side_effect = Error(private_detail)

    response = client.post("/handle_add_major", data={"major_name": "Engineering"})

    assert b"An unexpected error occurred." in response.data
    assert private_detail.encode() not in response.data
    assert b"private-value" not in response.data


def test_feedback_escapes_untrusted_success_message(app_module):
    message = '<script>alert("untrusted")</script>'
    with app_module.app.test_request_context():
        response = app_module.show_feedback(message)
    assert "<script>" not in response
    assert "&lt;script&gt;" in response


def test_unhandled_error_has_no_debug_traceback(client, app_module):
    app_module.app.config["TESTING"] = False

    @app_module.app.route("/_test_failure")
    def fail_request():
        raise RuntimeError("private-deployment-detail")

    response = client.get("/_test_failure")

    assert response.status_code == 500
    assert b"private-deployment-detail" not in response.data
    assert b"Traceback" not in response.data
    assert b"Werkzeug Debugger" not in response.data


ROOT = Path(__file__).resolve().parents[1]
FLASK_ENTRY_POINTS = [
    ROOT / "apps/campus_information_center/app_v1.py",
    ROOT / "apps/campus_information_center/app_v2.py",
    ROOT / "apps/campus_information_center/the_app_using_sqlalchemy_notforserver.py",
    ROOT / "archive/assignment-05/flask/the_app.py",
    ROOT / "archive/prototypes/public_html/new_design/the_app.py",
]


@pytest.mark.parametrize("path", FLASK_ENTRY_POINTS, ids=lambda path: str(path.relative_to(ROOT)))
def test_all_entry_points_reject_hardcoded_keys_and_debug_mode(path):
    tree = ast.parse(path.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Attribute) and target.attr == "secret_key":
                    assert not isinstance(node.value, ast.Constant), path
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if node.func.attr == "run":
                debug_arguments = [kw.value for kw in node.keywords if kw.arg == "debug"]
                assert debug_arguments
                assert all(
                    isinstance(value, ast.Constant) and value.value is False
                    for value in debug_arguments
                ), path


def test_php_database_configuration_contains_no_literal_credentials():
    source = (ROOT / "archive/assignment-05/php/db_connect.php").read_text()
    assert "getenv($name)" in source
    assert "$password =" not in source
    assert "$username =" not in source
    assert "display_errors', '0'" in source
    assert "->connect_error" not in source
