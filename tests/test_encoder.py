#!/usr/bin/env python3

from src import encoder


def test_split():
    assert encoder.encode("Мама мыла раму") == {"Мама": 0, "мыла": 1, "раму": 2}


def test_blank():
    assert encoder.encode("") == dict()


def test_stars():
    assert encoder.encode("* " * 1000) == {"*": 0}


def test_case():
    assert encoder.encode("Мама мыла раму", preserve_case=False) == {"мама": 0, "мыла": 1, "раму": 2}
