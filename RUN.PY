#!/usr/bin/python

'''
renames files or folders, changing all uppercase characters to lowercase.
directories will be parsed recursively.

usage: ./changecase.py file|directory
'''

import sys, os

def rename_recursive(srcpath):
    srcpath = os.path.normpath(srcpath)
    if os.path.isdir(srcpath):
        # lower the case of this directory
        newpath = name_to_lowercase(srcpath)
        # recurse to the contents
        for entry in os.listdir(newpath): #FIXME newpath
            nextpath = os.path.join(newpath, entry)
            rename_recursive(nextpath)
    elif os.path.isfile(srcpath): # base case
        name_to_lowercase(srcpath)
    else: # error
        print "bad arg: " + srcpath
        sys.exit()

def name_to_lowercase(srcpath):
    srcdir, srcname = os.path.split(srcpath)
    newname = srcname.lower()
    if newname == srcname:
        return srcpath
    newpath = os.path.join(srcdir, newname)
    print "rename " + srcpath + " to " + newpath
    os.rename(srcpath, newpath)
    return newpath

arg = sys.argv[1]
arg = os.path.expanduser(arg)
rename_recursive(arg)
