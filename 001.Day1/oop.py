#OOP 
print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('Frey0xD'))
print(type([]))
print(type(()))
print(type({}))
print(type(2^45))

# in day 1 i'm going with oop theory so in upcoming projects we 
# can use this concept xD
class PlayerHacker:
  def __init__(self, name, skill):
    self.name = name
    self.skill = skill
  def hack(self):
    print('hack')

Player1 = PlayerHacker('Frey','None')
Player2 = PlayerHacker('Rakesh','Reverse Engineering')

# king of the hill
Player2.attack = 100

print(Player1) # Address
print(Player1.name)
print(Player2.skill)
print(Player2.attack)
