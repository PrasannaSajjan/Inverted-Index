import sys
from itertools
import *
num_arg = len(sys.argv)
if num_arg < 2:
    print 'Usage: inverted_index.py document_1 document_2 ... document_n'
else :
    input = []
input = sys.argv[1: ]
indexing = {}
for file in input:
    f = open(file, 'r')
words = f.read().strip().lower().split(" ")# split the words
for word in words:
    if word in indexing:
    indexing[word].append(file)
else :
    indexing[word] = []
indexing[word].append(file)
f.close()
for k, v in indexing.items():
    print k, v