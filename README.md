# Bayesian-Unsupervised-Topic-Segmentation_Replica


<p align="center">
  <img width="260" height="150" src="https://github.com/rohitmanral/Bayesian-Unsupervised-Topic-Segmentation_Replica/blob/main/Output%20AWS.png">
</p>


## Overall Goal
For this task, I will be working with the code associated with the paper [Bayesian Unsupervised Topic Segmentation](https://www.aclweb.org/anthology/D08-1035.pdf). I will create some new input data for this code by writing and running a script, and report the output results.

## Data
As described in the paper, the aim of the code is to segment text where the topic changes.  The sample data, used for evaluation in the paper, is from a medical textbook; the topic there changes in each section of the book.

Have a look at the sample data and its documentation to understand how segments are indicated and what segment dividers are used.

You can create your own artificial dataset by taking two documents on different topics, splitting them up, and interleaving the segments.  So if you have doc1 on topic A, and doc2 on topic B, you can create a composite document where you know the topic changes, of the form:
doc1_seg1 doc2_seg1 doc1_seg2 doc2_seg2 ... doc1_segN doc2_segN
## Method
To demonstrate that you understand how segmentation is indicated in the sample data, you will count the number of segmentation markers in two specific files.

You should write a script that takes two documents as inputs and produces the composite document as output.

The script should be one of a Python Notebook, a Python command-line script, or a bash script.

You should run the text segmentation code on the composite document in a VM.

## Resulting Documents
i) The two input data documents, as two .txt files.

ii) The composite output document, as a single file composite.txt. 

iii) The script mixFiles.ipynb, mixFiles.py or mixFiles.sh (depending on whether it's a Python Notebook, Python script or bash script, respectively). 

iv) A text file comments.txt which includes the following:

* A comment noting how many segmentation markers there are for your two specific sample data files.
* A comment noting where the source documents come from. (This could just be two URLs.)
* A comment giving the results of processing the composite document  (i.e. the scores produced by the program) under the configuration dp.config.
* A brief note about whether the scores are what might be expected.  

v) A screenshot of the output of the text segmentation program inside your VM. Once you run your script on the VM, run the following command; the screenshot should contain both the output of the file processing and the output of the command below:
ping -c 1 www.theculinaryacademy.org && curl http://checkip.amazonaws.com
