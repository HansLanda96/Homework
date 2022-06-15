first_distance = int(input("Insert first run distance: "))
second_distance = int(input("Insert second run distance: "))
day = 1
while first_distance < second_distance:
    day += 1
    first_distance *= 1.1
print("Runner will run", second_distance, "km", "on", day, "day")
