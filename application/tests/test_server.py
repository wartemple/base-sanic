import pytest
from web.server import create_app

@pytest.fixture
def app():
    sanic_app = create_app()

    return sanic_app

@pytest.mark.asyncio
async def test_basic_asgi_client(app):
    request, response = await app.asgi_client.get("/api/v1/hello_world/success")

    assert request.method.lower() == "get"
    assert response.body == b'{"messages":"success"}'
    assert response.status == 200