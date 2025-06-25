def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

num = input("Enter a word or number: ")
print(is_palindrome(num))





