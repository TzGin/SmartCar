# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2019/01/19 11:19:31
@Author  :   Zijing Feng
'''

import sys

def debug_print(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)