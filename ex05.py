kata = (19, 42, 24)

kata1 = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

kata3 = (2019, 9, 25, 3, 30)

print("the 3 numbers are: " + " ,".join(str(i) for i in kata))

for i in kata1:
    print(i + " was created by " + kata1[i])

print("{:02d}/{:02d}/{:04d} {:02d}:{:02d}".format(kata3[3], kata3[4], kata3[2], kata3[0], kata3[1]))