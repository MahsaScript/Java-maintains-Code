# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 03:38:06 2021

@author: 
"""
from pydriller.metrics.process.code_churn import CodeChurn
from pydriller.metrics.process.contributors_count import ContributorsCount
from pydriller.metrics.process.commits_count import CommitsCount

from pydriller import Repository

import csv

header = ['File', 'Path', 'Commit_Count', 'Code_Churn', 'Contributors']


with open('output_3.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
  
    data=[]

    for commit in Repository('https://github.com/JavaDevPractice/JavaCode').traverse_commits():
        print('Commit ID: %s' %(commit.hash))
        print('Commit Line: %s' %(commit.lines)) #total number of added + deleted lines in the commit (as shown from –shortstat).
        print('Commit File: %s' %(commit.files)) #number of files changed in the commit (as shown from –shortstat).
        print('Commit insertions: %s' %(commit.insertions)) #number of added lines in the commit (as shown from –shortstat).
        print('Commit deletions: %s' %(commit.deletions)) #number of deleted lines in the commit (as shown from –shortstat).
        
        print(commit.msg)
        print('Commit project_path: %s' %(commit.project_path ))
    
        for file in commit.modified_files:
            data.append(str(file.filename))
            print(file.filename, ' has changed')

            data.append(str(file.filename))
            data.append(str(commit.project_path))

           
            metric_CommitsCount = CommitsCount(path_to_repo='https://github.com/JavaDevPractice/JavaCode',
            from_commit=commit.hash,
            to_commit=commit.hash)

            data.append(str(metric_CommitsCount.count()))
            
 
            
            metric = ContributorsCount(path_to_repo='https://github.com/JavaDevPractice/JavaCode',from_commit=commit.hash,to_commit=commit.hash)
            count = metric.count()
            minor = metric.count_minor()
            data.append(str(count))
            data.append(str(minor))
            
            # metric_CodeChurn = CodeChurn(path_to_repo='https://github.com/JavaDevPractice/JavaCode',
            # from_commit=commit.hash,
            # to_commit=commit.hash)
            # CodeChurn = metric_CodeChurn.count()

            
            writer.writerow(data)