import pytest

def functie(x):
    if x%2==0:
        return x/2
    else:
        return x

def test_functie():
    assert functie(3) == 4
