#this is already O(n)
def recursive_factorial(n):
    if n<=1:
        return n
    return recursive_factorial(n-1)*(n)


# we're trying to find the nth fibonaci number

# how'd I do it in 30 sec?
def mine_fib(n):
    fib=[1,1]
    for x in range(0, n-2):
        fib.append(sum(fib[-2:]))
    return fib[-1]

# I believe thats O(n)?

# this shit is O(2^n)
def recursive_fib(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


# already did it in mine
def memoization_fib(n):
    return

# logn version?
# idk some matrix determinant shit

# Python3 Program to find n'th fibonacci Number in
# with O(Log n) arithmatic operations
MAX = 1000

# Create an array for memoization
f = [0] * MAX

# Returns n'th fuibonacci number using table f[]
def fib(n) :
    # Base cases
    if (n == 0) :
        return 0
    if (n == 1 or n == 2) :
        f[n] = 1
        return (f[n])

    # If fib(n) is already computed
    if (f[n]) :
        return f[n]

    if( n & 1) :
        k = (n + 1) // 2
    else :
        k = n // 2

    # Applying above formula [Note value n&1 is 1
    # if n is odd, else 0.
    if((n & 1) ) :
        f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1))
    else :
        f[n] = (2*fib(k-1) + fib(k))*fib(k)

    return f[n]



if __name__=="__main__":
    print(mine_fib(9))
    print(recursive_fib(9))
    print(fib(9))
