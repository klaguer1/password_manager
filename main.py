#! /usr/bin/env python3

import tkinter as tk
import argparse 
import utils
from desktop_app import DesktopApp 

#To DO: Assuming the website exists put in a feature that finds the website even if the .com or .org is missing. 


# ---------------------------- ARG PARSE ------------------------------- #  
def parse_args():
    parser = argparse.ArgumentParser(description='Generate a secure password') 
    subparsers = parser.add_subparsers(help='commands', dest='command') 
    
    #Arguments 
    parser.add_argument("website", help="The website you are creating a password for")
    parser.add_argument("email", help="The email or username associated with the password")

    # COMMANDS
    # headless
    subparsers.add_parser('headless', help='Run without GUI') 

    return parser.parse_args(), parser

args, parser = parse_args()

if args.command == 'headless':
     print('Running headless...') 
     pwd = utils.generate_passsword(None, True) 
     """Add in code to check display whether or not password has been generated
     or if an error has been encountered from command line. Check if save completed""" 
    #  print("This is your random password {} for this website: {} and email: {}".format(pwd, args.website, args.email))
    #  parser.print_usage()
    #  parser.print_help()   
# ---------------------------- DESKTOP APP ------------------------------- # 
else:  
    root = tk.Tk()
    app = DesktopApp(master=root)
    app.mainloop()