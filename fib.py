# Fibonnacci sequence
# dynamic programming
#  - recursion + caching
#  - overlapping sub problems

def fib(n):
    memo = [0]*(n+1)
    memo [0] = 0
    memo [1] = 1
    return fib_dp(n, memo)

# makes function this o(n) time complexity but adds o(n) spacce for the caching
# this is also a top down approach > memoization = caching the smaller functions so we dont have to compute it again.
def fib_dp(n, memo):
    if n==0 or n==1:
        return n

    if memo[n] == 0:
        memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]

# interative approach
def fib_iterative(n):
    iter_memo = [0] * (n+1)
    iter_memo [0] = 0
    iter_memo [1] = 1

    for x in range (2, n+1):
        iter_memo[x] = iter_memo[x-1] + iter_memo[x-2]

    return iter_memo[n]


print(fib(5))
print(fib(8))
print(fib_iterative(5))
print(fib_iterative(8))