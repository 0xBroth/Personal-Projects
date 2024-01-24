#!/usr/bin/python3
# This is a quick and dirty Web page brute forcer in python using the requests module
# By: 0xBroth - Arguably the best part of the soup!
import requests

# This function opens a specified file to use in the web dir brute force
# And create's a list out of the items in the file ---
def get_brute_list(file):
    final_list = []
    with open(file, 'r') as f:
        dir_file_read = f.read()
    clean = dir_file_read.strip().split("\n")
    for item in clean:
        final_list.append(item)
    return final_list
# This function opens a specified file to use in the web dir brute force ---

# This function sends out the get requests to the url
# And then prints a cleaned up version of the url, response code, and time it took
# To get the request back ---
def brute_force(url, directories):
    print(f"[X] Testing {url}!")
    for directory in directories:
        req = f"{url}/{directory}"
        response = requests.get(req)
        print(f"{req}:({str(response)[10:15].strip('[]')}):({response.elapsed})")
# This function sends out the get requests to the url ---


# Asks for the file to use within the web brute forcer ---
list_of_dirs = input(
    "Please input full file path if list is not in current directory:\n")
# Asks for the file to use within the web brute forcer ---

# Asks for the url to use ---
url = input("Please input a url to test:\n")
# Asks for the url to use ---

# Gets the file that contains a list of the desired directories to brute force ---
dirs = get_brute_list(list_of_dirs)
# Gets the file that contains a list of the desired directories to brute force ---

# Function that takes in the url from the user input, and the list of directories ---
brute_force(url, dirs)
# Function that takes in the url from the user input, and the list of directories ---
