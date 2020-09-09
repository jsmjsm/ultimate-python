# -*- coding: utf-8 -*

def main():
    # 这是要注意的主要数据类型
    a = 1
    b = 2.0
    c = True
    d = "hello"

    # 请注意，每种类型都是一个类。
    # 上面的每个变量都引用了它所属的类的一个实例
    a_type = type(a)
    b_type = type(b)
    c_type = type(c)
    d_type = type(d)

    # 现在，让我们认识 `assert` 关键字。
    # 这是一个调试辅助工具，在我们逐步执行每个`main`函数时，我们将使用它们来验证代码。
    # 这些语句用于验证数据的正确性并减少发送到屏幕的输出量
    assert a_type is int
    assert b_type is float
    assert c_type is bool
    assert d_type is str

    # Python中的一切都是对象。这意味着实例是对象，类也是对象
    assert isinstance(a, object) and isinstance(a_type, object)
    assert isinstance(b, object) and isinstance(b_type, object)
    assert isinstance(c, object) and isinstance(c_type, object)
    assert isinstance(d, object) and isinstance(d_type, object)


if __name__ == '__main__':
    main()
