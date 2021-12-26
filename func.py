import os
import sys
import collections

def opAll(operator, *numbers):
    """opAll(op, numbers) --> Based on the first arg operator, the function applies to the given set of numbers.

    Parameters:
    op: Operator: + or - or * or /
    numbers: Any length of numbers

    Returns:
     A floating point number
    """
    numbers = list(numbers)
    res = numbers.pop(0)
    if operator == '+':
        for n in numbers:
            res = res + n

    
    elif operator == '*':
        for n in numbers:
            res = res * n

    elif operator == '-':
        for n in numbers:
            res = res - n

    elif operator == '/':
        for n in numbers:
            res = res / n

    else:
        print('Operator', operator, 'is not applicable on the numbers')
    return res


def keywordFunc(arg1, arg2, *, status=False):
    if status:
        print("You are good", arg1, arg2)
    else:
        print("Something went wrong", arg1, arg2)


def helloFunc(a,b=None):
    """helloFunc(Name, Statement) --> It just wishes 'hello' to the given name and adds the following statement.

    Parameters: 
    Name: Any name that needs to be printed
    Statement: Any statement. But can be nothing too. Defaults to None
    """
    print("Hello {}! {}".format(a, b))


def c2F(x):
    return (x * 9/5) + 32

def f2C(x):
    return (x-32) * 5/9

def main():
    """main(void) --> A quick Summary

    Parameters:
    <write parameters>

    Returns:
    <write outputs of the function>
    """
    print("Documentations:")
    print("map built-in:", map.__doc__)

    print("Collection modules:", collections.__doc__)
    helloFunc('vatsa', "What's up?")
    print(helloFunc.__doc__)
    print(main.__doc__)

    print(opAll.__doc__)
    print(opAll('+', 1, 2, 3, 4))
    print(opAll('*', 1, 2, 3, 4))
    print(opAll('-', 1, 2, 3, 4))
    print(opAll('/', 1, 2, 3, 4))
    print(opAll('^', 1, 2, 3, 4))

    nums = [1,2,3,4]
    v = opAll('+', *nums)
    print("Total:", v)

    # lamda function (inline function)
    ctemp = [0, 12, 34, 100]
    ftemp = [32, 0, 65, 100, 72]
    print("In C:", list(map(f2C, ftemp)))
    print("In F:", list(map(c2F, ctemp)))

    print("In C with lambda:", list(map(lambda x: (x-32) * 5/9, ftemp)))
    print("In F with lambda:", list(map(lambda x: (x * 9/5) + 32, ctemp)))

    # use of keyword only functions
    keywordFunc(1, 2, status=True)
    

if __name__ == '__main__':
    main()