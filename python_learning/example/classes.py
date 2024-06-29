from dataclasses import dataclass


class Superman:
    power = "unknown"  # 类属性，不可变属性不能够通过对象实例操作（静态变量）
    organization = []

    def __init__(self, name):
        self.name = name  # 实例属性
        self.organization.append(name)  # 可变对象的类属性可通过对象实例操作

    def work(self):  # 方法：实例对象会作为函数的第一个参数被传入
        print(f"My power is {self.power}, my work is save the world!")


class SpiderMan(Superman):  # 继承
    power = "cobweb"

    def work(self):  # 重写方法
        print(f"I am {self.name}.")
        super().work()  # 调用基类方法，也可以通过基类名称显式指定调用


class IronMan(Superman):
    power = "iron robot"

    def work(self):
        print("I am iron man.")
        Superman.work(self)  # 通过基类名称显式指定调用

    def invent(self, something):
        print(f"I am {self.name}, I am inventing {something}.")

    def invite(self, someone):
        # 操作类的可变对象
        self.organization.append(someone)


class GreenBigMan(Superman):
    power = "powerful"

    def __init__(self, name, power, place, natasha_name):
        super().__init__(name)
        # 类属性 power 为不可变属性，此操作对类属性 power 无效，但对实例属性有效
        self.power = power
        self._place = place
        self.__natasha_name = natasha_name

    def _run(self):  # 约定：带有一个下划线的名称应该被当作是 API 的非公有部分
        print(f"I don't know where I'm going to run away,maybe {self._place}.")

    # 名称改写：至少带有两个前缀下划线，至多一个后缀下划线的类属性名称，被定义为类私有变量，会被进行名称改写
    # 改写形式：_<className>__<property_name>
    def __save(self):
        print(f"Natasha knows where I am, her name is {self.__natasha_name}.")


class TinySpider(SpiderMan, IronMan):  # 多重继承，继承的属性的搜索规则是深度优先、从左到右
    power = "spider-iron-clothes"

    def append_instance_properties(self):
        # 未在 `__init__` 方法中声明的属性，访问时将会报错
        self.property = "New property."


# 数据类型
@dataclass
class Person:
    name: str
    age: int
    weight: int


# 生成器，用于创建迭代器，即：可以使用 `for item in generator(data)` 的形式
def generator(data):
    for index in range(len(data)):
        yield data[index]


if __name__ == "__main__":
    PeterParker = SpiderMan("Peter Parker")
    PeterParker.work()

    tiny_spider = TinySpider("tiny Peter Parker")
    # 先从本类中查找，未找到则查找父类，仍未找到则向右查找继承类，并继续按继承深度查找
    tiny_spider.invent("Iron-Clothes")
    # 未在 `__init__` 方法中声明的属性，访问时将会报错
    # print(f"tiny_spider.property is {tiny_spider.property}")

    Banner = GreenBigMan("Banner", "Green Big Bomb!", "Everywhere", "Black Spider Women")
    # 虽然可以调用，但不建议，应遵循约定
    Banner._run()
    # 调用失败，双下划线开头为类私有变量
    # Banner.__save()
    # 可以调用，显式指定了改写之后的类私有属性，但不应该这么做，这里用于验证改写
    Banner._GreenBigMan__save()

    TonyStark = IronMan("TonyStark")
    SmallChili = IronMan("SmallChili")
    # 查看类变量（共享变量）
    print(f"TonyStark's power is {TonyStark.power}.")
    print(f"SmallChili's power is {SmallChili.power}.")
    # GreenBigMan 实例化时对 power 的赋值并没有影响类属性，而是重新声明了一个实例属性
    print(f"GreenBigMan's power is {GreenBigMan.power}.")
    # GreenBigMan 的实例属性（Banner）与类属性同名，但值不同
    print(f"Banner's power is {Banner.power}.")

    TonyStark.invite("me")
    print("A mutable object as class variable that everyone can change it:", Superman.organization)

    person = Person("Tony", 20, 20)
    print(person)

    for char in generator("generator"):
        print(char)
