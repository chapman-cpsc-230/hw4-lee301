"""File: <histogram2.py>

Copyright (c) 2016 Krystal Lee

License: MIT

<improve the histogram procedure using the digits function>
"""

ls = ([4, 9, 13, 5])

print " n|data"
print "---+----------------"

def bar(number):
    string = " "
    for i in range(number):
        string += "*"
    return string

for i in range(len(ls)):
    print ls[i], "|", bar(ls[i])
    
