# reaction time tester
import random
from time import sleep, time

print("Welcome to the reaction time tester")
print("You will have 5 tries to test your speed")

total_time = 0

for attempt in range(1,6):
    wait = random.random() * 5 # random.uniform(0,5)
    print(f"Get ready for try {attempt}")
    sleep(wait)
    start = time()
    input("Quick hit the enter key!")

    react_time = time() - start
    total_time += react_time
    print(f"Wow that was fast. It took you {react_time:.3f} seconds to hit enter!")

print("-" * 30)
print(f"Your average reaction time was {total_time / attempt:.3f}")




