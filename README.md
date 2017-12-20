# PY11-3.6
class Farm:
  eyes = 2
  food = true
  water = true
  pass
   
class Animals (Farm):
  legs = 4
  meat = true
class Birds (Farm):
  legs = 2
  eggs = true
  plumage = true
  
class cow (Animals):
  milk = true
class sheep (Animals):
  wool = true
class goat (Animals):
  cheese = true
class pig (Animals):
  lard = true

class duck (Birds):
  fly_speed = 30
class chicken (Birds):
  fly_speed = 0
class goose (Birds):
  fly_speed = 25
