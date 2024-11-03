"""Здесь надо написать тесты с использованием pytest для модуля keyboard."""
import pytest
from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def make_items():
    item1 = Keyboard("Клавиатура 1", 10000, 20)
    item2 = Keyboard("Клавиатура 2", 20000, 5)
    return item1, item2

def test_keyboard(make_items):
    kb1 = make_items[0]
    kb2 = make_items[1]
    assert isinstance(kb1, Keyboard)
    assert isinstance(kb2, Item)
    assert issubclass(Keyboard, Item)

def test_change_lang(make_items):
    kb1 = make_items[0]
    kb2 = make_items[1]
    assert kb1.language == 'EN'
    assert kb2.language == 'EN'
    kb1.change_lang()
    kb2.change_lang()
    assert kb1.language == 'RU'
    assert kb2.language == 'RU'
