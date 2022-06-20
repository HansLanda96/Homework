def square(side: int | float) -> tuple:
    perimetr = side * 4
    diagonal = side * 2 ** 0.5
    area = side ** 2
    return perimetr, diagonal, area


def main():
    side = square(5.5)
    print(f'\nPerimetr of square equal: {round(side[0], 2)} cm'
          f'\nDiagonal of square equal: {round(side[1], 2)} сm'
          f'\nArea of square equal: {round(side[2], 2)} cm2')


if __name__ == "__main__":
    main()
