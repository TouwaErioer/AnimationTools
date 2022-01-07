import datetime
import os

from format.Ass import Ass
from utils import input_value, input_value_int, get_file_type

TEMPLATE = 'Dialogue: '
DATE_FORMAT = '%H:%M:%S.%f'


def handler(text, operation_num):
    if text.find(TEMPLATE) != -1:
        ass = Ass(text.replace(TEMPLATE, ''))
        start = str_to_date(ass.start) + datetime.timedelta(milliseconds=operation_num)
        end = str_to_date(ass.end) + datetime.timedelta(milliseconds=operation_num)
        ass.setStart(date_to_str(start))
        ass.setEnd(date_to_str(end))
        return TEMPLATE + ass.toText()
    return text


def str_to_date(date_str):
    return datetime.datetime.strptime(date_str, DATE_FORMAT)


def date_to_str(date):
    return str(datetime.datetime.strftime(date, DATE_FORMAT))[:-4]


def run():
    path = input_value('请输入文件夹路径：')
    if os.path.isdir(path) is False:
        raise Exception('文件夹不存在')
    operation_num = input_value_int('请输入字幕偏移量（单位：毫秒）：')
    num = 0
    for path, dir_list, file_list in os.walk(path):
        for file_name in file_list:
            if get_file_type(file_name) == 'ass':
                ass_path = os.path.join(path, file_name)
                template_path = '%s.bak' % ass_path
                with open(ass_path, 'r', encoding='UTF-8') as r, open(template_path, 'w', encoding='UTF-8') as w:
                    for line in r.readlines():
                        w.write(handler(line, operation_num))
                os.remove(ass_path)
                os.rename(template_path, ass_path)
                num += 1
    if num > 0:
        print('成功！共同步 %d 个字幕' % num)
    else:
        print('失败！文件夹为空或字幕文件格式错误')
