"""
.py 结尾的文件是一个 Python 模块。

注意：为了保证运行效率，每次解释器会话只导入一次模块。如果更改了模块内容，必须重启解释器；
仅交互测试一个模块时，也可以使用 `importlib.reload()`，
例如 `import importlib; importlib.reload(modulename)`。
"""

# import 导入模块，此位置位于模块的最高层级，此操作只会将模块名称导入到当前模块的全局命名空间中，而不导入模块内函数名称。
# 可以使用 as 定义别名，如果这么做，原模块名称将失效。
# 模块被多次导入时，模块内定义语句会且只会在第一次导入时被执行。
# 启动模块（主模块）中必须使用绝对导入！
from python_learning.modules.modules import module1 as md1
# 导入同一个包中的模块可以使用相对路径。
# （注意：此模块被多次导入，但其内部可执行语句只执行了一次）
from .modules import module1

# 也可以将模块的全局属性导入到导入方模块的命名空间中，如果属性名发生重复冲突，根据作用域规则，位于导入方的模块属性会生效。
# 这条语句不会将被导入模块的名称引入到命名空间中（`module3` 将是未定义的）：
from python_learning.modules.modules.module3 import function3
# 同样，被导入的属性也可以使用别名，可以用此形式避免名称重复冲突。
# 注意，即使只导入了属性，模块内可执行语句仍会被执行一次。
from python_learning.modules.modules.module2 import function2 as func2, module_name


# import * 会导入除下划线（_）开头的属性名称。如果的确需要这些属性，可以在 import 关键字后面显式指定名称导入。
# 通常不建议使用 * 导入，因为你不知道导入了什么，但如果是在交互模式下使用 * 导入，则可以简化导入减少输入字符数量。


# 转到测试类以启动执行此方法（由于此模块中使用了相对定位导入）
def module_main():
    md1.function1()

    module1.function1()

    function2()
    func2()
    print("模块 2 被导入属性名:", module_name)

    # __function3()  # _ 开头的函数不被 import * 导入
    function3()

    # function4()  # 局部导入的模块不被更高层作用域引用


def function2():
    print("主模块方法被调用。用于检测函数名冲突。")

    # 局部导入模块
    from python_learning.modules.modules.module4 import function4
    function4()


if __name__ == "__main__":
    """
    注意，相对导入基于当前模块名。因为主模块名永远是 "__main__" ，所以如果计划将一个模块用作 Python 应用程序的主模块，
    那么该模块内的导入语句必须始终使用绝对导入。
    由于此模块中使用了相对导入，因此此入口语句将会 ** 执行失败 **。
    """
    module_main()
