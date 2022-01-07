import os

from utils import input_value, get_file_type, choose_point


def run():
    path = input_value('请输入文件夹路径:')
    if os.path.isdir(path) is False:
        raise Exception('文件夹不存在')
    point_start = 0
    point_end = 0
    num = 0
    for path, dir_list, file_list in os.walk(path):
        for i, file_name in enumerate(file_list, 1):
            if i == 1:
                print(file_name)
                point = input_value('请输入特征点：')
                point_start = choose_point(file_name, point)
                point_end = point_start + len(point)
            file_type = get_file_type(file_name)
            file_path = os.path.join(path, file_name)
            file_name = file_name[point_start:point_end]
            try:
                os.rename(file_path, os.path.join(path, file_name + '.' + file_type))
            except Exception as e:
                print(e)
                file_name = input_value('请手动命名:')
                os.rename(file_path, os.path.join(path, file_name + '.' + file_type))
            num += 1
    if num > 0:
        print('重命名成功！共完成 %d 个文件' % num)
    else:
        print('重命名成功！文件夹不存在')
