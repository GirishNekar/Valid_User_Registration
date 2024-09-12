"""
@Author: Girish
@Date: 2024-08-14
@Last Modified by: Girish
@Last Modified time: 2024-08-14
@Title: Check for Users First name, Lat Name, Email , Mobile Number, Password
"""

import pytest
from user_registration import validate_first_name, validate_last_name, validate_email, validate_mobile_number, validate_password

class TestNameValidation():
    def test_valid_name(self):
        """
        Description:
            Checks if the first name is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid first name.
        """
        ## For valid Inputs
        assert validate_first_name("John") is not None, "Expected 'John' to be valid"
        assert validate_first_name("Alice") is not None, "Expected 'Alice' to be valid"
        
        ## For Invalid Inputs
        assert validate_first_name("Jo") is None, "Expected 'Jo' to be invalid due to length"
        assert validate_first_name("alice") is None, "Expected 'alice' to be invalid due to lowercase first letter"
    
    def test_valid_last_name(self):
        """
        Description:
            Checks if the last name is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid last name.
        """
        ## For valid Inputs
        assert validate_last_name("Nekar") is not None, "Expected 'Nekar' to be valid"
        assert validate_last_name("Naik") is not None, "Expected 'Naik' to be valid"
        
        ## For Invalid Inputs
        assert validate_last_name("nek") is None, "Expected 'nek' to be invalid due to lowercase"
        assert validate_last_name("js") is None, "Expected 'js' to be invalid due to length"

    def test_valid_email(self):
        """
        Description:
            Checks if the email is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid email.
        """
        ## For valid Inputs
        assert validate_email('abc-100@yahoo.com') is not None, "Expected 'abc-100@yahoo.com' to be valid"
        assert validate_email('abc.100@yahoo.com') is not None, "Expected 'abc.100@yahoo.com' to be valid"
        assert validate_email('abc111@abc.com') is not None, "Expected 'abc111@abc.com' to be valid"
        assert validate_email('abc-100@abc.net') is not None, "Expected 'abc-100@abc.net' to be valid"
        assert validate_email('abc.100@abc.com.au') is not None, "Expected 'abc.100@abc.com.au' to be valid"
        assert validate_email('abc@1.com') is not None, "Expected 'abc@1.com' to be valid"
        assert validate_email('abc@gmail.com.com') is not None, "Expected 'abc@gmail.com.com' to be valid"
        assert validate_email('abc+100@gmail.com') is not None, "Expected 'abc+100@gmail.com' to be valid"

        ## For Invalid Inputs
        assert validate_email('abc') is None, "Expected 'abc' to be invalid"
        assert validate_email('abc@.com.my') is None, "Expected 'abc@.com.my' to be invalid"
        assert validate_email('abc123@gmail.a') is None, "Expected 'abc123@gmail.a' to be invalid"
        assert validate_email('abc123@.com') is None, "Expected 'abc123@.com' to be invalid"
        assert validate_email('abc123@.com.com') is None, "Expected 'abc123@.com.com' to be invalid"
        assert validate_email('abc()*@gmail.com') is None, "Expected 'abc()*@gmail.com' to be invalid"
        assert validate_email('.abc@abc.com') is None, "Expected '.abc@abc.com' to be invalid"
        assert validate_email('abc@%*.com') is None, "Expected 'abc@%*.com' to be invalid"
        assert validate_email('abc..2002@gmail.com') is None, "Expected 'abc..2002@gmail.com' to be invalid"
        assert validate_email('abc@abc@gmail.com') is None, "Expected 'abc@abc@gmail.com' to be invalid"
        assert validate_email('abc@gmail.com.1a') is None, "Expected 'abc@gmail.com.1a' to be invalid"
        assert validate_email('abc@gmail.com.aa.au') is None, "Expected 'abc@gmail.com.aa.au' to be invalid"

    def test_valid_mobile_number(self):
        """
        Description:
            Checks if the mobile number is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid mobile number.
        """
        ## For valid Inputs
        assert validate_mobile_number("91 8989765430") is not None, "Expected '91 8989765430' to be valid"
        assert validate_mobile_number("45 8796354208") is not None, "Expected '45 8796354208' to be valid"
        
        ## For Invalid Inputs
        assert validate_mobile_number("918987654086") is None, "Expected '918987654086' to be invalid"
        assert validate_mobile_number("909090675") is None, "Expected '909090675' to be invalid"

    def test_valid_password(self):
        """
        Description:
            Checks if the password is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid password.
        """
        ## For valid Inputs
        assert validate_password("dfAds8&n9mf") is True, "Expected 'dfAds8&n9mf' to be valid"
        assert validate_password("rkf*9jKkApj") is True, "Expected 'rkf*9jKkApj' to be valid"
        
        ## For Invalid Inputs
        assert validate_password("948nkAf") is False, "Expected '948nkAf' to be invalid"
        assert validate_password("847s(fgdfddf") is False, "Expected '847s(fgdfddf' to be invalid"

if __name__ == "__main__":
    pytest.main()
