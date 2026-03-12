# for loop
# loop through list
primes = [2, 3, 5, 7]
for x in primes:
    print(x)

# loop round range(start, stop)
# ps. will stop before number
for i in range(5):
    print(i)

# while loop
count = 0
while count < 5:
    print(count)
    count += 1

# loop (break & continue)
# break
for x in range(10):
    if x == 3:
        break
    print(x)

# continue
for x in range(5):
    if x % 2 == 0:
        continue
    print(x)

# exercise
numbers = [951, 402, 984, 651, 360, 69, 408,319, 601, 485]

for x in numbers:
    # if found 237 will stop
    if x == 237:
        break

    # if even number will skip
    if x % 2 == 0:
        continue

    # print remaining numbers
    print(x)