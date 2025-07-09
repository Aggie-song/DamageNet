# test_path.py
import os

test_path = ""
if os.path.exists(test_path):
    print(" 验证通过：文件存在")
    try:
        with open(test_path, "rb") as f:
            print(" 文件可正常读取")
    except PermissionError:
        print(" 权限不足：无法读取文件")
else:
    print(" 文件不存在，请检查路径")