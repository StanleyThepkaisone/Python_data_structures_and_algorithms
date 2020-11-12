# Complete the function below. Given a string,
# function should return a modified string by
# rotating half of the string. Example -
# Input: Saturn
# Output: urnSat
# if the string is odd length then the extra
# Char goes to the front half in returned
# string, Example:
# Input: Neptune
# Output: tuneNep
# If the string is none than return none




def rotate_half(s):
    if s == None:
        return None
    else:
        half = int(len(s)/2)
        return s[half:] + s[:half]

if __name__ == '__main__':
    test_cases = ['Universe', 'Hello', '12345', ' ', None]
   
    for case in test_cases:
        print(rotate_half(case))