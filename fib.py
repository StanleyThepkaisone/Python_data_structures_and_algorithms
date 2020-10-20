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

print(fib(5))
print(fib(8))