"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import *
from src.phone import Phone

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


def test_instantiate_from_csv(Item5):
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number(Item5):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5



def test_name(Item5):
    Item5.name = 'Смартфон'
    assert Item5.name == 'Смартфон'

    Item5.name = '123456789123'
    assert Item5.name == '1234567891'


def test_repr(Item5):
    assert repr(Item5) == "Item('stol', 12.2, 10)"


def test_str(Item5):
    assert str(Item5) == 'stol'


def test_add(Item5):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert Item5 + phone1 == 15
    assert phone1 + phone1 == 10


def test_item_add(Item5):
    with pytest.raises(ValueError):
        Item5+10































