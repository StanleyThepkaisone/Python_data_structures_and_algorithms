# Palindrome
# write a method name is_palindrome which acceptrs a string input.
# function will return True if string is a palindrome else it will
# return false
# write test cases to test it out.

def is_palindrome(s):
    if not s:
        return 'Empty String'
    if s.lower() == s[::-1].lower():
        return True
    else:
        return False
    return

if __name__ == '__main__':
    test_cases = ['Kayak', '12345', 'abcd', 'asddsa', '']

    for case in test_cases:
        print(case, end = " -> ")
        print(is_palindrome(case))