year = int(input("Insert any year: "))
if year % 400 == 0:
    print("YES")
elif year % 100 == 0:
    print("YES")
elif year % 4 == 0:
    print("YES")
else:
    print("NO")

# also we can do same thing with less "elif" construction
year2 = int(input("Insert any year(2): "))
if year2 % 400 == 0 or year2 % 100 == 0 or year2 % 4 == 0:
    print("YES")
else:
    print("NO")
