import pytest
from hello import greet

def test_greeting():
    assert greet("Suzzie") == "Hello, Suzzie!"