import sys
if len(sys.argv) != 3:
    print("ERROR")
    exit(1)
for i in sys.argv[1:]:
    for h in i:
        if h.isalpha():
            print("ERROR")
            exit(1)

print("Sum = " + str(int(sys.argv[1]) + int(sys.argv[2])))
print("product = " + str(int(sys.argv[1]) * int(sys.argv[2])))
print("division = " + str(float(int(sys.argv[1]) / int(sys.argv[2]))))
print("remainder = " + str(int(sys.argv[1]) % int(sys.argv[2])))
print("difference = " + str(int(sys.argv[1]) - int(sys.argv[2])))