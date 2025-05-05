"""
Object utility functions for common operations on Python objects.
"""

from typing import TypeVar, Optional

T = TypeVar("T")
U = TypeVar("U")


def get_default_if_none(value: Optional[T], default: T) -> T:
    """
    Returns the default value if the given value is None.

    Args:
        value: The value to check
        default: The default value to return if value is None

    Returns:
        The original value if not None, otherwise the default value

    Examples:
        >>> get_default_if_none(None, "default")
        'default'
        >>> get_default_if_none("value", "default")
        'value'
    """
    return default if value is None else value
