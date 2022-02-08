#!/usr/bin/env python3
import pytest


@pytest.fixture()
def test_string():
    return "Мама мыла раму"


@pytest.fixture()
def test_dict():
    return {"Мама": 0, "мыла": 1, "раму": 2}


@pytest.fixture()
def test_dict_lower():
    return {"мама": 0, "мыла": 1, "раму": 2}
