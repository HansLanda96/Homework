number = float(input("Insert any float number: "))
num_in_str = str(number).split(".")[1]
print("Decimal part equals", num_in_str,
      "\nFirst number of decimal part equals", num_in_str[0])
