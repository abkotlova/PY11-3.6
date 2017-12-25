class Farm:
    eyes = 2
    food = true
    water = true
    pass


class Animals (Farm):
    legs = 4
    meat = true
    minweight = 10
    maxweight = 500


class Birds (Farm):
    legs = 2
    eggs = true
    plumage = true
    maxspeed = 30
    minspeed = 1


class Cow (Animals):
    milk = true
    minweight = 30
    maxwigth = 500

    def __init__(self, minweight, maxwight):
        self.minweight = minweight
        self.maxwight = maxwight


class Sheep (Animals):
    wool = true
    minweight = 20
    maxwigth = 80


class Goat (Animals):
    cheese = true
    minweight = 10
    maxwigth = 30


class Pig (Animals):
    lard = true
    minweight = 30
    maxwigth = 200


class Duck (Birds):
    maxspeed = 20
    minspeed = 1


class Chicken (Birds):
    maxspeed = 3
    minspeed = 1

    def __init__(self, maxspeed, minspeed):
        self.maxspeed = maxspeed
        self.minspeed = minspeed


class Goose (Birds):
    maxspeed = 30
    minspeed = 1

cow_1 = Cow(35, 300)
cow_2 = Cow(45, 400)
chicken_1 = Chicken(2, 1)
