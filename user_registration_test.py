"""
@Author: Girish
@Date: 2024-08-14
@Last Modified by: Girish
@Last Modified time: 2024-08-14
@Title: Check for Users First name and last name is Valid or not
"""

import pytest
from user_registration import validate_first_name,validate_last_name

class TestNameValidation():

    def test_valid_name(self):
        
        
        """
        Description:
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
    

if __name__ == "__main__":
    pytest.main()