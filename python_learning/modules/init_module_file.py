"""__init__.py 文件：

1、初始化包和定义命名空间
  - __init__.py 文件表示目录是一个 Python 包，它在包或模块被导入时执行。其主要目的是初始化包或模块，并定义包的命名空间（简化导入）。
  - 在 __init__.py 中，可以执行包级别的变量初始化和任务。

2、包结构
  - 项目中不要将过多代码添加到 __init__.py 文件中。在项目复杂度增加时，可能会有子包和子子包，当导入子子包中的单个项目时，
    必须执行遍历树过程中遇到的所有 __init__.py 文件。

3、包文档
  - __init__.py 文件中的 docstring 应该提供包的文档信息，描述包的用途、背景和包内各个组件的整体概况。
"""

if __name__ == '__main__':
    # 导入模块中 `__all__` 声明的属性
    from modules import *

    print(module2_name)
    # function4() # `function4` 不在 `__all__` 列表声明中，因此不可被访问

if __name__ == '__main__':
    # 导入模块中的属性
    from modules import function4, module2_name

    function4()  # 虽然 __init__.py 的 `__all__` 列表并没有声明 `function4`，但 `function4` 作为模块属性，仍然可以被访问
    print(module2_name)
