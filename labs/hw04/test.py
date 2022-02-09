'''
功能模块与目的: 
版本: 
开发者: 高嘉伟(gaojw20@mails.tsinghua.edu.cn)
Date: 2022-02-09 20:42:42
版权信息: 
最后修改者: 高嘉伟(gaojw20@mails.tsinghua.edu.cn)
LastEditTime: 2022-02-09 20:48:08
修改日志: 
备注: 
'''

from typing import List
import itertools


dictionaries = [chr(i) for i in
                itertools.chain(range(97, 123),    # a - z
                      range(65, 91),    # A - Z
                      range(48, 58))]    # 0 - 9

def all_passwd(dictionaries: List[str], maxlen: int):
    # 返回由 dictinaries 中字符组成的所有长度为 maxlen 的字符串

    def helper(temp: list, start: int, n: int):
        # 辅助函数，是个生成器
        if start == n:    # 达到递归出口
            yield ''.join(temp)
            return
        for t in dictionaries:
            temp[start] = t    # 在每个位置
            yield from helper(temp, start + 1, n)

    yield from helper([0] * maxlen, 0, maxlen)
    
all_passwd(dictionaries, 5)