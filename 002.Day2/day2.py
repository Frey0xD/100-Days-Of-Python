
class hacker:
	membership = True
	def __init__(self, name):
		if (hacker.membership):
			self.name = name

	def shout(self):
		print(f'my name is {self.name}')

	def onepiece(self, hello):
		print(f'one piece is real {self.name}')
		

hacker1 = hacker('frey')

hacker2 = hacker('prince')

print(hacker1.name)
print(hacker1.shout())
print(hacker2.membership)
print(hacker2.onepiece('PirateKing'))