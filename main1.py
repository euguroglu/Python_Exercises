#Print prime numbers between 100 and 200
def prime_between_100_200() -> int:
    for i in range(100, 200):
        if all(i%j !=0 for j in range(2, i)):
            print(i)

if __name__ == '__main__':
    prime_between_100_200()
