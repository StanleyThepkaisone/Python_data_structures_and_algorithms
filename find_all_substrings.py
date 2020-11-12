# Find all Substrings
# Complete the definition of the following funtion to compute all
# that can be formed from a given string.
# Example :  For a string s = 'Hello', all the substrings within it are:
# ['H', 'He', 'Hel', 'Hell', 'Hello', 'e', 'el', 'ell', 'ello', 'l', 'll', 'llo', ,'l', 'lo', 'o']


def find_all_substring(s):
    index0 = 0
    index1 = 1
    subStrings = []

    if not s :
        return []
    else:
        while index0 < len(s):
            while index1 <= len(s):
                subStrings.append(s[index0:index1])
                index1 += 1
            index0 += 1
            index1 = index0 + 1
    return subStrings

if __name__== '__main__':
    test_cases = ['Universe', 'Hello', '12345', '', None]
    for case in test_cases:
        print(case, ' -->', find_all_substring(case),  '\n')