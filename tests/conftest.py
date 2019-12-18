from pytest import fixture

from App.app import create_app

@fixture
def app():
    app = create_app()

    # some setup code

    ctx = app.app_context()
    ctx.push()
    yield app
    ctx.pop()

@fixture
def client(app):
    client = app.test_client()
    return client