import random

while True:
    n = input("Level: ")
    n = int(n)
    if n > 1:
        break
z = int(input("Guess: "))
y = random.randint(1, n)
if z == y:
    print("Just right!")
elif z > y:
    print("Too large")
else:
    print("Too small")

print(y)
