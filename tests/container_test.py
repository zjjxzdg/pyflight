# Tests the various Containers / Classes found in results.py
from pyflight.results import *


# Test the Tax Container
def test_tax():

    first_tax = Tax('9B1', 'Example Tax')
    second_tax = Tax('7B3', 'Another Example Tax')
    third_tax = first_tax

    # Test the __eq__ overload
    assert first_tax != second_tax
    assert second_tax != first_tax
    assert first_tax == third_tax
    assert third_tax == first_tax

    # Test the __len__ overload
    assert len(first_tax) == 11
    assert len(second_tax) == 19
    assert len(third_tax) == 11

    # Test the __str__ overload
    assert str(first_tax) == '9B1: Example Tax'
    assert str(second_tax) == '7B3: Another Example Tax'
    assert str(third_tax) == '9B1: Example Tax'

    # Test the as_dict method
    assert first_tax.as_dict() == {'id': '9B1', 'name': 'Example Tax'}
    assert second_tax.as_dict() == {'id': '7B3', 'name': 'Another Example Tax'}
    assert third_tax.as_dict() != {'id': '9B1', 'name': 'Example Tax'}

# Test the Airport Container
def text_airport():

    # Test the __str__ overload
    pass