# Following the grouping of articles based on their publication years (in decade intervals) using the dataframe, 
# proceed to save them as text files and organize them into distinct folders corresponding to different decades.
# Upon reviewing this, I realized that the process is redundant. The grouping process can be 
# accomplished within the dataframe, eliminating the need to output them as text files again.
import glob, os
import numpy as np
import pandas as pd

path='C:/Users/过青灯客/'
df=pd.read_excel(path+'20032012.xlsx')
df_tt = df[["title", "date","text"]].copy()# Copy to a new dataframe
df_tt["tdt"] = df_tt["title"]+df_tt["text"]# Create a new column
print(df_tt)
for index, row in df_tt.iterrows():
    print(row)
    if index > len(df_tt):
       break
    else:
       f = open(str(index)+'.txt', 'w',encoding='UTF-8')
       f.write(str(row[3]))
       f.close()
       index+=1
