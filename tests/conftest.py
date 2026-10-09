import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from unittest.mock import Mock

import mysql.connector
import pytest


@pytest.fixture
def app_module(monkeypatch):
    monkeypatch.setenv("FLASK_SECRET_KEY", "test-only-secret-" + "x" * 32)
    config = ModuleType("config")
    config.DB_HOST = "127.0.0.1"
    config.DB_USER = "test_user"
    config.DB_PASS = "test_password"
    config.DB_NAME = "test_database"
    monkeypatch.setitem(sys.modules, "config", config)

    def prevent_database_connection(*args, **kwargs):
        pytest.fail("Tests must mock database access instead of opening a real connection")

    monkeypatch.setattr(mysql.connector, "connect", prevent_database_connection)

    path = Path(__file__).resolve().parents[1] / "apps/campus_information_center/app_v2.py"
    module_name = "_campus_test_app"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load the application from {path}")
    module = importlib.util.module_from_spec(spec)
    monkeypatch.setitem(sys.modules, module_name, module)
    spec.loader.exec_module(module)
    module.app.config.update(TESTING=True, SECRET_KEY="test-only-secret")
    return module


@pytest.fixture
def client(app_module):
    with app_module.app.test_client() as test_client:
        yield test_client


@pytest.fixture
def database(app_module, monkeypatch):
    connection = Mock(name="database_connection")
    cursor = Mock(name="database_cursor")
    connection.cursor.return_value = cursor
    cursor.fetchall.return_value = []
    monkeypatch.setattr(app_module, "get_db_connection", Mock(return_value=connection))
    return connection, cursor
