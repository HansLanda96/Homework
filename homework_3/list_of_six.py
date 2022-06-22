list_of_six = [i for i in range(100, 197, 6)]
for num in list_of_six:
    if num % 5 == 0 and num < 150:
        print(num)

