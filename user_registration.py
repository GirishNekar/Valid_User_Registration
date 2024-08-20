
"""
@Author: Girish
@Date: 2024-08-20
@Last Modified by: Girish
@Last Modified time: 2024-08-20
@Title: Validate User's First Name and Lat Name
"""

import re
import mylogging as log

logger = log.logger_init('UC4')

def validate_first_name(first_name):
    
    """
    Description: 
        Checks for a valid first name.
    Parameter: 
        first_name: The first name to validate.
    Return: 
        bool: True if the first name is valid, False otherwise.
    """
    
    pattern = r'^[A-Z][A-Za-z]{2,}$'
    return re.search(pattern, first_name)

def validate_last_name(last_name):
    
    """
    Description: 
        Checks for a valid last name.
        
    Parameter: 
        last_name: The last name to validate.
    Return: 
        Object: returns Object if the last name is valid, None otherwise.
    """
    
    pattern = r'^[A-Z][A-Za-z]{2,}$'
    return re.search(pattern, last_name)

def validate_email(email):
    
    """
    Description: 
        Checks for a valid email.
        
    Parameter: 
        email: The email to validate.
    Return: 
        Object: returns Object if the email is valid, None otherwise.
    """
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$'
    return re.search(pattern, email)

def validate_mobile_number(mobile):
    
    """
    Description:
        Checks for a valid mobile number.
        
    Parameter:
        mobile : The mobile number to validate.
        
    Return:
        Object: True if the mobile number is valid, False otherwise.
    """
    
    pattern = r'^\d{2} \d{10}$'
    return re.search(pattern, mobile)


def get_input_with_validation(prompt, validation_func):
    
    """
    Description:
        Repeatedly asks the user for input, validating it with the provided function.
        
    Parameter:
        prompt : The input prompt for the user.
        validation_func : The validation function to apply to the input.
        
    Return:
        str: returns input or None if the input was not valid after 3 attempts.
    """
    
    attempts = 0
    while attempts < 3:
        
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print(f"Invalid input {attempts + 1} of 3.")
        attempts += 1

    logger.info("Your Chances of Registration are Expired.")
    return None


def main():
    
    print("---Welcome For User Registration---\n")
    
    print('Please Enter the details carefully\n')
    
    
    first_name = get_input_with_validation("Enter a valid First Name: ", validate_first_name)
    
    if not first_name :
        return
    
    last_name = get_input_with_validation("Enter a valid last Name: ", validate_last_name)
    
    if not last_name:
        return
    
    email = get_input_with_validation("Enter a valid email: ", validate_email)
    
    if not email:
        return
    
    mobile = get_input_with_validation("Enter a valid mobile number: ", validate_mobile_number)

    if  mobile:
        logger.info("Thanks For Registering")



if __name__ == "__main__":
    main()
