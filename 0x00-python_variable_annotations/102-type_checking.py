#!/usr/bin/env python3
"""0x00-python_variable_annotations/102-type_checking.py"""


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zooms in on an array by repeating its elements."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected the factor argument
