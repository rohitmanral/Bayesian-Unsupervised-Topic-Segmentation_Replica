# -*- coding: utf-8 -*-
"""Task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i37Hyk0KcxXTLAgRCppQ7wBb9SWMkzED

#<strong><center>Bayesian-Unsupervised-Topic-Segmentation</center></strong>

## Import necessary libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""# **Web scraping from two websites**"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

website_1 = BeautifulSoup(urlopen("http://www2.nau.edu/lrm22/lessons/human_senses/human_senses.html"), 'lxml')

website_2 = BeautifulSoup(urlopen("http://www2.nau.edu/lrm22/lessons/nuts_and_bolts/nuts_and_bolts.html"), 'lxml')

"""# XXXXXXXXXXXXXXXXXXXX

# **Writing the webscraped text files in two text files i.e. `in_1.txt` & `in_2.txt`**

# **`in_1.txt`**
"""

website_1.title.decompose()

to_remove = website_1.find_all("b") 
for element in to_remove:
    element.extract()

to_remove = website_1.find_all("h1") 
for element in to_remove:
    element.extract()


to_remove = website_1.find_all("em") 
for element in to_remove:
    element.extract()

to_remove = website_1.find_all("a") 
for element in to_remove:
    element.extract()

text_1 = website_1.text

print(text_1)

text_1 = text_1.replace(",","").replace(":","").replace('"','').replace(";","")
import re

text_1=re.sub('\d. ', '', text_1)
text_1=re.sub('[A-Z]. ', '', text_1)
text_1=re.sub('([0-9]*[.])?[0-9]+', '', text_1)
text_1=text_1.replace(".", "\n")
text_1=text_1.replace("ii", "").replace("iii", "")
text_1=re.sub('\\n+\s+\\n+', '\n', text_1)
text_1=re.sub('i\n', '\n', text_1)
text_1=text_1.replace(" () and  ()","")
text_1=re.sub('\\n+\s+\\n+', '\n', text_1)
text_1 = text_1.replace("\n\n ","\n").replace("\n\n","\n")

print(text_1)

"""# **Creating a .txt file**"""

f= open("input_1.txt","w+") #open the file for writing
f.write(text_1) #writing the file

f=open("input_1.txt", "r") #Opening the file back to read the contents
print(f.read()) #reading & printing the contents of file
f.close() #finally closing the file

"""# **Counting number of lines in a .txt file**"""

# Opening a file 
file = open("input_1.txt","r") 
Counter = 0
  
# Reading from file 
Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1
          
print("There is {} lines in this file.".format(Counter))

"""# **Dividing the file into 4 segments, means `number of segments` will be 4.**"""

files=[]

lines_per_file = int(Counter/3.0)  # Lines on each small file
lines = []  # Stores lines not yet written on a small file
lines_counter = 0  # Same as len(lines)
created_files = 0  # Counting how many small files have been created

with open('input_1.txt') as big_file:
    for line in big_file:  # Go throught the whole big file
        lines.append(line)
        lines_counter += 1
        if lines_counter == lines_per_file:
            idx = lines_per_file * (created_files + 1)
            with open('small_file_%s.txt' % idx, 'w') as small_file:
                # Write all lines on small file
                small_file.write('\n'.join(lines))
                files.append('small_file_%s.txt' % idx,)
            lines = []  # Reset variables
            lines_counter = 0
            created_files += 1  # One more small file has been created
    # After for-loop has finished
    if lines_counter:  # There are still some lines not written on a file?
        idx = lines_per_file * (created_files + 1)
        with open('small_file_%s.txt' % idx, 'w') as small_file:
            # Write them on a last small file
            small_file.write('n'.join(lines))
            files.append('small_file_%s.txt' % idx,)
        created_files += 1

print ('%s small files (%s lines in each) are created.' % (created_files,
                                                             lines_per_file))
print(files)

def add_dashes(file_name):
  with open(file_name, 'r+') as file: 
    originalContent = file.read() 
    file.seek(0, 0)              # Move the cursor to top line 
    file.write("==========")             # Add a new blank line 
    file.write(originalContent) 

for i in files:
  add_dashes(i)

with open('input_1.txt', 'w') as outfile:
  for fname in files:
    with open(fname) as infile:
      for line in infile:
        outfile.write(line)

with open('input_1.txt', 'r') as f:
  contents = f.read()

with open('input_1.txt', 'w') as f:
  f.write(contents.replace("==========", "==========\n"))

with open('input_1.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('input_1.txt', 'w') as fout:
    fout.writelines(data[3:])

with open("input_1.txt", "a") as a_file:
  a_file.write("==========")

with open('input_1.txt') as f: 
	updatedfile="=========="+'\n'+f.read() 
with open('input_1.txt','w') as f: 
	f.write(updatedfile)

with open('input_1.txt', 'r') as fin:
  print(fin.read())
fin.close()

"""# XXXXXXXXXXXXXXXXXXXX

# **`in_2.txt`**
"""

website_2.title.decompose()

to_remove = website_2.find_all("b") 
for element in to_remove:
    element.extract()

to_remove = website_2.find_all("h1") 
for element in to_remove:
    element.extract()


to_remove = website_2.find_all("em") 
for element in to_remove:
    element.extract()

to_remove = website_2.find_all("a") 
for element in to_remove:
    element.extract()

text_2 = website_2.text

print(text_2)

text_2 = text_2.replace(",","").replace(":","").replace('"','').replace(";","").replace(")","").replace("(","")
import re

text_2=re.sub('\d', '', text_2)
text_2 = text_2.replace(".","")
text_2 = text_2.replace("-","").replace("!","")
text_2 = text_2.replace("a ","").replace("b ","")

text_2=re.sub('\s+\\n', '\n', text_2)

print(text_2)

"""# **Creating a .txt file**"""

f= open("input_2.txt","w+") #open the file for writing
f.write(text_2) #writing the file

f=open("input_2.txt", "r") #Opening the file back to read the contents
print(f.read()) #reading & printing the contents of file
f.close() #finally closing the file

"""# **Counting number of lines in a .txt file**"""

# Opening a file 
file = open("input_2.txt","r") 
Counter = 0
  
# Reading from file 
Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1
          
print("There is {} lines in this file.".format(Counter))

"""# **Dividing the file into 4 segments, means `number of segments` will be 4.**"""

files=[]

lines_per_file = int(Counter/3)  # Lines on each small file
lines = []  # Stores lines not yet written on a small file
lines_counter = 0  # Same as len(lines)
created_files = 0  # Counting how many small files have been created

with open('input_2.txt') as big_file:
    for line in big_file:  # Go throught the whole big file
        lines.append(line)
        lines_counter += 1
        if lines_counter == lines_per_file:
            idx = lines_per_file * (created_files + 1)
            with open('small_file_%s.txt' % idx, 'w') as small_file:
                # Write all lines on small file
                small_file.write('\n'.join(lines))
                files.append('small_file_%s.txt' % idx,)
            lines = []  # Reset variables
            lines_counter = 0
            created_files += 1  # One more small file has been created
    # After for-loop has finished
    if lines_counter:  # There are still some lines not written on a file?
        idx = lines_per_file * (created_files + 1)
        with open('small_file_%s.txt' % idx, 'w') as small_file:
            # Write them on a last small file
            small_file.write('n'.join(lines))
            files.append('small_file_%s.txt' % idx,)
        created_files += 1

print ('%s small files (with %s lines each) were created.' % (created_files,
                                                             lines_per_file))
print(files)

def add_dashes(file_name):
  with open(file_name, 'r+') as file: 
    originalContent = file.read() 
    file.seek(0, 0)              # Move the cursor to top line 
    file.write("==========")             # Add a new blank line 
    file.write(originalContent) 

for i in files:
  add_dashes(i)

with open('input_2.txt', 'w') as outfile:
  for fname in files:
    with open(fname) as infile:
      for line in infile:
        outfile.write(line)

with open('input_2.txt', 'r') as f:
  contents = f.read()

with open('input_2.txt', 'w') as f:
  f.write(contents.replace("==========", "==========\n"))

with open('input_2.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('input_2.txt', 'w') as fout:
    fout.writelines(data[3:])

with open("input_2.txt", "a") as a_file:
  a_file.write("==========")

with open('input_2.txt') as f: 
	updatedfile="=========="+'\n'+f.read() 
with open('input_2.txt','w') as f: 
	f.write(updatedfile)

with open('input_2.txt', 'r') as fin:
  print(fin.read())
fin.close()

"""# **XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX**

# **Preprocessing the two text files and Segmenting them to make our final `input_1.txt` & `input_2.txt` files**

# **Retriving the two input files i.e., `input_1.txt` & `input_2.txt` and making a `composite.txt`file for our fina evaluation**

splitting both input files whenever the "Choi" notation occurs, with segment boundaries indicated by a row of equal signs.
"""

with open("input_1.txt",'r') as f:
  strt=0
  op="=========="
  cnt=11
  for x in f.read().split('\n'):
    if(x=="=========="):
      if (strt==1):
        opf=open(str(cnt)+'.txt','w')
        opf.write(op)
        opf.close()
        op="=========="
        cnt+=1
      else:
        strt=1
    else:
       op=op + '\n' + x  
f.close()


with open("input_2.txt",'r') as f:
  strt=0
  op="=========="
  cnt=21
  for x in f.read().split('\n'):
    if(x=="=========="):
      if (strt==1):
        opf=open(str(cnt)+'.txt','w')
        opf.write(op)
        opf.close()
        op="=========="
        cnt+=1
      else:
        strt=1
    else:
       op=op + '\n' + x   
f.close()

with open("input_1.txt",'r') as f:
  cnt=0
  for x in f.read().split('\n'):
    if(x=="=========="):
      cnt+=1
  print("input_1.txt has {} markers, means {} different segments".format(cnt,cnt-1))
  len_input_1=cnt-1
f.close()

with open("input_2.txt",'r') as f:
  cnt=0
  for x in f.read().split('\n'):
    if(x=="=========="):
      cnt+=1
  print("input_2.txt has {} markers, means {} different segments".format(cnt,cnt-1))
  len_input_2=cnt-1
f.close()

list1=[]
for i in range(1,len_input_1+1):
  list1.append(str(1)+str(i)+'.txt')
print(list1)

list2=[]
for i in range(1,len_input_2+1):
  list2.append(str(2)+str(i)+'.txt')
print(list2)

def countList(list1, list2): 
    return [sub[item] for item in range(len(list2)) 
                      for sub in [list1, list2]] 

print(countList(list1, list2))

with open('composite.txt', 'w') as outfile:
  for fname in countList(list1, list2):
    with open(fname) as infile:
      for line in infile:
        outfile.write(line)

with open('composite.txt', 'r') as f:
  contents = f.read()

with open('composite.txt', 'w') as f:
  f.write(contents.replace("==========", "\n=========="))

with open("composite.txt", "a") as a_file:
  a_file.write("\n==========")

with open('composite.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('composite.txt', 'w') as fout:
    fout.writelines(data[1:])

with open('composite.txt', 'r') as fin:
  print(fin.read())
fin.close()

"""# XXXXXXXXXXXXXXXXXXXX"""