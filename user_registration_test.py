"""
@Author: Girish
@Date: 2024-08-14
@Last Modified by: Girish
@Last Modified time: 2024-08-14
@Title: Check for Users First name, Lat Name, Email , Mobile Number, Password
"""

import pytest
from user_registration import validate_first_name,validate_last_name,validate_email,validate_mobile_number,validate_password


class TestNameValidation():

    def test_valid_name(self):
        
        """
        Description:s
            Checks if the name is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid name.
        """
        
        ## For valid Inputs
    def test_valid_name(self):
        """
        Function:
            Test if the first name validation function works correctly.
        Parameters:
            None
        Return:
            None
        """
        assert validate_first_name("John") is not None, "Expected 'John' to be valid"
        assert validate_first_name("Alice") is not None, "Expected 'Alice' to be valid"
        assert validate_first_name("Jo") is None, "Expected 'Jo' to be invalid due to length"
        assert validate_first_name("alice") is None, "Expected 'alice' to be invalid due to lowercase first letter"
    
    def test_valid_last_name(self):
        
        
        """
        Description:
            Checks if the name is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid name.
        """
        
        ## For valid Inputs
        assert validate_last_name("Nekar") is not None
        assert validate_last_name("Nekar") is not None
        ## For Invalid Inputs
        assert validate_last_name("nek") is None
        assert validate_last_name("Ne") is None
    
    
    def test_valid_email_name(self):
        
        
        """
        Description:
            Checks if the email is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid name.
        """
        
        ## For valid Inputs
        assert validate_email("gmnekar76@gmil.com") is not None
        assert validate_email("Google@gmil.com") is not None
       
        ## For Invalid Inputs
        assert validate_email("naveennikgmail.com") is None
        assert validate_email("namveenNaika2gmailcom") is None

    def test_valid_mobile_number(self):
        
        """
        Description:
            Checks if the mobile number is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid mobile Number.
        """
        
        ## For valid Inputs
        assert validate_mobile_number("91 8989765430") is not None
        assert validate_mobile_number("91 8989765430") is not None
        ## For Invalid Inputs
        assert validate_mobile_number("91-8989765430") is None       
        assert validate_mobile_number("89765430") is None 

    def test_valid_password(self):
        
        """
        Description:
            Checks if the password is valid according to the validation criteria.
            
        Parameters:
            self
            
        Return:
            Returns True for a valid mobile Number.
        """
        
        ## For valid Inputs
        assert validate_password("dfAds8&n9mf") is True
        assert validate_password("rkf*9jKkApj") is True
        ## For Invalid Inputs
        assert validate_password("948nkf") is False       
        assert validate_password("847sfgdfddf") is False


        
        
if __name__ == "__main__":
    pytest.main()