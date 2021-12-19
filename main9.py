#Write program which takes two strings as input from the user
#Giving 2 outputs, output1 takes all character which is not present output2
#But present in output 1 , output2 is vice versa.

def character_finder(x, y) -> str:
    l = ''
    m = ''
    for i in range(0, len(x)):
        if all(x[i] != y[j] for j in range(0, len(y))):
            l = l + x[i]
    for i in range(0, len(y)):
        if all(y[i] != x[j] for j in range(0, len(x))):
            m = m + y[i]

    print("Output 1:{}".format(l))
    print("Output 2:{}".format(m))

if __name__ == '__main__':
    character_finder("enes", "sertac")

'''
Alternative solution:

def character_finder(x, y) -> str:
    l = ''
    m = ''
    for i in x:
        if i not in y:
            l = l + i
    for i in y:
        if i not in x:
            m = m + i
    return l,m
'''