def right_triangle_area():
    first_leg = float(input("\nInsert first leg of triangle (cm): "))
    second_leg = float(input("Insert second leg of triangle (cm): "))
    return round(first_leg * second_leg / 2, 2)


def rhombus_area():
    f_diagonal = float(input("\nInsert first diagonal of rhombus (cm): "))
    s_diagonal = float(input("Insert second diagonal of rhombus (cm): "))
    return round(f_diagonal * s_diagonal / 2, 2)


def square_area():
    side = float(input("\nInsert one side of square (cm): "))
    return round(side ** 2, 2)


def circle_area():
    radius = float(input("\nInsert radius of circle (cm): "))
    return round(radius ** 2 * 3.14, 2)


def rectangle_area():
    length = float(input("\nInsert length of rectangle (cm): "))
    width = float(input("Insert width of rectangle (cm): "))
    return round(length * width, 2)


def parallelogram_area():
    base = float(input("\nInsert base of parallelogram (cm): "))
    height = float(input("Insert height of parallelogram (cm): "))
    return round(base * height, 2)


def main():
    print("Right Triangle = 1 \t Rhombus = 2"
          "\nSquare = 3 \t\t\t Circle = 4"
          "\nRectangle = 5 \t\t Parallelogram = 6")
    figure = int(input("\nArea of which figure you want to know: "))
    if figure > 6 or figure < 0:
        print("\nThere is no figure with this number")
    elif figure == 1:
        print(f'\nArea of triangle equals: {right_triangle_area()} cm2')
    elif figure == 2:
        print(f'\nArea of rhombus equals: {rhombus_area()} cm2')
    elif figure == 3:
        print(f'\nArea of square equals: {square_area()} cm2')
    elif figure == 4:
        print(f'\nArea of circle equals: {circle_area()} cm2')
    elif figure == 5:
        print(f'\nArea of rectangle equals: {rectangle_area()} cm2')
    else:
        print(f'\nArea of parallelogram equals: {parallelogram_area()} cm2')


if __name__ == "__main__":
    main()


"""Variant with named parameters"""
# def triangle_area(first_leg: float, second_leg: float) -> float: return round(first_leg * second_leg / 2, 2)
#
#
# def rhombus_area(f_diagonal: float, s_diagonal: float) -> float: return round(f_diagonal * s_diagonal / 2, 2)
#
#
# def square_area(side: float) -> float: return round(side ** 2, 2)
#
#
# def circle_area(radius: float) -> float: return round(radius ** 2 * 3.14, 2)
#
#
# def rectangle_area(length: float, width: float) -> float: return round(length * width, 2)
#
#
# def parallelogram_area(base: float, height: float) -> float: return round(base * height, 2)
#
#
# def main():
#     print("Triangle = 1 \t Rhombus = 2"
#           "\nSquare = 3 \t\t Circle = 4"
#           "\nRectangle = 5 \t Parallelogram = 6")
#     figure = int(input("\nArea of which figure you want to know: "))
#     if figure > 6 or figure < 0:
#         print("There is no figure with this number")
#     elif figure == 1:
#         print(f'\nArea of triangle equals: {triangle_area(23, 33)} cm2')
#     elif figure == 2:
#         print(f'\nArea of rhombus equals: {rhombus_area(15, 44)} cm2')
#     elif figure == 3:
#         print(f'\nArea of square equals: {square_area(22)} cm2')
#     elif figure == 4:
#         print(f'\nArea of circle equals: {circle_area(33.3)} cm2')
#     elif figure == 5:
#         print(f'\nArea of rectangle equals: {rectangle_area(16, 22)} cm2')
#     else:
#         print(f'\nArea of parallelogram equals: {parallelogram_area(22, 88)} cm2')
#
#
# if __name__ == "__main__":
#     main()
