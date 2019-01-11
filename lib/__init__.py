/*
 * @Author: Zijing Feng 
 * @Date: 2018-12-18 
 * @Last Modified by: Zijing Feng
 * @Last Modified time: 2019-01-10 20:55:31
 */

#-*- coding: utf-8 -*-
import sys

def debug_print(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)