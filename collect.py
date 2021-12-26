"""
Collections:
1. list: [,,,] - mutable
2. tuple: (,,,) - immutable
3. sets: {,,,} - mutable
4. dictionary: {x:y, q:w} - mutable
"""

"""
Advanced Collections:
1. namedtuple
2. OrderDict, defaultdict
3. Counter
4. deque
"""

import collections
from collections import defaultdict
from collections import Counter
from collections import OrderedDict
from collections import deque
import string

def main():

    # namedtuple ...
    ThreePoint = collections.namedtuple("ThreePoint", "x y z")
    p1 = ThreePoint(1,2,3)
    p2 = ThreePoint(3,4,4)
    print(p1, p2)
    print(p1.x, p2.y)
    p1 = p1._replace(x=100)
    print(p1)

    # defaultdict ...
    names = ['Joe', 'Bob', 'Su', 'Joe', 'Joe', 'Mark', 'Su', 'Vin', 'Mag', 'Vin']
    name_count = {}
    name_def_dict = defaultdict(int)
    name_def_dict = defaultdict(lambda: 0)

    for n in names:
        if n in name_count.keys():
            name_count[n] += 1
        else:
            name_count[n] = 1
        name_def_dict[n] += 1

    print(name_count)
    print(name_def_dict)

    names2 = ['Lu', 'Phil', 'Chris', 'Bill', 'Ed', 'Mag', 'Lu', 'Lu']

    # Counters
    c1 = Counter(names)
    c2 = Counter(names2)

    print(c1)
    print(c1['Joe'], "Joe count")
    print(sum(c1.values()), "total in names list")

    c1.update(names2) # update method
    print(sum(c1.values()), "total in names list now updated")

    print(c1.most_common(3)) # give me the three most common names in c1
    c1.subtract(names2) # subtract
    print(c1.most_common(3))

    print(c1&c2) # intersection

    # Applying OrderedDict on teams with names, wins, and loses
    teams = [('Chargers', 4, 5), ('Panthers', 5, 2), ('Rams', 8, 2), ('Bulls', 3, 5)]
    sorted_teams = sorted(teams, key=lambda t: t[1], reverse=True)
    print("Teams:", teams)
    print("Sorted Teams:", sorted_teams)

    # observe the change in the ordered list
    teams = [('Chargers', (4, 5)), ('Panthers', (5, 2)), ('Rams', (8, 2)), ('Bulls', (3, 5))]
    sorted_teams = sorted(teams, key=lambda t: t[1][0], reverse=True)
    print("Teams:", teams)
    print("Sorted Teams:", sorted_teams)
    teams = OrderedDict(sorted_teams)
    print("Ordered Teams:", teams)

    tm, wl = teams.popitem(False) # same as pop(0) in list
    print("Top team", tm, wl)
    print("Bottom team", teams.popitem(True))

    for i, t in enumerate(sorted_teams, start=1):
        print(i, t)


    a = OrderedDict({
        'a' : 1,
        'b' : 2,
        'c': 3,
    })
    b = a
    c = {
        'a' : 1,
        'c': 3,
        'b' : 2,
    }
    d = OrderedDict({
        'a' : 1,
        'c': 3,
        'b' : 2,
    })

    print("Are a and b equal?", a == b)
    print("Are a and c the same?", a == c) # when it is not Ordered, it is the same as long as the content is the same
    print("Are a and d the same?", a == d)

    # deque implementation
    d = deque(string.ascii_lowercase)
    print("Deck:", d)
    print("Count of alphabets:", len(d))
    print("First is:", d.popleft())
    print("Last is:", d.pop())
    print("Deck:", d)
    print("Now Count of alphabets:", len(d))
    d.append('z')
    d.appendleft('a')
    print("Deck:", d)
    print("Final Count of alphabets:", len(d))

    for a in d:
        print(a.upper(), end=",")
    print("\n")
    print("Deck again:", d)
    d.rotate(3)
    print("Rotated:", d)


    
if __name__ == '__main__':
    main()