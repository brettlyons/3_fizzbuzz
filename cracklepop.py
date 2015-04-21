#/usr/bin/python
# CracklePop (aka FizzBuzz)
# Specification:  Prints the numbers 1 through 100 with three notable exceptions
#     if the number is divisbile by 3, Crackle is printed, if the number is
#     divisible by 5, Pop is printed, and if the number is divisible by both,
#     15 is printed.
# python3 syntax
for i in range(1, 101):
    if(i % 3 == 0 and i % 5 == 0):
        print("CracklePop")
    elif(i % 5 == 0):
        print("Pop")
    elif (i % 3 == 0):
        print("Crackle")
    else:
        print(i)
