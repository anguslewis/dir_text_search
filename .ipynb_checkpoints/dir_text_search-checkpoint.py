import os
import re
from natsort import natsorted, ns
import pandas as pd
import sys
import argparse

# parse argument
parser = argparse.ArgumentParser()
parser.add_argument("search_term", help="term to search for in the directoriws",
                    type=str)
parser.add_argument("--no_comment", help="omit commented lines form search",
                    action="store_true")
args = parser.parse_args()

# define search term
# search is always lower case on text and argument regardless of input
search_term = args.search_term

# list of every file in directory and all sub-directoreis
root = os.getcwd()
all_files = []
for path, subdirs, files in os.walk(root):
    for name in files:
        all_files = all_files + [os.path.join(path, name)]

# program to search files line by line
def search(file_name, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line.lower():
                # If yes, then add the line number & line as a tuple in the list
                list_of_results.append((line_number, line.rstrip()))
    # Return list of tuples containing line numbers and lines where string is found
    return list_of_results

# search thorugh all files and print output
rgx_file = re.compile(r'(.*?).(do|sh|py)$')
for file in all_files:
    rgx_match = rgx_file.search(file)
    if bool(rgx_match)==True:
        if rgx_match[2] in ['do','py','sh','txt']:
            results = search(file, search_term.lower())
            print('#'*20)
            print('file   :' + file)
            if results==[]:
                print('TERM DID NOT APPEAR')
            for res in results:
                if args.no_comment:
                    py_not_com = (rgx_match[2] in ['sh','py']) and res[1].lstrip()[0]!='#'
                    do_not_com = rgx_match[2]=='do' and res[1].lstrip()[0]!='*'
                    not_py_sh_do = rgx_match[2] not in ['do','py','sh']
                    if py_not_com or do_not_com or not_py_sh_do:
                        l = len(str(res[0]))
                        print(str(res[0]) + ' '*(6-l) + ' : ' + res[1].lstrip())
                else:
                    l = len(str(res[0]))
                    print(str(res[0]) + ' '*(6-l) + ' : ' + res[1].lstrip())
            print()
        
    