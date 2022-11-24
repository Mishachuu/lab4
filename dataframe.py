import pandas as pd
import numpy as np
import cv2
import os

# first
df = pd.read_csv('annotation.csv', delimiter=';')
# print(df)
# second
df = df.rename(columns={"Абсолютный путь": "absolute_path", "Класс": "class_"})

# third
df['marks'] = df['class_'].apply(lambda x: '0' if x == 'cat' else '1')
# fourth
height_list = []
width_list = []
channels_list = []
size_list=[]
absolute_path_list = df.absolute_path.tolist()
for row in absolute_path_list:
    image = cv2.imread(row)
    height_list.append(image.shape[0])
    width_list.append(image.shape[1])
    channels_list.append(image.shape[2])
    size_list.append(image.size)
df["height"] = height_list
df["width"] = width_list
df["channels"] = channels_list
df["size"]=size_list
# print(df)
# five

# six


def sort_marks(df, mark: int) -> df:
    return df[df.marks == f'{mark}']
# seven


def sort_max(df, mark: int, max_height: int, max_width)->df:
    return df[((df.marks == f'{mark}') & (df.height < max_height) & (df.width < max_width))]

# eighth
print(df.size)
df2 = df.groupby(['marks']).agg({"size":["max","mean","min"]}).reset_index()
print(df2)
