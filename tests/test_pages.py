import pytest


@pytest.mark.parametrize(
    ("path", "expected_content"),
    [
        ("/", b"Campus Information Center"),
        ("/maintenance", b"Maintenance"),
        ("/imprint", b"Imprint"),
        ("/add_major", b"Add a New Major"),
        ("/add_registration", b"Add a New User Registration"),
        ("/search-building", b"<form"),
        ("/search-event", b"<form"),
        ("/search-venue", b"<form"),
        ("/new-search-building", b"<form"),
        ("/new-search-event", b"<form"),
        ("/new-search-lecture-hall", b"<form"),
    ],
)
def test_public_page_renders_without_database(client, path, expected_content):
    response = client.get(path)

    assert response.status_code == 200
    assert response.mimetype == "text/html"
    assert expected_content in response.data


def test_stylesheet_is_served(client):
    response = client.get("/static/style.css")

    assert response.status_code == 200
    assert response.mimetype == "text/css"
    assert response.data


def test_logo_is_served_as_png(client):
    response = client.get("/static/campus_logo.png")

    assert response.status_code == 200
    assert response.mimetype == "image/png"
    assert response.data.startswith(b"\x89PNG\r\n\x1a\n")


def test_unknown_route_returns_not_found(client):
    assert client.get("/does-not-exist").status_code == 404


def test_major_submission_rejects_get_requests(client):
    assert client.get("/handle_add_major").status_code == 405
