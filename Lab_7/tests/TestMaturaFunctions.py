import pytest
from src.MaturaFunctions import matura_logarithm


test_input = [(2, -0.8613531161467861), (11, 23.244276953193612), (9, 29.012224006582876), (1.5, None), (6, None),
              (-111, None), ("Bacon Ipsum", "Error: Bacon Ipsum is not a number"), ("", "Error:  is not a number"),
              (0, None), ("15.01", "Error: 15.01 is not a number"), (True, None), (False, None),
              ([4, 12, -7], "Error: [4, 12, -7] is not a number"), ({}, "Error: {} is not a number")]


@pytest.mark.parametrize("x,expected", test_input)
def test_matura_logarithm(x, expected):
    assert matura_logarithm(x) == expected
