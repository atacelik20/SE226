x=int(input("Please enter a number between 1 and 100"))
while x<10 or x>100:
    print("Invalid number")
    x = int(input("Please enter a number between 1 and 100"))
fizz=0
buzz=0
fizzBuzz=0

for y in range(1, x+1):
    if y%7==0:
        continue
    if y%3==0 and y%5==0:
        print("FizzBuzz")
        fizzBuzz=fizzBuzz+1
    elif y%3==0:
        print("Fizz")
        fizz=fizz+1
    elif y%5==0:
        print("Buzz")
        buzz=buzz+1
    else:
        print(y)
print("--- Summary ---")
print("Fizz Count: " , fizz)
print("Buzz Count: " , buzz)
print("FizzBuzz Count: " , fizzBuzz)

