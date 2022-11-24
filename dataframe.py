import pandas as pd
import numpy as np

#first
df=pd.read_csv('annotation.csv',delimiter=';')
print(df)
#second
df.rename(columns={"Класс":"Class"})
#third
shape=df.shape
print(shape)
for row in shape:
    if df.Класс
        df.loc[[df.index[row]],'Метка']=0

