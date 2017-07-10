"""语句"""

NUM = 0
while NUM < 5:
    print(NUM, "< 5")
    NUM += 1
else:
    print(NUM, ">= 5")

print("-----")

for i in range(5):
    print("i =", i)

print("-----")
SEQUENCE = [11, 22, 33]
for i, j in enumerate(SEQUENCE):
    print(i, "=", j)
