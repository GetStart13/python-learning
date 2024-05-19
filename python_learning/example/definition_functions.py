"""
函数定义练习。
"""


def function(x, y, *_tuple, **keywords):
    """各参数说明：

    x 和 y 通过位置顺序绑定，称为：位置参数。
    :param x:
    :param y:
    :param _tuple: 单符号 * 开头，表示接收一个除形参列表之外的位置参数的元组，即：任意实参列表。
    :param keywords: 双符号 ** 开头，表示接收关键字参数列表，例如：key="key", word="word"。
    :return:
    """
    print("x:", x)
    print("y:", y)
    for item in _tuple:
        print(item)
    print("keymap:", keywords)


def special_parameters(pos1, pos2="default", /, pos_or_kwd1="", pos_or_kwd2="", *, kwd1, kwd2):
    """特殊参数：

    符号 / 分隔的前面部分必须是位置参数，后面部分可为位置参数或关键字参数。

    符号 * 之后的参数必须是关键字参数。如果 * 存在，则参数中不能出现通配符参数 *param 或 **param。

    默认值：
      对于位置参数，被设置默认值的参数必须位于未设置默认值参数之后。

    各类型参数使用场景：
      - 使用仅限位置形参，可以让用户无法使用形参名。形参名没有实际意义时，强制调用函数的实参顺序时，或同时接收位置形参和关键字时，这种方式很有用。
      - 当形参名有实际意义，且显式名称可以让函数定义更易理解时，阻止用户依赖传递实参的位置时，才使用关键字。\n
      - 对于 API，使用仅限位置形参，可以防止未来修改形参名时造成破坏性的 API 变动。\n
    """
    print(pos1, pos2, pos_or_kwd1, pos_or_kwd2, kwd1, kwd2)


def unpacking():
    """解包行为：

    符号 * 用于解包列表或元组。

    符号 ** 用于解包字典。
    """
    _list = [1, 2, 3]
    _tuple = (7, 8, 9)
    list_combined = [*_list, *[4, 5, 6], *_tuple]
    print("List combined:", list_combined)

    name = {"name": "logic-queue"}
    me = {**name, **{"age": 26}}
    print("My messages:", me)


# noinspection PyUnusedLocal
# 抑制警告，PyUnusedLocal 为对应的警告代码
def combine_positional_and_keyword_arguments(name, /, **keywords):
    """位置参数与关键字参数组合：

    两者组合可能会发生潜在冲突。
    本例中，在未添加 / 的情况下，如果 keywords 接收的参数中存在键为 name 的数据，将会产生错误。

    加入 / 后，将位置参数与关键字参数区分，代码将运行正常。
    """
    result = "name" in keywords
    print("Parameter keywords has the key 'name'?", result)


def lambda_expression(number):
    """
    lambda 关键字用于创建小巧的匿名函数。
    """
    return _execute_lambda(lambda x: x + number)


def _execute_lambda(_lambda):
    provide = 10
    return _lambda(provide)


def annotations(number: int, description: str) -> str:
    """
    函数注解用于标注参数和返回值的类型。
    但并不具备限定作用，输入时仍然可以不遵循类型标注。
    """
    return "这是 " + str(number) + " 个 " + description
