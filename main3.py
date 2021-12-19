#Write sort function without using built in sort function
def sort_list(x):
    l = []
    k = list(x)
    for j in range(0, len(k)):
        for i in k:
            if i == max(k):
                l.append(i)
                k.remove(i)
    print(l)

if __name__ == '__main__':
    sort_list(['A', 'Y', 'Z', 'M', 'B'])


'''
while data_list:
    min = data_list[0]
    for x in data_list:
        if x > min:
            min = x
    new_list.append(min)
    data_list.remove(min)
'''


