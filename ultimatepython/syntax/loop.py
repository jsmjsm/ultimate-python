def main():
    # 这是一个 “for” 循环，它在值 0..4 上进行迭代并将每个值添加到变量 “total” 中。
    # 它利用的是 `range` 迭代器。
    # 提供单个整数表示起点为 0 ，终点为 5 ，增量步长为 1（每次增加 1）
    total = 0
    for i in range(5):
        total += i

    # 答案是: 10
    assert total == 10

    # 这是一个 “for” 循环，它迭代值 5..1 并将每个值乘以 “fib”。
    # 通过将起点设置为 5，终点设置为 0，增量步长为 -1（向后退一步）。在这里更明确地使用了 “范围” 迭代器。
    fib = 1
    for i in range(5, 0, -1):
        fib *= i

    # 答案是: 120
    assert fib == 120

    # 这是一个简单的while循环，类似于for循环，不同之处在于：计数器是在循环外部声明，并且其状态在循环内部进行显式管理。
    # 这个循环将持续，直到计数器超过 8
    i = 0
    while i < 8:
        i += 2

    # `while`循环终止于8
    assert i == 8

    # 这是一个`while`循环，以`break`停止，并且其计数器在循环中成倍增加，表明我们可以对计数器执行任何操作。
    # 像上一个“ while”循环一样，该循环一直持续到计数器超过 8
    i = 1
    break_hit = False
    continue_hit = False
    while True:
        i *= 2

        if i >= 8:
<<<<<<< HEAD
            # break语句停止当前的while循环。
            # 如果此“ while”循环嵌套在另一个循环中，则此语句不会停止父循环
            break

        if i == 2:

            # `continue`语句返回到当前`while`循环的开始
=======
            # The `break` statement stops the current `while` loop.
            # If this `while` loop was nested in another loop,
            # this statement would not stop the parent loop
            break_hit = True
            break

        if i == 2:
            # The `continue` statement returns to the start of the
            # current `while` loop
            continue_hit = True
>>>>>>> 1f8f61d4d524b83f6dd07078ada4e7a2d13cbf7d
            continue

        # `while`循环终止于此值
        assert i == 8

    # The `while` loop hit the `break` and `continue` blocks
    assert break_hit is True
    assert continue_hit is True


if __name__ == "__main__":
    main()
