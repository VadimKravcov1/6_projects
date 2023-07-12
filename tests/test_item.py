"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import *

@pytest.fixture
def Item5():
    return Item('stol',12.2,10)

def test_calculate_total_price(Item5):
    assert Item5.calculate_total_price() == 122.0


def test_apply_discount(Item5):
    Item5.apply_discount()
    assert Item5.price == 12.2


def test_item_initialized(Item5):
    assert Item5.name == 'stol'
    assert Item5.price == 12.2
    assert Item5.quantity == 10