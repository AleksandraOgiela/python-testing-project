import pytest

@pytest.fixture
def valid_email():
    return "test@test.com"

@pytest.fixture
def invalid_emails():
    return [
        "testtest.com",
        "test@testcom",
        "",
        None,
        123
    ]

@pytest.fixture
def valid_mac():
    return "00:1A:2B:3C:4D:5E"

@pytest.fixture
def invalid_macs():
    return [
        "00:1A:2B:3C:4D",
        "00:1A:2B:3C:4D:ZZ",
        "001A:2B:3C:4D:5E",
        None,
        123
    ]