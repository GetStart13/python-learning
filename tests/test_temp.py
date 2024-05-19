import sys

if __name__ == '__main__':
    # 查看一个模块是否在内置模块中
    print("ensurepip is builtin-module?", "ensurepip" in sys.builtin_module_names)
