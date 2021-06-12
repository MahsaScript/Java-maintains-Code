# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 03:38:06 2021

@author: Mahsa
"""

from pydriller import Repository

for commit in Repository('https://github.com/JavaDevPractice/JavaCode').traverse_commits():
    print(commit.hash)
    print(commit.msg)
    print(commit.author.name)

    for file in commit.modified_files:
        print(file.filename, ' has changed')