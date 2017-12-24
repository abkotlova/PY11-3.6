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


class Goose (Birds):
    maxspeed = 30
    minspeed = 1

cow_1 = Cow()
cow_2 = Cow()
chicken_1 = Chicken()
