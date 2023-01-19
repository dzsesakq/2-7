#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f():
    def g(x):
        return x + 3

    return g


if __name__ == '__main__':
    k = int(input("ввод -> "))
    cnt = f()
    print(cnt(k))
