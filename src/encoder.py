#!/usr/bin/env python3

from typing import List
from collections import defaultdict

def encode(s: str, preserve_case=True) -> List:
    if not preserve_case:
        s = s.lower()
    return {x: i for i, x in enumerate({z: None for z in s.split()}.keys())}
