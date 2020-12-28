from random import randint
from abc import ABC, abstractmethod
from math import floor


class init_hero(self):
	def hero(self):
   		level_hero = 8
   		strength_hero = 18
   		dexterity_hero = 12
   		constitution_hero = 14
   		intelligence_hero = 8
   		wisdom_hero = 10
   		charisma_hero = 8
   		average_damage_hero: 8.625
   		attacks_counts_hero: 8
   		healed_hero: 8
   		hp_hero = max_hp_hero
   		max_hp_hero = 10 + constitution_hero + randint(1, 11) * level_hero
   		hero_attack = (randint(1, 13) + (floor(strength_hero - 10) / 2))

class init_dragon(self):
	def gragon(self):
		level_dragon = 10
		strength_dragon = 20
		dexterity_dragon = 10
		constitution_dragon = 16
		intelligence_dragon = 8
		wisdom_dragon = 20
		charisma_dragon = 8
		average_damage_dragon: 11.25
		attacks_counts_dragon: 4
		hp_dragon = max_hp_dragon 
		max_hp_dragon = 10 + constitution_dragon + randint(1, 11) * level_dragon
		dragon_attack = (randint(1, 13) + (floor(strength_dragon - 10) / 2))

class Cont(unittest.TestCase):
	@abstractmethod
	def deth (self):
    

