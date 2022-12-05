This is a simple password manager written in Python

Installation

1. Clone the repository
2. Install the requirements using the command 'pip install -r requirements.txt'
3. Run main.py with arguments:                                             
   -g = Generate a new password and save it in the database
   
   -r = Getting a password from the database
   
   -s = Service name that needs to be saved or retrieved
    
    Example to save a password to the password database manager:
    
    python main.py -g -s passwordforamazon
    
    Example to retrieve a password from the password database
    
    python main.py -r -s passwordforamazon

The encryption is done with private key but this application may be vulnerable to several attacks
like SQL injection as I have not done the testing for that.

It may or may not be updated in the future
