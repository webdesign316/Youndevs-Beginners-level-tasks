#Beginner level task2
def isPalindrome(s):
    return s == s[::-1]
str1 = input ("Enter a string.")
ans = isPalindrome(str1)
if ans:
    print("Yes")
else:
    print("No")

