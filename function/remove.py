import os

from utils import input_value


def run():
    path = input_value('请输入文件夹路径:')
    if os.path.isdir(path) is False:
        raise Exception('文件夹不存在')
    point = input_value('请输入特征点：')
    res = 0
    num = 0
    for path, dir_list, file_list in os.walk(path):
        for file_name in file_list:
            file_path = os.path.join(path, file_name)
            if file_name.find(point) != -1:
                if res < 3:
                    agree = input('是否删除 %s?(y/n)' % file_name)
                    if agree == 'y':
                        os.remove(file_path)
                        res += 1
                        num += 1
                else:
                    os.remove(file_path)
                    num += 1
    if num > 0:
        print('批量去除繁体成功！共删除 %d 个文件' % num)
    else:
        print('批量去除繁体失败！没有找到特征点')
