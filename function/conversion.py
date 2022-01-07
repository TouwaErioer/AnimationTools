import os

from zhconv import convert

from format.Ass import Ass
from utils import input_value, get_file_type

TEMPLATE = 'Dialogue: '


def handler(text):
    if text.find(TEMPLATE) != -1:
        ass = Ass(text.replace(TEMPLATE, ''))
        ass.setText(convert(ass.text, 'zh-cn'))
        return TEMPLATE + ass.toText()
    return text


def run():
    path = input_value('请输入文件夹路径：')
    if os.path.isdir(path) is False:
        raise Exception('文件夹不存在')
    num = 0
    for path, dir_list, file_list in os.walk(path):
        for file_name in file_list:
            if get_file_type(file_name) == 'ass':
                ass_path = os.path.join(path, file_name)
                template_path = '%s.bak' % ass_path
                with open(ass_path, 'r', encoding='UTF-8') as r, open(template_path, 'w', encoding='UTF-8') as w:
                    for line in r.readlines():
                        w.write(handler(line))
                os.remove(ass_path)
                os.rename(template_path, ass_path)
                num += 1
    if num > 0:
        print('成功！共转换 %d 个字幕' % num)
    else:
        print('失败！文件夹为空或字幕文件格式错误')
