"""
Tests for object utility functions.
"""

from pyutils.core.object_utils import get_default_if_none


class TestGetDefaultIfNone:
    def test_none_value_returns_default(self):
        assert get_default_if_none(None, "default") == "default"

    def test_non_none_value_returns_original(self):
        assert get_default_if_none("value", "default") == "value"
        assert get_default_if_none(0, 42) == 0
        assert get_default_if_none(False, True) is False
