#Write program to print set of duplicates in a list
def print_dup(x):
    x = list(x)
    l = []
    for i in range(0,len(x)):
        if x.count(x[i]) > 1:
            l.append(x[i])
    print(set(l))

if __name__ == '__main__':
    print_dup([1, 2, 3, 4, 4, 5, 5, 6, 7])

