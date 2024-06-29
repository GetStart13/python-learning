"""
数据结构练习。
"""


def tuple_practice():
    _tuple = ("这是", 1, "个元组")
    print(f"元组第2个值：{_tuple[1]}")
    # 元组拆包
    (this_is, a, __tuple) = _tuple
    print(this_is, a, __tuple)


if __name__ == '__main__':
    tuple_practice()
