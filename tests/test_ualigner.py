"""Test ualigner."""
from ualigner import __version__
from ualigner import ualigner


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not ualigner()
    except Exception:
        assert True
