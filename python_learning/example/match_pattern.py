class Point:
    # 在模式匹配中如果使用类名作为匹配，默认不允许使用位置参数，为了允许这种匹配，就需要设置 __match_args__ 属性
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def matcher(points):
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(y, x) as point]:  # 根据位置顺序匹配，参数数量必须少于或等于 __match_args__ 元素数量
            print(f"Single point {x}, {y}")
            print("as 关键字作为别名:", "x:", point.x, ", y:", point.y)
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")
