def scope_test():
    """
    作用域规则：

    命名空间：名称到对象的映射。
    """

    def do_local():
        # 没有 `global` 和 `nonlocal` 语句，变量的作用域只为局部，对外部不影响。
        spam = "local spam"

    def do_nonlocal():
        # 非局部作用域指：外层闭包函数作用域。即：全局以内，局部以外。
        nonlocal spam
        spam = "nonlocal spam"

        def nested_nonlocal():
            # 绑定非局部作用域变量名称前，变量必须事先被定义，可以被定义多次，
            # 根据非局部作用域性质，会由内往外查找名称。所以这里绑定了外第二层函数作用域变量 `nested_spam`。
            nonlocal nested_spam
            nested_spam = "nested nonlocal spam"

        nested_nonlocal()

    def do_global():
        # 绑定全局作用域，变量可以不用事先定义。这虽然可行，但如果在此方法执行（全局定义变量并赋值）之前调用了未定义的全局变量将引发错误。
        global spam, undeclared_spam
        spam = "global spam"
        undeclared_spam = "undeclared global spam"

    def variables_name_scopes_rules():
        """
        Python 函数变量的作用域规则范围是整个函数体或类语句体，作用域在函数或类定义时就被确定。
        在没有使用作用域声明关键字（`global` 或 `nonlocal`）声明作用域，且没有赋值行为时，会由内往外逐层查找最近绑定的变量名称。
        此过程不发生作用域指定行为。
        以下情况会进行作用域指定：
          - 在没有使用作用域声明关键字声明作用域，但有赋值行为时，被指定为局部作用域。
          - 在使用了作用域声明关键字声明作用域后，没有赋值行为时，对应作用域被明确指定。

        如果一个变量被多次指定作用域将引发错误（虽然连续地使用相同的作用域声明关键字声明变量作用域可行，但这没有意义）。
        """
        variable_name = "variable name"

        def fun():
            # 赋值行为将作用域改为局部，这里引用的是局部变量，因此会报错
            # print(variable_name)
            # variable_name = "variable name"

            # 先行语句的赋值操作产生作用域指定行为，和后面的作用域声明行为产生冲突，也会报错
            # variable_name = "variable name"
            nonlocal variable_name
            variable_name = "variable name"
            # 删除一个变量，会导致其作用域中的引用确切被删除。
            # 这里删除之后，在此函数外部也无法获取到此变量。
            del variable_name

    spam = "test spam"
    nested_spam = None

    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    print("After multiple nonlocal assignment:", nested_spam)
    do_global()
    print("After global assignment:", spam)


# nested_spam = None  # nonlocal 不能绑定全局作用域变量
scope_test()
print("In global scope:", spam)
print("Undeclared global variable:", undeclared_spam)

if __name__ == "__main__":
    pass
