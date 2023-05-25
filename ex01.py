import sys
line = " ".join(sys.argv[1:][::-1])
arr = line.split(" ")
for i in range(0, len(arr)):
	arr[i] = arr[i].swapcase()
for i in range(0, len(arr)):
	if i == len(arr) - 1:
		print(arr[i][::-1], end = "\n")
	else:
		print(arr[i][::-1], end = " ")
