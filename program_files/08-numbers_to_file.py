import matplotlib.pyplot as plt
import random

# integer_str = ''
#
# file = open('../files/numbers.txt', 'w')
# for integer in range(500):
#     integer_str += str(random.randint(1, integer + 1)) + " "
# file.write(integer_str)
# file.close()
#
# file = open('../files/numbers.txt')
# data = file.read().split()
# file.close()
#
# integers = []
# for num in data:
#     integers.append(int(num))
#
# plt.plot(integers)
# plt.show()

file = open('../files/numbers.txt', 'w')

for integer in range(500):
    file.write(str(random.randint(integer, 500)) + "\n")
file.close()

file = open('../files/numbers.txt', 'r')
data = []
for integer in file.readlines():
    data.append(int(integer.strip()))
print(data[:5])

file.close()
plt.plot(data)
plt.show()









