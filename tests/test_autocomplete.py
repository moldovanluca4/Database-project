from unittest.mock import Mock

from mysql.connector import Error
import pytest


@pytest.mark.parametrize(
    "path",
    [
        "/api/autocomplete/personnel",
        "/api/autocomplete/search_personnel",
        "/api/autocomplete/lecture_hall",
        "/api/autocomplete/search_lecture_hall",
        "/api/autocomplete/search_event",
    ],
)
def test_autocomplete_returns_json_and_closes_resources(client, database, path):
    connection, cursor = database
    cursor.fetchall.return_value = [("First result",), ("Second result",)]

    response = client.get(path)

    assert response.status_code == 200
    assert response.mimetype == "application/json"
    assert response.get_json() == ["First result", "Second result"]
    cursor.close.assert_called_once_with()
    connection.close.assert_called_once_with()


@pytest.mark.parametrize(
    "path",
    [
        "/api/autocomplete/search_personnel",
        "/api/autocomplete/lecture_hall",
        "/api/autocomplete/search_lecture_hall",
        "/api/autocomplete/search_event",
    ],
)
def test_autocomplete_binds_search_term_as_a_parameter(client, database, path):
    _, cursor = database
    search_term = "name'); DROP TABLE users; --"

    response = client.get(path, query_string={"term": search_term})

    assert response.status_code == 200
    cursor.execute.assert_called_once()
    query, parameters = cursor.execute.call_args.args
    assert "%s" in query
    assert search_term not in query
    assert parameters == (f"%{search_term}%",)


def test_autocomplete_returns_empty_list_for_no_matches(client, database):
    response = client.get("/api/autocomplete/search_event", query_string={"term": "missing"})

    assert response.status_code == 200
    assert response.get_json() == []


@pytest.mark.parametrize("failure_point", ["connect", "execute", "fetchall"])
def test_autocomplete_handles_database_failure(
    client, app_module, database, monkeypatch, failure_point
):
    connection, cursor = database
    error = Error("Database unavailable")
    if failure_point == "connect":
        monkeypatch.setattr(app_module, "get_db_connection", Mock(side_effect=error))
    else:
        getattr(cursor, failure_point).side_effect = error

    response = client.get("/api/autocomplete/search_event")

    assert response.status_code == 200
    assert response.get_json() == []
    if failure_point == "connect":
        cursor.close.assert_not_called()
        connection.close.assert_not_called()
    else:
        cursor.close.assert_called_once_with()
        connection.close.assert_called_once_with()
