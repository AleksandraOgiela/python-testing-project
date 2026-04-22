import pytest
from app.validator import czy_email

@pytest.mark.parametrize("email, expected", [
    ("test@test.com", True),
    ("tetstest.com", False),
    ("test@testcom", False),
    (None, False),
    (123, False)
])
def test_email_parametrize(email, expected):
    assert czy_email(email) == expected

def  test_email_fixture(valid_email):
    assert czy_email(valid_email) == True

def test_invalid_emails(invalid_emails):
    for email in invalid_emails:
        assert czy_email(email) == False