def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("abba"))
print(not is_palindrome("abab"))
print(is_palindrome("tenet"))
print(not is_palindrome("banana"))
print(is_palindrome("straw warts"))
print(is_palindrome("a"))
