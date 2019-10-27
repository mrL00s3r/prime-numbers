# this is a program that will find prime numbers forever
# mr_L00s3r
# oct. 26 2019
# TODO: make it infinitly, without the user interaction.

num  = int(input('Write  the number and find how many prime numbers exist between 0 and your number: '))
def infinite(i):
    if i > 1:
        for j in range(2, i//2):
            if (i % j) == 0:
                print('\n')
            else:
                print(i, ' PRIME NUMBER')
while True:
    for i in range(0, num):
        i = i+1
        infinite(i)

