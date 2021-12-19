#Write function to print fibonacci series
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n-1) + F(n-2)

if __name__ == '__main__':
    for i in range(0, 12):
        print(F(i))

