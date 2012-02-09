#!usr/bin/python


import sys
import os
import re


def execute(args):
    cpid = os.fork()

    if cpid == 0:
        os.execvp(args[0], args)
    else:
        os.wait()



def shell():

    if len(sys.argv) > 1: #if we have a file arg 
        source = file(sys.argv[1])  #read from the file
    else:
        source = sys.stdin  #otherwise read from stdin
    
    while True:
         print '%  ',

         command = source.readline().strip()

         #remove comments
         #split the string into an array of words
         args = re.search('^[^#]*', command).group(0).split()

         #if file is finished, or we're exiting exit
         if command == '' or (len(args) != 0 and args[0] == 'exit'): 
             sys.exit()
         
         print args

         if len(args) != 0:
             execute(args)



shell()
