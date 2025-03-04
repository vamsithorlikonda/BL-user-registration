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
            print(f"{first} is a valid first name")
            break
        print("Please enter  valid first name")
        
if __name__ == "__main__":
    main()  
