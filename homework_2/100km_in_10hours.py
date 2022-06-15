length_of_road = 99
speed = int(input("Insert speed of Vasil (Km/h): "))
time = int(input("Insert how much time Vasil rides(hours): "))
position_on_road = (speed * time % length_of_road)
print("Vasil will stop on:", position_on_road, "km of road")
