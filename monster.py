'''
Aggiungo un limite.
Fare in modo che il mostro non possa uscire dalla griglia 
'''
class Entity:
  def __init__(self, x, y, field): 
    self.x = x
    self.y = y
    self.field = field
    self.field.entities.append(self) #aggiungo entity al field
  
  def move(self, direction):
    if direction == "up":
      self.y -= 1
    elif direction == "down":
      self.y += 1
    elif direction == "right":
      self.x += 1
    elif direction == "left":
      self.x -= 1
  
  def check_field(self):
    if self.x >= self.field.w:
      print("entità non può muoversi più a destra")
      self.x -= 1
    elif self.x < 0:
      print("entità non può muoversi più a sinistra")
      self.x += 1
    elif self.y >= self.field.h:
      print("entità non può muoversi più in basso")
      self.y -= 1
    elif self.y < 0:
      print("entità non può muoversi più in alto")
      self.y += 1
    else:
      return True
   
class Monster(Entity):
  def __init__(self, x, y, name, damage, field):
    super().__init__(x, y, field)
    self.name = name
    self.hp = 10
    self.damage = damage

  def info(self):
    print("sono", self.name, "hp:", self.hp, "/10", "e mi trovo a", self.x, ",", self.y)

  def attack(self, enemy):
    if self.hp <= 0:
      print(self.name, "prova ad attaccare da morto con scarsi risultati")
    else: 
      print(self.name, "attacca", enemy.name)

      if enemy.hp <= 0:
        print(enemy.name, "e' morto")
      else:
        enemy.hp -= self.damage

class Field:
  def __init__(self):
    self.w = 5
    self.h = 5
    self.entities = []

  def draw(self): #disegno il campo
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if x == e.x and y == e.y:
            print("[x]", end = "")
            break    
        else:
          print("[ ]", end = "")
      print()
def check(entity):
    if entity.check_field()== True : 
        field.draw()

field = Field()
m = Monster(2, 2, "Pino", 10, field)
m = Monster(1, 1, "Gino", 10, field)
field.draw()

for f in range(6): #esce dalla griglia 
    print()
    m.move("down")
    check(m)