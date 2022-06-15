import random

inputs = 0
rand_num = random.randint(1, 10)
while inputs < 3:
    number = int(input("Insert any number from 1 to 10: "))
    inputs += 1
    if inputs == 3:
        print("Random number was:", rand_num, "\nYou are looser(devillaugh)!!!")
        break
    if number == rand_num:
        print("Random number was:", rand_num, "\nYou win this time(machine is crying)")
        break
    elif number > rand_num:
        inputs += 1
        print("Attempts left:", 3 - inputs, "\nYou can do better homie...try again", )
    elif number < rand_num:
        print("Attempts left:", 3 - inputs, "\nOoops, incorrect...try one more time")
else:
    pass
