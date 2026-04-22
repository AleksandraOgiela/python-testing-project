import pytest
from app.validator import czy_mac

@pytest.mark.parametrize("mac, expected", [
    ("00:1A:2B:3C:4D:5E", True),
    ("00:1A:2B:3C:4D", False),
    ("00:1A:2B:3C:4D:ZZ", False),
    ("001A:2B:3C:4D:5E", False),
    (None, False)
])
def test_mac_parametrize(mac, expected):
    assert czy_mac(mac) == expected

def test_valid_mac(valid_mac):
    assert czy_mac(valid_mac) == True

def test_invalid_macs(invalid_macs):
    for mac in invalid_macs:
        assert czy_mac(mac) == False
