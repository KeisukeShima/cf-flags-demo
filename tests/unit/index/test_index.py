import pytest
from src.index.index import Index

def test_uncovered_if():
    assert Index().uncovered_if() == False

def test_fully_covered():
    assert Index().fully_covered() == True

def test_another_tested_function():
    assert Index().another_covered_function() == True
