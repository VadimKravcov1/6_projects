from src.keyboard import Keyboard
import pytest

@pytest.fixture
def Keyboard1():
    return Keyboard("4Tech", 3500, 10)


def test_property(Keyboard1):
    assert Keyboard1.language == "EN"


def test_change_lang(Keyboard1):
    Keyboard1.change_lang()
    assert Keyboard1.language == "RU"
    Keyboard1.change_lang()
    assert Keyboard1.language == "EN"
