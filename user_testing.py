import pytest
# Import the functions from user.py to test them with various inputs
from user import (
    validate_first_name,
    validate_last_name,
    validate_email_id,
    validate_mobile_number,
    validate_password
)


def test_validate_first_name():
    """
	Description:
		Tests the validate_first_name function with various inputs.
	Parameters:
		None
	Return:
		None
    """
    assert validate_first_name("Pe") == False
    assert validate_first_name("percy") == False
    assert validate_first_name("PER") == False
    assert validate_first_name("P") == False
    assert validate_first_name("Percy Jackson") == True

def test_validate_last_name():
    """
	Description:
		Tests the validate_last_name function with various inputs.
	Parameters:
		None
	Return:
		None
    """
    assert validate_last_name("Gr") == False
    assert validate_last_name("Greek") == True
    assert validate_last_name("demi") == False
    assert validate_last_name("Demigod") == True

def test_validate_email_id():
    """
	Description:
		Tests the validate_email_id function with various inputs.
	Parameters:
		None
	Return:
		None
    """
    assert validate_email_id("abc.xyz@bl.co.in") == True
    assert validate_email_id("abc@bl.co") == True
    assert validate_email_id("abc@bl") == False
    assert validate_email_id("abc@.co.in") == False
    assert validate_email_id("abc@bl.c") == False

def test_validate_mobile_number():
    """
	Description:
		Tests the validate_mobile_number function with various inputs.
	Parameters:
		None
	Return:
		None
    """
    assert validate_mobile_number("+91 9876543210") == True
    assert validate_mobile_number("+1 1234567890") == False
    assert validate_mobile_number("9876543210") == False
    assert validate_mobile_number("+91987654321") == False

def test_validate_password():
    """
	Description:
		Tests the validate_password function with various inputs.
	Parameters:
		None
	Return:
		None
    """
    assert validate_password("Tyson@1234") == True
    assert validate_password("tyson1234") == False
    assert validate_password("TYSON1234") == False
    assert validate_password("Tyson1234") == False
    assert validate_password("tyc@1") == False
