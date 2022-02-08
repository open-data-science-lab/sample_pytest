#!/usr/bin/env python3

from src import encoder


def test_split(test_string, test_dict):
    assert encoder.encode(test_string) == test_dict


def test_blank():
    assert encoder.encode("") == dict()


def test_stars():
    assert encoder.encode("* " * 1000) == {"*": 0}


def test_case(test_string, test_dict_lower):
    assert encoder.encode(test_string, preserve_case=False) == test_dict_lower
