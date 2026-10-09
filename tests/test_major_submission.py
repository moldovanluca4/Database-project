from mysql.connector import Error
import pytest


def test_major_submission_commits_and_closes_resources(client, database):
    connection, cursor = database
    major_name = "Engineering'); DROP TABLE Majors; --"

    response = client.post("/handle_add_major", data={"major_name": major_name})

    assert response.status_code == 200
    assert b"Success! Added major:" in response.data
    cursor.execute.assert_called_once()
    query, parameters = cursor.execute.call_args.args
    assert "%s" in query
    assert major_name not in query
    assert parameters == (major_name,)
    connection.commit.assert_called_once_with()
    connection.rollback.assert_not_called()
    cursor.close.assert_called_once_with()
    connection.close.assert_called_once_with()


@pytest.mark.parametrize("failure_point", ["execute", "commit"])
def test_major_submission_rolls_back_and_closes_resources(client, database, failure_point):
    connection, cursor = database
    failing_method = cursor.execute if failure_point == "execute" else connection.commit
    failing_method.side_effect = Error("Database unavailable")

    response = client.post("/handle_add_major", data={"major_name": "Engineering"})

    assert response.status_code == 200
    assert b"An unexpected error occurred." in response.data
    assert b"Database unavailable" not in response.data
    connection.rollback.assert_called_once_with()
    if failure_point == "execute":
        connection.commit.assert_not_called()
    else:
        connection.commit.assert_called_once_with()
    cursor.close.assert_called_once_with()
    connection.close.assert_called_once_with()
