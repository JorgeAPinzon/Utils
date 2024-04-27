#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:59:06 2024

@author: antiXLinux
"""

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: Division por cero no permitida'


# if __name__ == "__main__":
#     print(divide(100, 0))