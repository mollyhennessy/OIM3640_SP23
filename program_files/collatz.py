# collatz
steps = 0
print("Enter a positive integer: ")
number = int(input())

while number > 1:
    if number % 2:
        number = number * 3 + 1
        print(number)
    else:
        number //= 2
        print(number)
    steps += 1
print()
print(f"That took {steps} steps to get to 1")