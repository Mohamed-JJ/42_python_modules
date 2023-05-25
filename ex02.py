import sys

if len(sys.argv) > 2:
    print("Assertation Error: more than one argument are provided")
    exit(1)
number = sys.argv[1]
if not number.isdigit():
    print("Assertation Error: argument is not an integer")
    exit(1)
if (int(number) == 0):
    print("I'm zero")
elif (int(number) % 2 == 0):
    print("I'm even")
else:
    print("I'm odd")