#Write a function to check whether is a string is Palindrome or not (abc = cba)
def Palindrome(x):
    if all(x[i] == x[-(i+1)] for i in range(0, len(x))):
        return print("This value is Palindrome")
    else:
        return print("This value is not Palindrome")

if __name__ == '__main__':
    x = "ASSA"
    Palindrome(x)






