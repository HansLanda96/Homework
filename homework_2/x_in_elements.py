my_tuple = tuple(i for i in range(10, 110, 10))
x = abs(float(input("Insert any number: ")))
if x in my_tuple:
    print(my_tuple, "\nThis number exist in this list")
else:
    print(my_tuple, "\nThis number is not exist in this list")
