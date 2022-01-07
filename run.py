import os

from function import rename, remove, sync, conversion
from utils import input_value_int


def show_operation():
    print("1. 批量同步字幕（仅支持 ass）")
    print("2. 批量字幕重命名")
    print("3. 批量去除繁体")
    print("4. 批量繁体转简体（仅支持 ass）")
    print("5. 批量更改字体（仅支持 ass）")
    return input_value_int("请输入序号执行功能:")


if __name__ == '__main__':
    operation_no = show_operation()
    os.system('cls')
    try:
        if operation_no == 1:
            sync.run()
        elif operation_no == 2:
            rename.run()
        elif operation_no == 3:
            remove.run()
        elif operation_no == 4:
            conversion.run()
    except Exception as e:
        print(e)
    input('输入任意值退出')
