"""
Coding style:
pep8 - python enhancement proposals - 8.
* imports are always at the top and each in a line
* limit 72 characters for the code and comment
* Functions and classes seperated by 2 lines
* dont align the equals like ab  = 3 and abc = 4

"""

import sys
import os
from string import Template

gvar = "GV"
class Sample():
    cvar = "CV"
    def __init__(self):
        self.ovar = "OV"

    def _setOvar(self, val):
        self.ovar = val
    
    def getOvar(self):
        return self.ovar

    def fullPrint(self):
        return "Global variable: "+gvar+", Class variable: "+Sample.cvar+", Object variable: "+ self.ovar

    
class StringBytes():
    def __init__(self):
        self.b = bytes()
        self.s = ''

    def __init__(self, bites, statements):
        self.b = bites
        self.s = statements

# main function 
def main():
    s1 = Sample()
    s2 = Sample()

    print(s1.fullPrint(), s2.fullPrint())
    s1._setOvar("I have changed")
    Sample.cvar = "boom"
    print(s1.fullPrint(), s2.fullPrint())
    
    
    sb = StringBytes(bytes([0x41, 0x42, 0x43]), "The first three are: ")
    print(sb.b)
    print(sb.s)
    print("string:", sb.s + ' ' + sb.b.decode('utf-8'))
    print("bytes 8:", sb.s.encode('utf-8'))
    print("bytes 32:", sb.s.encode('utf-32'))

    t = "I am a template where I get one value {0} and also another value {1}".format("as one", "as two")
    tpl = Template("Checking the code: ${code_name} by ${developer}")

    print(t)
    print(tpl.substitute(code_name="lang.py", developer="vatsa")) # template substitution

    data = {
        'code_name' : 'hello world',
        'developer' : 'charles babagge',
    }

    print(tpl.substitute(data))

# -------------------------------------------
if __name__ == '__main__':
    main()