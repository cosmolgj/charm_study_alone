
for i in range(4, 0 -1, -1):
    print(i)

#===========================
print("===================")
for i in reversed(range(5)):
    print(i)

print("===================")
import time

number = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1

print("repeated {} times during 5 seconds".format(number))


#===========================
print("===================")
numbers = [5, 15, 6, 20, 7, 25]

for number_ in numbers:
    if number_ < 10:
        continue
    print(number_)
