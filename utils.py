import os

import chardet


def input_value(tip):
    value = input(tip)
    if value == '':
        print('输入为空，请重新输入:')
        input_value(tip)
    return value


def input_value_int(tip):
    try:
        return int(input(tip))
    except ValueError:
        input_value_int('请输入数字:')


def clear():
    os.system('cls')


def get_file_type(file_name: str):
    return file_name.split('.')[-1]


def str_color(text):
    return '\033[33m' + text + '\033[0m'


def choose_point(name, feature_point, start=0):
    clear()
    index = name.find(feature_point, start, len(name))
    if index != -1:
        point_local = index + len(feature_point)
        print(name[:index] + str_color('*') + feature_point + str_color('*') + name[point_local:])
        agree = input('是否为合适的位置(y/n)?')
        if agree == 'n':
            return choose_point(name, feature_point, point_local)
        elif agree == 'y':
            return index


def get_file_encoding(file):
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']
