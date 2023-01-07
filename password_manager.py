#!/usr/bin/python3
import os
import sys
import pyperclip
from cryptography.fernet import Fernet
import db
import generator
import argparse
from os.path import exists
import master


def generate_key():
    key = Fernet.generate_key()
    with open("/media/pranav/HDD-1/python projects/password_manager/.key.txt", "ab") as f:
        f.write(key)


def get_key():
    with open("/media/pranav/HDD-1/python projects/password_manager/.key.txt", "rb") as f:
        key = f.read()

    return key


def encrypt(service):
    # service = input('What do you want your password for: ')
    password = generator.generate_password()
    key = get_key()

    fernet = Fernet(key)
    encMessage = fernet.encrypt(password.encode())
    save_or_not = input("Do you want to save to the database: ")
    if save_or_not == 'y':
        db.add_item(service, encMessage)
        pyperclip.copy(password)
        print('saved and copied to clipboard')


def decrypt(service):
    # service = input("Enter the service you want to be retrived: ")
    key = get_key()

    fernet = Fernet(key)
    encMessage = db.search(service)

    decMessage = fernet.decrypt(encMessage).decode()
    pyperclip.copy(decMessage)
    print("Password copied to clipboard")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-g', help='Generate a new password and save it in the database', action="store_false")
    parser.add_argument('-s', help='Service name')
    parser.add_argument('-r', help='retrieve the password from the database', action="store_false")
    args, remaining = parser.parse_known_args()

    if os.path.exists('.key.txt'):
        pass
    else:
        generate_key()

    if '-g' in sys.argv:
        if '-s' in sys.argv:
            if master.decrypt_master():
                encrypt(args.s)
            else:
                sys.exit("Wrong password!!!")
        else:
            sys.exit('Error provide the -s (service) argument ')

    elif '-r' in sys.argv:
        if '-s' in sys.argv:
            if master.decrypt_master():
                decrypt(args.s)
            else:
                sys.exit("Wrong password!!!")

        else:
            sys.exit('Error provide the -s (service) argument ')

    elif '-a' in sys.argv:
        if master.decrypt_master():
            print("\n****************************************************************************\n")
            db.retrieve_all()
            print("\n****************************************************************************\n")
        else:
            sys.exit("Wrong password!!!")
