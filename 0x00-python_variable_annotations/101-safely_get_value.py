#!/usr/bin/env python3
"""0x00-python_variable_annotations/101-safely_get_value.py"""

from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets the value from a dictionary with a default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
