
# how many ways can you travers an array to number n, assuming you can only take 1, 2, 3 steps at a time.
# when done manually we can see a pattern to find the amount of ways n, is equal to (n-1) + (n-2) + (n-3)
# the max to get to [1] is 1; [2] is 2; [3] is 4; [4] is 7. you can see if n = 4, you can sum the previous 3 steps.


# Brute force --> big(O) = 3^n
def num_of_ways_bf(n):
    if n == 1 : return n
    if n == 2 : return 2
    if n == 3 : return 4
    return num_of_ways(n-1) + num_of_ways(n-2) + num_of_ways(n-3)

# what you should do is create a function num_of_ways_dp and call that from another functions
# Dynamic Programming - top down
# Big(0) = o(n) since we are using a linear function

def num_of_ways(n):
    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    return num_of_ways_dp_top_down(n, arr)

def num_of_ways_dp_top_down(n, arr):

    if arr[n] == 0:
        arr[n] = num_of_ways_dp_top_down(n-1, arr) + num_of_ways_dp_top_down(n-2, arr) + num_of_ways_dp_top_down(n-3, arr)

    return arr[n]

# dp with bottom up approach - iterative
def num_of_ways_dp_bottom_up(n):
    arr = [0] * (n+1)
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4

    for x in range(4, n+1):
        arr[x] = arr [x-1] + arr[x-2] + arr[x-3]

    return arr[n]


print(num_of_ways_dp_bottom_up(8))