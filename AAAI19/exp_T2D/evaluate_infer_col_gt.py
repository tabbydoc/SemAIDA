import os
import sys
import argparse
from util_kb import super_classes
from util_t2d import read_col_gt

"""
This file contains a script that
extracts column ground truth classes of columns of T2Dv2
output: column_gt_extend_fg.csv (best class + okay classes of each column)
"""
"""
Скрипт первого шага. 
Находит для каждого столбца класс из DbPedia
Результатом является csv-файл column_gt_extend_fg.csv (Номер таблицы, Лучший класс для столбца + подходящие классы)
"""
# -*- coding: utf-8 -*-

current_path = os.path.dirname(os.path.realpath(sys.argv[0]))
parser = argparse.ArgumentParser()

parser.add_argument(
    '--io_dir',
    type=str,
    default=os.path.join(current_path, 'in_out'),
    help='Directory of input/output')
FLAGS, unparsed = parser.parse_known_args()


def extract_classes_columns():
    # Читаем намера таблиц и их супер классы
    # Из файла col_class_checked_fg
    col_classes = read_col_gt()

    # Дополняем этот словарь 'окей' классами из DBPedia
    col_classes = super_classes(col_classes)

    # Записываем в файл с строгим форматированием
    with open(os.path.join(FLAGS.io_dir, 'column_gt_extend_fg.csv'), 'w', encoding="utf-8") as f:
        for col in col_classes.keys():
            joined_str = '","'.join(col_classes[col])
            classes_str = f'"{joined_str}"'
            f.write(f'"{col}", "{classes_str}"\n')


if __name__ == '__main__':
    extract_classes_columns()
