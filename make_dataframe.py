from random import randint

import cv2
import pandas as pd
from matplotlib import pyplot as plt

# six


def sort_marks(df: pd.DataFrame, mark: int) -> pd.DataFrame:
    """сортирует датафрейм по заданной метке

    Args:
        df (pd.DataFrame): датафрейм
        mark (int): метка класса

    Returns:
        df (pd.DataFrame): датафрейм отсортированный
    """
    return df[df.marks == f'{mark}']
# seven


def sort_max(df: pd.DataFrame, mark: int, max_height: int, max_width) -> pd.DataFrame:
    """сортирует датафрейм по заданным значениям

    Args:
        df (pd.DataFrame): датафрейм
        mark (int): метка класса
        max_height (int): максимальная высота
        max_width (_type_): максимальная ширина

    Returns:
        pd.DataFrame: датафрейм отсортированный
    """
    return df[((df.marks == f'{mark}') & (df.height < max_height) & (df.width < max_width))]


# nine

def histograms(df: pd.DataFrame) -> None:
    """Создает гистограмму

    Args:
        df (pd.DataFrame): датафрейм
    """
    absolute_path_list = df.absolute_path.tolist()
    image = cv2.imread(absolute_path_list[randint(0, 2000)])
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


def main():

    # first
    df = pd.read_csv('annotation.csv', delimiter=';')
    print("Исходный датафрейм")
    print(df)
    # second
    df = df.rename(
        columns={"Абсолютный путь": "absolute_path", "Класс": "class_"})
    print("датафрейм с измененными колонками в соответствии с рекомендациями")
    print(df)
    # third
    df['marks'] = df['class_'].apply(lambda x: '0' if x == 'cat' else '1')
    print("Присваиваивание классам меток")
    print(df)
    # fourth
    height_list = []
    width_list = []
    channels_list = []
    size_list = []
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
    df["size"] = size_list
    print("Добавление высоты|ширины|размера изображений")
    print(df)
    # five
    print("Статистика")
    print(df[["height", "width", "channels"]].describe())

    df_marks = sort_marks(df, 0)
    print("Сортировка по метке")
    print(df_marks)
    df_max = sort_max(df, 0, 600, 800)
    print("Сортировка по заданым значениям высоты|ширины")
    print(df_max)
    # eighth
    df2 = df.groupby(['marks']).agg(
        {"size": ["max", "mean", "min"]}).reset_index()
    print("Группировка датафрейма")
    print(df2)
    print("Гистограмма рандомного изображения")
    histograms(df, 0)


if __name__ == "__main__":
    main()
