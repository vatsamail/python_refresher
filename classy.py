
from enum import Enum, unique, auto

# make sure keys are always unique
@unique # ensures even the values are unique
class User(Enum):
    Joe = 1
    Bob = 2
    Su = 3
    Mark = 4
    Jack = auto()

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y) # used as : p1 + p2

    # note that function overload based on the type is not posible with python as the datatype is unknown while interpretting .. :-/
    # def __iadd__(self, other):
    #     self.x += other
    #     self.y += other # used for p1 += 2
    #     return self

    def __iadd__(self, other):
        self.x += other.x # used for p1 += p2
        self.y += other.y
        return self

    def __ge__(self, other):
        if self.x >= other.x and self.y >= other.y:
            return True
        return False
    
    def __le__(self, other):
        if self.x <= other.x and self.y <= other.y:
            return True
        return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        if self.x != other.x or self.y != other.y:
            return True
        return False    

    def __str__(self):
        return str(self.x) +','+ str(self.y)



class Person():
    def __init__(self):
        self.f = "Vatsa"
        self.l = "Prahallada"
        self.e = "vatsamail@gmail.com"
     
    # you cannot do this.
    # the better approach is to use @classmethod
    # def __init__(self, f, l, e, w):
    #     self.f = f
    #     self.l = l
    #     self.e = e
    #     self.w = w


    def __getattr__(self, attr):
        if attr == 'fullname':
            return (self.f, self.l)
        elif attr == 'info':
            return {
                'first_name': self.f,
                'last_name': self.l,
                'email_id': self.e,
            }
        else:
            raise AttributeError

    def __setattr__(self, attr, val):
        if attr == 'info':
            self.f = val[0]
            self.l = val[1]
            self.e = val[2]
        elif attr == '':
            self.f = val[0]
            self.l = val[1]
        else:
            super().__setattr__(attr, val) # always call super of __setattr__

    # make sure you write the __str__ at the last. Else it will affect the __getattr__
    def __str__(self):
        return self.f+" "+self.l #p1, str(p1), format function
    
    def __repr__(self):
        return "<Person Class - fname: {0}, lname: {1}, email: {2}>".format(self.f, self.l, self.e) # affects repr

    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.f, self.l, self.e)
        return val.encode('utf-8') # affects bytes

    def __dir__(self):
        v = super().__dir__() # can str(v) in the return as well
        return('f', 'l', 'e', 'info', 'fullname')

    
    
        


def main():
    print(User.Joe)
    print(type(User.Joe))
    print(repr(User.Joe))
    print(User.Joe.name, User.Joe.value)
    print(User)
    print(User.Jack.value) # auto in function

    people = {}
    people[User.Bob] = "He is a manager"
    print(people[User.Bob])

    p1 = Person()
    print("Person:", p1)
    print(repr(p1))
    print(str(p1))
    print("Formatted: {0}".format(p1))
    print(bytes(p1))

    print("Fullname:", p1.fullname)
    print("Full info:", p1.info)
    p1.info = ('Whatson', 'Prahayada', 'whatsonp@blahmail.com')
    print("Full info now:", repr(p1))
    print("Calling dir", dir(p1))

    p1 = Point(1,2)
    p2 = Point(3,4)
    print("when {} + {} = {}".format(p1, p2, p1+p2))
    # p1 += 1
    # print("New p1:", p1)
    
    p1 += p2
    print("Added p1 and p2: ", p1)

    print("Is p1 {} is >= p2 {}? {}".format(p1, p2, p1 >= p2))
    print("Is p1 {} is not equal to p2 {}? {}".format(p1, p2, p1 != p2))

if __name__ == '__main__':
    main()