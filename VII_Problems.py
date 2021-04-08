import timeit
from collections import defaultdict
import json
#from tqdm import tqdm

# Bottlenecks
"""
Example: Given an array of distinct integer values,
count the number of pairs of integers that have difference k.
For example, given the array { 1,  7,  5,  9,  2,  12,  3} and
the difference k =  2,thereare four pairs with difference 2:
(1,  3),  (3,  5),  (5,  7),  (7, 9).

"""
# bruteforce
# check each number with every subsequent number
# loop across full list but check a spliced version of the list w/ enumerate
# so it's slightly better than checking every number against every numbe
# runtime: n * (n-1) * (n-2)... 1, looks like O(n2)

l=[1,  7,  5,  9,  2,  12,  3]
k=2
def diff_bruteforce(l, k):
    pairs=[]
    for n, x in enumerate(l):
        for y in l[n:]:
            if abs(x-y)==k:
                pairs.append((x,y))

    return pairs

# first time through, didn't read carefully!
# we're counting the number of pairs, so we should return 4.
# I'll use a defaultdict (hashtable) to do it efficiently
# count the number of x+-y==K for each x
# then find sum of values
# runtime: O(n), just passes through list once!
def diff_hash(l, k):
    dd=defaultdict(int)
    for n,x in enumerate(l):
        # checks to see if the pair already exists as well
        if (x+k in l and dd[x+k]==0):
            dd[x]+=1
        if (x-k in l and dd[x-k]==0):
            dd[x]+=1
    print(dd)

    return sum(dd.values())



"""
Example: Print all positive integer solutions to the equation a3 + b3 = c3 +d3
where a, b, c, and d are integers between 1 and 1000.
"""
# brutforce first
# the classic quadruple for loop
# should be right though...
# update: yikes

n=range(1,1000)
def findNums_bruteforce():
    solutions=[]
    for a in tqdm(n):
        for b in n:
            for c in n:
                for d in n:
                    if (a^3 + b^3) == (c^3 + d^3):
                        solutions.append((a,b,c,d))
    return solutions


# okay... optimizations!
# something something hashtables
# calculate pairs first and then compare pairs w/ O(1) lookups
# 2 sets of pairs, should be O(n2) now
# update: finished quickly but... its just the same shit on both sides...
# update 2: after removing duplicates there seems to be a lot of cool pairs as well.
n=range(1,100)
def findNums_hashtables():
    dict_ab={}
    for a in n:
        for b in n:
            dict_ab[(a,b)]=(a**3+b**3)
    dict_cd={}
    for c in n:
        for d in n:
            dict_cd[(c,d)]=(c**3+d**3)

    ans=[]
    for ab in dict_ab.keys():
        for cd in dict_cd.keys():
            if dict_ab.get(ab) == dict_cd.get(cd):
                ans.append([ab, cd])
    return ans

def write_to_file(ls):
    with open("file.txt", "w") as fp:
        json.dump(ls, fp)

def open_and_check():
    with open("file.txt", "r") as fp:
        b = json.load(fp)

    new=[]
    for x in b:
        if (x[0][0] not in x[1]) and (x[0][1] not in x[1]):
            new.append(x)
    for x in new:
        print(new)



"""
 Given a smaller string S and a bigger string B, design an algorithm
 to find all permuta­tions of the shorter string within the longer one.
 Print the location of each permutation.
"""
# first try, I think this is good: O(n)
# correction: since you're also looping through s,
# it would be O(S*B) in an example where s is much larger.
# should be writing a function that applies to multiples cases anyways
def string_1():
    s='abc'
    b='aabbcabcddcabc'
    list_b=list(b)
    ans=[]
    try:
        for x in range(len(list_b)):
            one,two,three=list_b[x],list_b[x+1],list_b[x+2]
            group=[one,two,three]
            if s[0] in group and s[1] in group and s[2] in group:
                ans.append(['Index: {index}'.format(index=x),[one,two,three]])
    except IndexError:
        return ans

# O(S*B) isn't bad
# can optimize further by skipping if encountered
# char isn't in s

def string_2(s,b):
    bList=list(b)
    ans=[]
    try:
        for x in range(len(b)):
            group=[]
            ugh=True
            for y in range(len(s)):
                if bList[x+y] not in s:
                    ugh=False
                    break
                else:
                    group.append(bList[x+y])
            if ugh==True:
                ans.append([x, group])

    except IndexError:
        return ans


if __name__ == "__main__":
    ans = diff_bruteforce(l, k)
    print(ans)
    # ans=diff_hash(l, k)
    # print(ans)

    #ans=findNums_hashtables()
    #print(ans)
    #write_to_file(ans)
    #open_and_check()

    # s='abc'
    # b='aabbcabcddcabc'
    # ans=string_2(s,b)
    # print(ans)
