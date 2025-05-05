"""
Examples for core utilities.
"""
from pyutils.core.object_utils import get_default_if_none

# Example of get_default_if_none
print("Example of get_default_if_none:")
print(f"get_default_if_none(None, 'default') = {get_default_if_none(None, 'default')}")
print(f"get_default_if_none('value', 'default') = {get_default_if_none('value', 'default')}")
print(f"get_default_if_none(0, 42) = {get_default_if_none(0, 42)}")
