'''
File: OOP_Test.py
Description: The testing file/module
Author: Alisher Kenja
StudentID: 110414870
EmailID: kenay030
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import unittest
from OOP_Main import Alchemist, Laboratory, Herb, Catalyst, SuperPotion, ExtremePotion

lab = Laboratory()
alchemist = Alchemist(attack=70, strength=80, defence=75, magic=90, ranged=85, necromancy=55, labratory=lab)
herb = Herb("Irit", 3.0)
catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
super_potion = SuperPotion(herb, catalyst)

# Testing the mixPotions method
mix_output = alchemist.mixPotions(herb, catalyst)
print(mix_output)

# Testing the drinkPotion method
drink_output = alchemist.drinkPotion(super_potion)
print(drink_output)

# Testing the collectReagent method
alchemist.collectReagent(herb)
alchemist.collectReagent(catalyst)

# Testing the refineReagents method
alchemist.refineReagents()