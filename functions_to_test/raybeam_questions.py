"""

Write a function factors which, when passed a number returns a list of all factors of that number.
For example:
factors(16) = [1,2,4,8,16]
factors(20) = [1,2,4,5,10,20]

"""
import math
from runtime import *

def find_all_factors_0(number):
    results=[]
    for x in range(1, number+1):
        if number%x == 0:
            results.append(x)
    return results

def find_all_factors_1(number):
    results=[]
    for x in range(1, int(math.sqrt(number))+1):
        if number%x == 0:
            results.append(x)
            if (number/x) not in results:
                results.append(int(number/x))

    return sorted(results)


if __name__ == "__main__":
    print(find_all_factors_1(20))
    #compare_runtime()







"""
How can you check if a tic-tac-toe board is in a winning state?

[ [ 1 ,2 3].
[4,5,6],
[7,8,9] ]

def check_win_p0(array):
    # Horizontal
    for x in array:
        if x.count(0) == 3:
            return win
    # Verticals
counter=0
    while(counter!=3):

    for x in len(array):
counter=0
        if array[x][y].count(0) == 3:
            counter+=1
"""
