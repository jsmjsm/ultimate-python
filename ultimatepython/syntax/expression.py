def main():
    # 这是一个简单的整数。
    x = 1

    # 它的值可以用作表达式的一部分。
    assert x + 1 == 2

    # 表达式可以无限地链接。
    # 链接表达式的概念很强大，因为随着时间的推移，它使我们可以将简单的代码段组合成较大的代码段。
    assert x * 2 * 2 * 2 == 8

<<<<<<< HEAD
    # 除法在Python中有点棘手，因为默认情况下它返回类型为'float'的结果。
    assert x / 2 == 0.5

    # 如果需要整数除法 ， 则必须在表达式中添加一个额外的斜杠 `/`。
=======
    # Division is tricky because Python 3.x returns 0.5 of type `float`
    # whereas Python 2.x returns 0 of type `int`. If this line fails, it
    # is a sign that the wrong version of Python was used
    assert x / 2 == 0.5

    # If an integer division is desired, then an extra slash must be
    # added to the expression. In Python 2.x and Python 3.x, the behavior
    # is exactly the same
>>>>>>> 1f8f61d4d524b83f6dd07078ada4e7a2d13cbf7d
    assert x // 2 == 0

    # 整数的幂也是可以使用的。
    # 如果需要更多功能，则可以利用内置的`math`库或第三方库。
    # 否则，我们不得不搭建自己的数学库。
    assert x * 2 ** 3 == 8


if __name__ == "__main__":
    main()
