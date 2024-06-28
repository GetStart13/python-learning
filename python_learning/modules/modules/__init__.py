# 在这里导入模块的属性，在客户代码中就可以通过导入此包而获取已暴露的属性
from .module1 import function1
from .module2 import module_name as module2_name
from .module3 import function3
from .module4 import function4

# `__all__` 列表用于控制希望暴露给用户使用的接口，但主要影响客户代码的 `from module import *` 行为。
__all__ = ["function1", "module2_name"]
