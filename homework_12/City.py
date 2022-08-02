from random import randint
from tabulate import tabulate


class City:
    """
           A class that represent City.
           Create your own City with streets, houses and population.


       __init__ Attributes
       __________
       name: str
            Name of the city

       streets: dict
            Allows to create dict from street. That could be filled with houses and population

       __________

       Methods
       __________
       city_filler:
            You can fill City with just one method

       city_population: @property
            Give sum of population in all houses for each street

       add_house:
            Allows to create house on the street (add house in the end of a list)

       del_houses:
            Allows to delete few houses on the street (0 - delete firs index house, -1 - delete last house)

       add_streets:
            Allows to generate streets in your City in one row

       del_streets:
            Allows to delete few streets in the City on your taste :D

       prettytable:
            Generate table for beautiful output of City that you create

       prettyprint:
            Return generated table

       format_streets:
            Return formatted streets list and fill __str__ method with returned streets

       __str__:
            Print beautiful output in console :D
       """

    def __init__(self, name: str):
        self.name = name
        self._streets = {}

    def city_filler(self):
        streets = ["gogi", "shmogi", "gogol", "mogol"]
        for names in streets:
            self.add_streets(names)

    @property
    def city_population(self):
        return sum(street.street_population for _, street in self._streets.items())

    def add_house(self, name: str):
        self._streets[name].add_house()

    def del_houses(self, name: str, *house_index: [int]):
        for index in house_index:
            self._streets[name].del_house(index)

    def add_streets(self, *name: [str]):
        for street in name:
            self._streets[street] = Street(street)

    def del_streets(self, *name: [str]):
        for street in name:
            del self._streets[street]

    def prettytable(self):
        table = []
        for street_name, street in self._streets.items():
            for house in street.houses:
                table.append({
                    "Street": street_name.capitalize(),
                    "House": house.number,
                    "Population in the house": house.population
                })
        return table

    def prettyprint(self):
        return tabulate(self.prettytable(), headers="keys", tablefmt="fancy_grid", showindex=True)

    def format_streets(self):
        return ", ".join([str(street).capitalize() for street in self._streets])

    def __str__(self):
        return f'''
        City: {self.name}
        Streets in {self.name}: {self.format_streets()}
        Population of {self.name}: {self.city_population} people
        '''

    def __repr__(self):
        return self.__str__()


class House:
    """
           Class represent house on the street. House has a number, and random population from 50 to 100 peoples.
    """
    def __init__(self, number: int):
        self.number = number
        self.population = randint(50, 100)


class Street:
    """
           Class represent street in the city.

       __init__ Attributes
       __________
       name: str
            Name of a street

       amount:
            Generate house(object) on the street. Generate from 5 to 21 houses.

       houses:
            Fill streets with created list of houses

       street_population: property
            Return population of street

       add_house:
            Create house on the street and give number "1" for it. Also add house(object)

       del_house:
            Delete house by index on the street. Also delete house(object)
    """
    def __init__(self, name: str):
        self.name = name
        self.amount = randint(5, 21)
        self.houses = [House(house + 1) for house in range(self.amount)]

    @property
    def street_population(self):
        return sum(house.population for house in self.houses)

    def add_house(self):
        self.houses.append(House(self.houses[-1].number + 1))
        self.amount += 1

    def del_house(self, number: int):
        del self.houses[number]
        self.amount -= 1


def main():
    city = City("Novigrad")
    city.city_filler()
    city.del_streets("gogi", "shmogi", "gogol", "mogol")
    city.add_streets("plotvinska", "novigradska", "chornobaivska", "vesimirska", "lastochkina", "cirivska")
    city.del_streets("chornobaivska")
    city.del_houses("plotvinska", 0, 0, 0, 0)
    city.del_houses("lastochkina", -1, -1, -1, -1)
    city.add_house("lastochkina")

    print(f'{city} \n{city.prettyprint()}')


if __name__ == '__main__':
    main()
