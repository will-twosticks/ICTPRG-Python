# question 1
for x in range(0,26):
    print(x)
    x += 1

# question 2
sum = 0
for x in range(10,51):
    sum += x
    print(sum)

# question 3
while True:
    number = int(input("what is the number? "))
    if (number >= 50) and (number <= 70):
        print("within range")
        break
else:
    print("not within range")

# question 4
for x in range(0,26):
    print(x, end =", ")
    x += 1

# question 5
total = 0
number = 0
while number != "x":
    number = input("what is the number? ")
    if str(number) == "x":
        print("total: " + str(total))
    else:
        total = total + int(number)

# question 6
for collumn in range(0,5):
    for row in range(0,5):
        print("x", end='')
    print("")