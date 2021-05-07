#! /usr/bin/env python3

import tkinter as tk
import argparse 
from desktop_app import DesktopApp 

#To DO: Assuming the website exists put in a feature that finds the website even if the .com or .org is missing. 


# ---------------------------- ARG PARSE ------------------------------- #  
def parse_args():
    parser = argparse.ArgumentParser(description='Generate a secure password') 
    subparsers = parser.add_subparsers(help='commands', dest='command') 

    # COMMANDS
    # headless
    subparsers.add_parser('headless', help='Run without GUI') 

    return parser.parse_args(), parser

args, parser = parse_args()

if args.command == 'headless':
     print('Running headless...')
    #  parser.print_usage()
     parser.print_help()   
# ---------------------------- DESKTOP APP ------------------------------- # 
else:  
    root = tk.Tk()
    app = DesktopApp(master=root)
    app.mainloop()