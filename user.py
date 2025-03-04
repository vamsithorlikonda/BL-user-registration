import re
import logging

#Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s : %(levelname)s : %(message)s',
    handlers = [
		logging.FileHandler('sample.log'),
		logging.StreamHandler()
	])

def validate_first_name(first_name):
    """
	Description:
		Checks whether first name is valid or not
	Parameters:
		first_name: first name to validate
	Return:
		bool: True if first name is valid, False otherwise
    """
    pattern = r'^[A-Z][a-z]{2,}(?: [A-Z][a-z]+){0,2}$'
    search = re.fullmatch(pattern,first_name)
    if search:
        logging.info(f"{first_name} is a valid first name")
        return True
    else:
        logging.warning(f"{first_name} is an invalid first name.")
        return False
    
def validate_last_name(last_name):
    """
	Description:
		Checks whether last name is valid or not
	Parameters:
		last_name: last name to validate
	Return:
		bool: True if last name is valid, False otherwise
    """
    pattern = r'^[A-Z][a-z]{2,}$'
    search = re.fullmatch(pattern,last_name)
    if search:
        logging.info(f"{last_name} is a valid last name")
        return True
    else:
        logging.warning(f"{last_name} is an invalid last name.")
        return False

def validate_email_id(email_id):
    """
	Description:
		Checks whether email id is valid or not
	Parameters:
		email_id: email id to validate
	Return:
		bool: True if email id is valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9+%_-]+(?:\.[a-zA-Z0-9+%_-]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$'
    search = re.fullmatch(pattern, email_id)
    if search:
        logging.info(f"{email_id} is valid email id")
        return True
    else:
        logging.warning(f"{email_id} is invalid email id")
        return False

def validate_mobile_number(mobile_number):
    """
	Description:
		Checks whether mobile number is valid or not
	Parameters:
		mobile_number: mobile number to validate
	Return:
		bool: True if mobile number is valid, False otherwise
    """
    pattern = r'^\+[0-9]{2,3} [0-9]{10}$'
    search = re.fullmatch(pattern, mobile_number)
    if search:
        logging.info(f"{mobile_number} is valid mobile number")
        return True
    else:
        logging.warning(f"{mobile_number} is a invalid mobile number")
        return False
    
def validate_password(pass_rule_3):
    """
	Description:
		Checks whether password is minimum of 8 characters and >= 1 [A-Z] and >= 1 [0-9], or not
	Parameters:
		pass_rule_3: password to validate
	Return:
		bool: True if password is valid, False otherwise
    """
    pattern = r'^(?=.*[A-Z])(?=.*[0-9]).{8,}$'
    search = re.fullmatch(pattern, pass_rule_3)
    if search:
        logging.info(f"{pass_rule_3} is a valid password")
        return True
    else:
        logging.warning(f"{pass_rule_3} is a invalid password")
        return False
            
def main():
    """
	Description:
		Collects user input and validates using necessary sub-functions.
	Parameters:
		None
	Return:
		None
    """
    while True:
        first = input("Enter your first name: ")
        if validate_first_name(first):
            break

    while True:
        last = input("Enter your last name: ")
        if validate_last_name(last):
            break
        
    while True:
        email_id = input("Enter your email id: ")
        if validate_email_id(email_id):
            break

    while True:
        mobile_number = input("Enter your mobile number (with country code): ")
        if validate_mobile_number(mobile_number):
            break
        
    while True:
        password_rule_3 = input("Enter your password (min 8 characters, >= 1 [A-Z] and >= 1 [0-9]): ")
        if validate_password(password_rule_3):
            print(f"{password_rule_3} is a valid password")
            break
        print("Please enter a valid password (min 8 characters, >= 1 [A-Z] and >= 1 [0-9])")

if __name__ == "__main__":
    main()          
