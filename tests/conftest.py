import pytest

from ui import ui


@pytest.fixture
def app():
    yield ui.app


@pytest.fixture
def client(app):
    return app.test_client()
