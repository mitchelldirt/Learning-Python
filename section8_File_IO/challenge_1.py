with open("C:/Users/Mitchell/Desktop/sample.txt", 'a') as tables:
    for i in range(1, 13):
        x = (i * 2)
        print("{0:>2} times 2 is {1}".format(i, x), file=tables)


