import contextlib

import pytest


@pytest.mark.django_db
def test_health_check(client):
    """Ensures /live endpoint returns HTTP 200."""
    response = client.get("/live")

    assert response.status_code == 200


@pytest.mark.django_db
def test_health_check_db_up(client):
    """Ensures db status is ``up``."""
    response = client.get("/live")
    assert response.status_code == 200
    assert response.json()["db"] == "up"


@pytest.mark.django_db
def test_health_check_db_down(client, monkeypatch):
    """Ensures db status is ``down`` when unable to connect to db."""
    from django.db import connection

    @contextlib.contextmanager
    def mock_cursor():
        yield None

    monkeypatch.setattr(connection, "cursor", mock_cursor)
    response = client.get("/live")
    assert response.status_code == 500
    assert response.json()["db"] == "down"
