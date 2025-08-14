import pytest
from mini_apollo import ApolloClient


@pytest.fixture
def apollo_client():
    return ApolloClient(
        server_url="http://localhost:8080",
        app_id="test-app",
        secret="test-secret"
    )


@pytest.fixture
def apollo_client_no_auth():
    return ApolloClient(
        server_url="http://localhost:8080",
        app_id="test-app"
    )


@pytest.fixture
def mock_config_response():
    return {
        "appId": "test-app",
        "cluster": "default",
        "namespaceName": "application",
        "configurations": {
            "key1": "value1",
            "key2": "value2",
            "timeout": "5000"
        },
        "releaseKey": "20250101000000-test"
    }