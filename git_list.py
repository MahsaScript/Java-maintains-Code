# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 03:38:06 2021

@author: 
"""

from pydriller import Repository

for commit in Repository('https://github.com/JavaDevPractice/JavaCode').traverse_commits():

    print(commit.lines) #total number of added + deleted lines in the commit (as shown from –shortstat).
    print(commit.files) #number of files changed in the commit (as shown from –shortstat).
    print(commit.insertions) #number of added lines in the commit (as shown from –shortstat).
    print(commit.deletions) #number of deleted lines in the commit (as shown from –shortstat).
    # print(commit.modifications) # list of modified files in the commit (see modifications_toplevel)
    print(commit.hash)
    print(commit.msg)
    print(commit.author.name)

    for file in commit.modified_files:
        print(file.filename, ' has changed')