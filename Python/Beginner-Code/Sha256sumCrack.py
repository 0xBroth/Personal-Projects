#!/usr/bin/python3
# By: 0xBroth - Arguably the best part of the soup!
from pwn import *
import sys

# This function is responsible for the computation of hashes and then comparing them to the user specified hash
def crack(hash, pass_file):
    attempts = 0
    with log.progress(f"Attempting to crack: {hash}!") as p:
        for password in pass_file:
                # Need to speficy the encoding because in some password files there might be certain characters that do not encode right off the bat
            password = password.encode('latin-1')
            # This needs to compare the hex representation because if using standard sha256sum() it will spit out the hex representation
            # rather than the converted hash value
            current_comparing_hash = sha256sumhex(password)
            p.status(
                f"[{attempts}] Calculating {password.decode('latin-1')} against {hash}.")
            if current_comparing_hash == hash:
                p.success(
                    f"Password hash found after {attempts} attempts! Clear Text: '{password.decode('latin-1')}' hashes to your input hash: {hash}")
                exit()
            attempts += 1
        p.failure("Password hash could not be found.")

# This function is starting to make more of an appearance in more of my programs as a quick way to clean
# files that contain a list of what I want to iterate over.
# This normally is called recursively in my open file function.
def cleanup(file):
    file = file.strip().split("\n")
    return file

# This is my standard function to open a file and clean up my list
def get_file(text_file):
    with open(text_file, 'r') as f:
        pass_file = f.read()
    return cleanup(pass_file)

# This is checking the length of arguments given by the user
# If it is not equal to three it will show the user how to use proper syntax when calling the function
if len(sys.argv) != 3:
    print("[X] Invalid format.")
    print("[~] Syntax Example: PassCrack.py <sha256sum> <path to password file>")
# This else statement actually sets the arugments to variables and calls the above functions
# Bascially this leads to most of the heavy lifting in the program
else:
    hash_to_crack = sys.argv[1]
    password_file = get_file(sys.argv[2])
    crack(hash=hash_to_crack, pass_file=password_file)
