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


class cow (Animals):
    milk = true
    minweight = 30
    maxwigth = 500


class sheep (Animals):
    wool = true
    minweight = 20
    maxwigth = 80


class goat (Animals):
    cheese = true
    minweight = 10
    maxwigth = 30


class pig (Animals):
    lard = true
    minweight = 30
    maxwigth = 200


class duck (Birds):
    maxspeed = 20
    minspeed = 1


class chicken (Birds):
    maxspeed = 3
    minspeed = 1


class goose (Birds):
    maxspeed = 30
    minspeed = 1
