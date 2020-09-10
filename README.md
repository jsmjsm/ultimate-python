# Ultimate Python study guide

![](https://img.shields.io/circleci/build/github/huangsam/ultimate-python)
![](https://img.shields.io/github/license/huangsam/ultimate-python)

Ultimate Python study guide for newcomers and professionals alike. :snake: :snake: :snake:

```python
print("Ultimate Python study guide")
```

## Motivation

I created a GitHub repo to share what I've learned about [core Python](https://www.python.org/)
over the past 5+ years of using it as a college graduate, an employee at
large-scale companies and an open-source contributor of repositories like
[Celery](https://github.com/celery/celery) and
[Full Stack Python](https://github.com/mattmakai/fullstackpython.com).
I look forward to seeing more people learn Python and pursue their passions
through it. :mortar_board:

## Goals

Here are the primary goals of creating this guide:

:trophy: **Serve as a resource** for Python newcomers who prefer to learn hands-on.
This repository has a collection of standalone modules which can be run in an IDE
like [PyCharm](https://www.jetbrains.com/pycharm/) and in the browser like
[Repl.it](https://repl.it/languages/python3). Even a plain old terminal will work
with the examples. Most lines have carefully crafted comments which guide a reader
through what the programs are doing step-by-step. Users are encouraged to modify
source code anywhere as long as the `main` routines are not deleted and
[run successfully](runner.py) after each change.

:trophy: **Serve as a pure guide** for those who want to revisit core Python concepts.
Only [builtin libraries](https://docs.python.org/3/library/) are leveraged so that
these concepts can be conveyed without the overhead of domain-specific concepts. As
such, popular open-source libraries and frameworks (i.e. `sqlalchemy`, `requests`,
`pandas`) are not installed. However, reading the source code in these frameworks is
inspiring and highly encouraged if your goal is to become a true
[Pythonista](https://www.urbandictionary.com/define.php?term=pythonista).

## Table of contents

:books: = External resource,
:cake: = Beginner topic,
:exploding_head: = Advanced topic

1. **About Python**
    - Overview: [What is Python](https://github.com/trekhleb/learn-python/blob/master/src/getting_started/what_is_python.md) (:books:, :cake:)
    - Design Philosophy: [The Zen of Python](https://www.python.org/dev/peps/pep-0020/) (:books:)
    - Style Guide: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) (:books:, :exploding_head:)
    - Data Model: [Data model](https://docs.python.org/3/reference/datamodel.html) (:books:, :exploding_head:)
2. **语法**
    - 变量: [内置文字类型](ultimatepython/syntax/variable.py) (:cake:)
    - 表达式: [对数字的操作](ultimatepython/syntax/expression.py) (:cake:)
    - 控制条件: [if | if-else | if-elif-else](ultimatepython/syntax/conditional.py) (:cake:)
    - 循环: [for-loop | while-loop](ultimatepython/syntax/loop.py) (:cake:)
    - 函数: [def | lambda](ultimatepython/syntax/function.py) (:cake:)
3. **Data Structures**
    - List: [List operations](ultimatepython/data_structures/list.py) (:cake:)
    - Tuple: [Tuple operations](ultimatepython/data_structures/tuple.py)
    - Set: [Set operations](ultimatepython/data_structures/set.py)
    - Dict: [Dictionary operations](ultimatepython/data_structures/dict.py) (:cake:)
    - Comprehension: [list | tuple | set | dict](ultimatepython/data_structures/comprehension.py)
    - String: [String operations](ultimatepython/data_structures/string.py) (:cake:)
4. **Classes**
    - Basic class: [Basic definition](ultimatepython/classes/basic_class.py) (:cake:)
    - Abstract class: [Abstract definition](ultimatepython/classes/abstract_class.py)
    - Exception class: [Exception definition](ultimatepython/classes/exception_class.py)
    - Iterator class: [Iterator definition | yield](ultimatepython/classes/iterator_class.py) (:exploding_head:)
5. **Advanced**
    - Decorator: [contextlib | wraps](ultimatepython/advanced/decorator.py) (:exploding_head:)
    - Metaclass: [Metaclass definition](ultimatepython/advanced/meta_class.py) (:exploding_head:)
    - Method Resolution Order: [mro](ultimatepython/advanced/mro.py) (:exploding_head:)
    - Asyncio: [async | await](ultimatepython/advanced/async.py) (:exploding_head:)
    - Weak reference: [weakref](ultimatepython/advanced/weak_ref.py) (:exploding_head:)
    - Benchmark: [cProfile | pstats](ultimatepython/advanced/benchmark.py) (:exploding_head:)

## Additional resources

:necktie: = Interview resource,
:test_tube: = Code samples,
:brain: = Project ideas

### GitHub repositories

Keep learning by reading from other well-regarded resources.

- [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) (:necktie:, :test_tube:)
- [faif/python-patterns](https://github.com/faif/python-patterns) (:necktie:, :test_tube:)
- [geekcomputers/Python](https://github.com/geekcomputers/Python) (:test_tube:)
- [karan/Projects](https://github.com/karan/Projects) (:brain:)
- [vinta/awesome-python](https://github.com/vinta/awesome-python) (:brain:)
- [MunGell/awesome-for-beginners](https://github.com/MunGell/awesome-for-beginners) (:brain:)

### Interactive practice

Keep practicing so that your coding skills don't get rusty.

- [leetcode.com](https://leetcode.com/) (:necktie:)
- [hackerrank.com](https://www.hackerrank.com/) (:necktie:)
- [codesignal.com](https://codesignal.com/) (:necktie:)
- [exercism.io](https://exercism.io/)
- [projecteuler.net](https://projecteuler.net/)
