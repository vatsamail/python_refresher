
def main():
    in_fahrenheit = [32, 0, 100, 70, 80, 160]
    in_celius = [(t-32) * 5/9 for t in in_fahrenheit] # comprehension style
    for t in zip(in_fahrenheit, in_celius):
        print("{}F in Celius is: {:.2f}C".format(t[0], t[1])) # formatted string

    evens = [2, 4, 6, 8, 10, 12]
    odds = [1, 3, 5, 7, 9, 11, 13]
    primes = [1, 2, 3, 5, 7, 11, 13, 17]

    even_sq = list(
        map(
            lambda e: e **2, 
            filter(lambda e: e>4 and e<12, evens) # print only even numbers that are gt 4 and lt 12
            )
        )
    print("Even Squares:", even_sq)

    # lets do the same with comprehension
    even_sq = [e ** 2 for e in evens]
    print("Comprehension even squares:", even_sq)

    # comprehension with predicate
    odd_sq = [o ** 2 for o in odds if o > 3 and o < 11]
    print("Comprehension with predicates:", odd_sq)


    #----------------------------------
    # dictionary comprehension
    #----------------------------------
    in_celius = [0, 10, 25, 20, 18, 40, 50, 100]
    temp_dict = {t: (t*9/5)+32 for t in in_celius if t < 100} # {key: value}
    print("Temp (Celius to Fahrenheit)", temp_dict)


    team1 = {
        'Bob': 24,
        'Joe': 23
    }
    team2 = {
        'Su': 19,
        'Lu' : 25
    }

    new_team = { k:v for team in (team1, team2) for k,v in team.items()} # complicated but once learnt it is fine.
    print("Merged teams:", new_team)

    #----------------------------------
    # sets comprehension
    #----------------------------------

    # set - all values are unique within the set
    in_celius = [0, 10, 25, 20, 18, 40, 50, 100, 0, 10, 25, 20, 18, 40, 50, 100] # you can see the duplicates in the list
    in_fahrenheit = {(t*9/5) + 32 for t in in_celius}
    dict_f = {t:(t*9/5) + 32 for t in in_celius}
    print("Unique Fahrenheit:", in_fahrenheit)
    print("Fahrenheit Dictionary:", dict_f)

    some_string = "once upon a time there was a prince who lived in a small hut"
    chars = {x.upper() for x in some_string if not x.isspace()}
    dict_chars = {x: x.upper() for x in some_string if not x.isspace()}
    print("Unique chars:", chars, "in a string:", some_string)
    print("Unq chars in the form of dictionary:", dict_chars)



if __name__ == "__main__":
    main()