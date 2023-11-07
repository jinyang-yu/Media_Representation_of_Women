# Collect the text files acquired via web scraping into a single dataframe.
import pandas as pd
import numpy as np
import nltk
import glob, os

all=[]
path= 'C:/学习/python/Thesis/Scraping'
os.chdir(path) # directory of text files
filelist = glob.glob("*.txt")
print(filelist)
for file in filelist:
    fin = open(file, "rt", encoding="utf8")#read input file
    data = fin.read()#read file contents to string
    data = data.replace("\t", "")#replace all occurrences of the required string
    #print(data)
    fin.close()#close the input file
    fout = open(file, "wt", encoding="utf8")#open the input file in write mode
    fout.write(data)#overwrite the input file with the result data
    fout.close()#close the file

#construct dataframe
    df = pd.read_table(file, names=['txt'], on_bad_lines='skip', header=None)
    df.insert(0, "structure", range(len(df)))
    df.loc[0,'structure'] = 'title'
    df.loc[1,'structure'] = 'date'
    for i in range(2,len(df)):
        df["structure"][i] ='text'

#exchange row and column
    def combine(df):
        return''.join(df.values)
    s=df.groupby(['structure'])['txt'].apply(combine)
    df=s.to_frame()
    df.insert(1, "newcol", range(len(df)))
    #print(df)
    df=df.stack()
    df=df.unstack(level=0)
    df=df.drop(['newcol'])
    order=['title','date','text']
    try:
        df=df[order]
        all.append(df)
    except:
        continue
#concatenate dataframe
    #print(all)
dfall = pd.concat(all, ignore_index=True)
print(dfall)
outputpath='C:/Users/过青灯客/all.csv'
dfall.to_csv(outputpath,sep=',',index=True,header=True,encoding='utf_8_sig')
