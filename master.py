#!/usr/bin/python3
from cryptography.fernet import Fernet
from getpass import getpass


def get_key():
    with open("/media/pranav/HDD-1/python projects/password_manager/.key1.txt", "rb") as f:
        key = f.read()

    return key


def decrypt_master():
    master_password = getpass("Enter the master password: ")
    key = get_key()

    fernet = Fernet(key)
    encMessage = "gAAAAABjkb6J8RPryf_hPuJlNyqaogUD9Zxn7P5waEjig-pFS-3DV11nwu181hi97AbU-0tZYc3b_pPp-4P8Ra5syYkEtP87_A=="

    decMessage = fernet.decrypt(encMessage).decode()

    if master_password == decMessage:
        return True
