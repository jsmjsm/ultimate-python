def main():
    x = 1
    x_add_two = x + 2

    # 这种情况显然是真的
    ran_1 = False
    if x_add_two == 3:  # 忽略: else
        ran_1 = True  # 运行
    assert ran_1 is True

    # 否定条件也可以成立
    ran_2 = False
    if not x_add_two == 1:  # 忽略: else
        ran_2 = True  # 运行
    assert ran_2 is True

    # 还有 “else” 语句，如果初始条件失败则运行
    # 请注意，有一行代码被略过了，并且这个条件无助于得到与变量的真实值有关的结论
    if x_add_two == 1:
        ran_3 = False  # 忽略: if
    else:
        ran_3 = True  # 运行
    assert ran_3 is True

    # 一旦所有的 `if` 和 `elif` 条件失败，`else` 的语句将被运行。
    # 注意，很多行被跳过了；并且，为了简单起见，所有条件可以压缩为 `x_add_two！= 3`。
    # 在这种情况下，通过较少的逻辑，可以得到更高的代码清晰度
    if x_add_two == 1:
        ran_4 = False  # 忽略: if
    elif x_add_two == 2:
        ran_4 = False  # 忽略: if
    elif x_add_two < 3 or x_add_two > 3:
        ran_4 = False  # 忽略: if
    else:
        ran_4 = True  # 运行
    assert ran_4 is True


if __name__ == "__main__":
    main()
