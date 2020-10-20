# find the maximum sum of the subarrays
# if we brute force we get O(n)^3 since we have to make multiple subarrays then sum the values.

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def max_subarray_sum(arr):
    local_max = [0] * len(arr)
    local_max[0] = arr [0]

    for x in range (1, len(arr)):
        local_max[x] = max(arr[x], arr[x] + local_max[x-1])
    return max(local_max)


print("max sum in the array: ", max_subarray_sum(arr))