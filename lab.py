
from math import floor
import random

class Character(object):
	level = 8
	strength = 18 
	dexterity = 12
	constitution = 14
	intelligence = 8
	wisdom = 10
	charisma = 8
	max_hp = 10 + 14 + 1d10 + 8
	hp = max_hp
	armour_class = 10 + 12
	initiative = 1d20 + 12

	def attack(self):

	def save_throw(self, attribute):

        @abstractmethod
        def perk(self):
    	
class Dragon(Character):
	@abstractmethod
        def perk(self):
	

	
class Hero(Character):
	@abstractmethod
        def perk(self):
