#course:cmps3500
#lab3
#date: 2/18/20
#username:mmercado
#name:Ma Mikaela Mercado
#description: PART A: Good and Bad Game
import numpy as np
import random
res2=[]
string1 = random.randint(1000,9999)
res=[int(x)for x in str(string1)]
print("Welcome to the Good and Bad Game!")

while res != res2:
    string2 = input("Enter a number: ")
    res2=[int(j) for j in str(string2)]
    good = 0
    bad = 4
    if len(res) == len(res2):
        for i in range(len(res)):
            if res[i]==res2[i]:
                good=good+1
    bad=bad-good
    print("Good: ", good, "Bad: ", bad)
