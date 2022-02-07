'''
功能模块与目的: 
版本: 
开发者: 高嘉伟(gaojw20@mails.tsinghua.edu.cn)
Date: 2022-02-07 21:07:06
版权信息: 
最后修改者: 高嘉伟(gaojw20@mails.tsinghua.edu.cn)
LastEditTime: 2022-02-07 22:23:29
修改日志: 
备注: 
'''
this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    call_time = -1
    def add_function(b):
        nonlocal call_time
        call_time = call_time + 1
        return a + b + call_time
    return add_function

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    prepre = -1
    pre = 1
    def fib_function():
        nonlocal prepre, pre
        pre = prepre + pre
        prepre = pre - prepre
        return pre
    return fib_function

def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """

    hit_index = []
    for i in range(len(lst)):
        if lst[i] == entry:
            hit_index.append(i)
    for i in range(len(hit_index)):
        lst.insert(hit_index[i] + i + 1, elem)
    return lst
