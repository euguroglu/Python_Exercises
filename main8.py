#Write a program to print number of words in a given sentence
def count_words(x) -> int:
    a = 0;
    for i in range(0, len(x)):
        if x[i] == ' ':
            a += 1
    print(a+1)

if __name__ == '__main__':
    count_words("This is a computer")
    count_words("There are 7 words in this sentence")

#Alternative is just use split function: print(len(sentence.split()))