import os
import pytest

@pytest.fixture
def api_base_url():
    return os.getenv("INVENTREE_API_URL", "http://localhost:8000/api")

@pytest.fixture
def api_token():
    return os.getenv("INVENTREE_API_TOKEN", "")
