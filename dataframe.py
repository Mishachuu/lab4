import pandas as pd
import numpy as np

#first
df=pd.read_csv('annotation.csv',delimiter=';')
print(df)
#second
df=df.rename(columns={"Абсолютный путь":"absolute_path","Класс":"class"})
print(df)
#third
df['marks'] = df['class'].apply(lambda x: '0' if x == 'cat' else '1')
print(df)
