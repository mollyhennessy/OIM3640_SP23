# savings calcuator
import time

print("We are offering a special CD")
print("Tell me how much you will deposit and I will")
print("calculate it's value")

RATE = 0.015
YEARS = 5
initial_deposit = float(input("How much you got?\n"))

print("Here are your balances each year")
print(f"{'Year':<10}{'Balance':>10}") # center = ^
print("-" * 20)


for year in range(YEARS):
    initial_deposit = initial_deposit * (1 + RATE)
    output = f"${initial_deposit:,.2f}"
    print(f"{year + 1:<10d}{output:>10}")