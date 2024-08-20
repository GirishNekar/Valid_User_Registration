"""
@Author: Girish
@Date: 2024-08-14
@Last Modified by: Girish
@Last Modified time: 2024-08-14
@Title: Check for Users First name, Lat Name, Email , Mobile Number, Password
"""

import unittest
from user_registration import validate_first_name,validate_last_name,validate_email,validate_mobile_number,validate_password

class TestNameValidation(unittest.TestCase):

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
        self.assertTrue(validate_first_name("John"),"Should be valid")
        self.assertTrue(validate_first_name("Alice"),"Should be valid")
        ## For Invalid Inputs
        self.assertFalse(validate_first_name("Jo"), "Should be invalid due to length")        
        self.assertFalse(validate_first_name("alice"),"Should be invalid due to lowercase first letter")
    
    
    def test_valid_last_name(self):
        
        
        """
        Description:
            Checks if the name is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid lastname.
        """
        
        ## For valid Inputs
        self.assertTrue(validate_last_name("Nekar"))
        self.assertTrue(validate_last_name("Naik"))
        ## For Invalid Inputs
        self.assertFalse(validate_last_name("nek"))        
        self.assertFalse(validate_last_name("js"))
    
    
    def test_valid_email_name(self):
        
        
        """
        Description:
            Checks if the email is valid according to the validation criteria.
        Parameters:
            self
        Return:
            Returns True for a valid email.
        """
        
        ## For valid Inputs
        self.assertTrue(validate_email("gmnekar76@gmil.com"))
        self.assertTrue(validate_email("Google@gmail.co.in"))
        ## For Invalid Inputs
        self.assertFalse(validate_email("naveennikgmail.com"))        
        self.assertFalse(validate_email("namveenNaika2gmailcom"))

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
        self.assertTrue(validate_mobile_number("91 8989765430"))
        self.assertTrue(validate_mobile_number("45 8796354208"))
        ## For Invalid Inputs
        self.assertFalse(validate_mobile_number("918987654086"))        
        self.assertFalse(validate_mobile_number("909090675"))

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
        self.assertTrue(validate_password("dfAds^&nmf"))
        self.assertTrue(validate_password("rkfjKkpj"))
        ## For Invalid Inputs
        self.assertFalse(validate_password("948nkf"))        
        self.assertFalse(validate_password("847Ad"))
        
        
if __name__ == "__main__":
    unittest.main()