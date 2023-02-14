def palindrome(s):
    t=s[::-1]
    if s==t:
        print("is a palindrome")
    else:
        print("is not a Palindrome")
v=str(input())
palindrome(v)