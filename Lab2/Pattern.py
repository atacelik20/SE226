x=int(input("Please enter a number between 3 and 9"))
while (x<3 or x>9):
    x=int(input("Please enter a number between 3 and 9"))
for y in range(1, 2*x):
    z=x - abs(x-y)
    print("*" * z)