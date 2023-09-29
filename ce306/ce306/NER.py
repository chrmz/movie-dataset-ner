import csv
from html import entities
from lib2to3.pgen2 import token
from matplotlib.pyplot import get
import nltk
import pandas as pd
import numpy as np


with open('M:/ce306/test.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    col = []
    for row in reader:
        plot_ner = row["Plot"]
        print("Plot: %s" %plot_ner)
        tokens = nltk.word_tokenize(plot_ner)
        print(tokens)
        pos_tags = nltk.pos_tag(tokens) #adds tags next to the word
        print(pos_tags)
        entities = nltk.ne_chunk(pos_tags)#breaks down the entities
        element = ""
        for i in entities:
            if (isinstance (i, nltk.Tree)):
                #i [0] #gets first element of the tree
                #print(i [0])
                for j in  i.leaves(): #i leaves the instance for j, which are the string elements and not the tags
                    element += j [0] + " " #retrieves first field of array, which are the strings (Irish, Carrie Nation, Irish and Nation + adds space between two strings)
                print(element)
        col.append(element)
        count+=1
        if count == 100:
            break

#with open('M:ce306/add_plot_ner.csv', 'reader') as csvinput:
    #with open('M:ce306/add_plot_ner/output.csv', 'writer') as csvoutput:
df = pd.read_csv('M:/ce306/test.csv') #dataframe outputs the csv file
df.insert(8, column ="plot_ner", value = col)
df.to_csv('M:/ce306/test.csv', index = False)
print(df.head())


