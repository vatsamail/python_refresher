import os
import sys
import itertools

"""
Shall deal with Built In functions as Python is a batteries-included language!
There are 70+ built in functions
"""

def oddFilter(x):
    if x %2 == 0:
        return False
    return True

def lowFilter(x):
    if x.islower():
        return True
    return False

def sqFunc(x):
    return x**2

def toGrade(x):
    if x >= 95:
        return 'A+'
    if x >= 90:
        return 'A'
    if x >= 85:
        return 'B+'
    if x >= 80:
        return 'B'
    if x > 70:
        return 'C'
    if x > 50:
        return 'D'
    return 'F'


def testFunc(x):
    return x < 50



def main():
    # arithmetic checks on the list -- 
    l1 = [1, 2, 3, 4, 5, 6, 0 ]
    l2 = [12, 23, 45]

    print(any(l1)) # True
    print(all(l1)) # False
    print(all(l2)) # True

    print(sum(l1))
    print(min(l2))
    print(max(l2))

    # iterators -- 
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    dins = ['Bha', 'Som', 'Man', 'Bud', 'Gur', 'Shu', 'Sha', 'extra day will not be printed']

    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))


    with open('input_file.txt', 'r') as fp:
        for line in iter(fp.readline, ''):
            print(line.strip())

    for i, m in enumerate(days, start=1):
        print(i, m)


    for i, m in enumerate(zip(days, dins), start=1): # zip gives you a tuple
        print(i, m[0], "in Hindi is", m[1])    

    # Transforms -- 
    nums = [1, 3, 2, 4, 6, 11, 71, 6, 0, 33]
    chars = 'arewoFfSwrYH1#6'
    grades = (91, 89, 87, 99, 83, 93)

    odds = list(filter(oddFilter, nums))
    print("Odds:", odds)

    lower = list(filter(lowFilter, chars))
    print("Lower", lower)

    sqs = list(map(sqFunc, nums)) # map
    print("Squares:", sqs)

    # grades = sorted(grades)
    letters = list(map(toGrade, grades))
    for i in zip(letters, grades):
        print("Grade:", i[0], i[1])


    # itertools
    seq = ('Joe', 'Bob', 'Su')

    # cycles ---
    c1 = itertools.cycle(seq)
    print(next(c1))
    print(next(c1))
    print(next(c1))
    print(next(c1))

    # counter ---
    counter = itertools.count(100, 10)
    print(next(counter))
    print(next(counter))
    print(next(counter))
    print(next(counter))


    # accumilator ---
    val = [22, 33, 44, 55, 99, 77, 11, 66, 33]
    acc = itertools.accumulate(val)
    print(list(acc))

    acc = itertools.accumulate(val, max)
    print(list(acc))

    # chain function
    x = itertools.chain('ABCD', '1234')
    print(list(x))

    # dropwhile and takewhile
    print("Sequence:", val)
    print("DropWhile (50)", list(itertools.dropwhile(testFunc, val)))
    print("Take While (50)", list(itertools.takewhile(testFunc, val)))

if __name__ == '__main__':
    main()