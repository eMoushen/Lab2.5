#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    C = tuple(map(int, input().split()))

    if len(C) != 24:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    print(C.count(5))