"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import *

@pytest.fixture
def Item5():
    return Item('stol',12.2,10)

def test_testing(Item5):
    assert Item5.calculate_total_price() == 122.0