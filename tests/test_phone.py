import pytest
from src.item import *
from src.phone import Phone

@pytest.fixture
def Phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_str(Phone1):
    assert str(Phone1) == "iPhone 14"


def test_repr(Phone1):
    assert repr(Phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_add(Phone1):
    with pytest.raises(ValueError):
        Phone1+10


def test_property(Phone1):
    assert Phone1.number_of_sim == 2

    with pytest.raises(ValueError):
        Phone1.number_of_sim = 0































