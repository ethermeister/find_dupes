#!/usr/bin/env python
# Author: Marcelo Ramos
# Version: 1.0
#
# Testing find duplicates based on md5 hash and file name; give user
# option on how to delete or move off dupes (newest or oldest file)

# TODO
# Compare hashes and store duplicates on a list



import os
import hashlib
import pprint # for debugging mostly

# Start walking from current directory

def get_files_list():
	dirs_and_files = dict()
	current_dir = os.getcwd()
	for root, subdirs, files in os.walk(current_dir):
		dirs_and_files[root] = files[:]
	return dirs_and_files	
		
# TODO
# Read directory from command line

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# This is where the main class will go
# Create a dictionary containing each file found with the full path info, and the respective hash

files_and_hashes = dict()
# print("The files found  are:")
for key,value in get_files_list().items():
	for item in value[:]:
		# print(item,md5(os.path.join(key,item)))
		files_and_hashes[os.path.join(key,item)] = md5(os.path.join(key,item))
# pprint.pprint(files_and_hashes)	

# Compare hashes on the dictionary, and return any entries with a duplicate

for file,hash in files_and_hashes.items():
	curr_file = file
	curr_hash = hash
	for f,h in files_and_hashes.items():
		if(curr_file == f):
			continue
		elif(curr_hash == h):
			print("Current file " + curr_file + " has a duplicate in " + f)

