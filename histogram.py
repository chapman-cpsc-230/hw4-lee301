"""
File: <histogram.py>

Copyright (c) 2016 Krystal Lee

License: MIT

<Define histogram>
"""

ls = [4, 9, 13, 5]


def bar(number):
    string = " "
    for i in range(number):
        string += "*"
    return string

for i in range(len(ls)):
    print bar(ls[i])
