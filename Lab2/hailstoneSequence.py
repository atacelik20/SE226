x = int(input("Please enter a positive integer greater than 1."))
step = 0
while x > 1:
    print(x,end=" ")
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            print("->", x, end=" ")
            step = step + 1

        else:
            x = 3 * x + 1
            print("->", x,end=" ")
            step = step + 1

print("Total Steps: ", step)
