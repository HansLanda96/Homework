first_horiz_cell = int(input("Insert first horizontal cell of chess desk(1-8): "))
first_verti_cell = int(input("Insert first vertical cell of chess desk(1-8): "))
sec_horiz_cell = int(input("Insert second horizontal of chess desk(1-8): "))
sec_verti_cell = int(input("Insert second vertical of chess desk(1-8): "))

horiz_position = abs(first_horiz_cell - sec_horiz_cell)
verti_position = abs(first_verti_cell - sec_verti_cell)

if horiz_position == 1 and verti_position == 2:
    print("Move of knight is acceptable")
elif horiz_position == 2 and verti_position == 1:
    print("Move of knight is acceptable")
else:
    print("Move of knight is unacceptable")

# also we can write "if" in one line, but i think use of one "elif" is not a crime:D
# if horiz_position == 1 and verti_position == 2 or horiz_position == 2 and verti_position == 1
