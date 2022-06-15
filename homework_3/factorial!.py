number = int(input("Insert any number: "))
factorial = 1

for q in range(2, number + 1):
    factorial *= q
print("Factorial of number", number, "equals", factorial)
