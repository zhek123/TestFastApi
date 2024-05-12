import asyncio
import pytest
import pytest_asyncio
from httpx import AsyncClient

from main import app
class CustomTestClient(AsyncClient):
    def delete_with_payload(self,  **kwargs):
        return self.request(method="DELETE", **kwargs)
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

@pytest_asyncio.fixture(scope="session")
async def client(event_loop):
    async with CustomTestClient(app=app, base_url="http://test") as test_client:
        yield test_client
