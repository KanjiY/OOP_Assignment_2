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

# Each method is tested
# Testing is appropriate to the given method. 
# could inlcude type testing and result testing


# lab = Laboratory()

# alchemist = Alchemist(50, 60, 70, 80, 90, 100, Laboratory())

# Set Herbs
# arbuck = Herb("Arbuck", 2.6)
# avantoe = Herb("Avantoe", 3.0)
# cadantine = Herb("Cadantine", 1.5)
# dwarf_weed = Herb("Dwarf Weed", 2.5)
# irit = Herb("Irit", 1.0)
# kwuarm = Herb("Kwuarm", 1.2)
# lantadyme = Herb("Lantadyme", 2.0)
# torstol = Herb("Torstol", 4.5)

# Set Catalysts
# eye_of_newt = Catalyst("Eye of Newt", 4.3, 1.0)
# limpwurt_root = Catalyst("Limpwurt Root", 3.6, 1.7)
# white_berries = Catalyst("White Berries", 1.2, 2.0)
# potato_cactus = Catalyst("Potato Cactus", 7.3, 0.1)
# wine_of_zamorak = Catalyst("Wine of Zamorak", 1.7, 5.0)
# blood_of_orcus = Catalyst("Blood of Orcus", 4.5, 2.2)
# ground_mud_rune = Catalyst("Ground Mud Rune", 2.1, 6.7)
# grenwall_spike = Catalyst("Grenwall Spike", 6.3, 4.9)
# ground_miasma_rune = Catalyst("Ground Miasma Rune", 3.3, 5.2)


# # Create Super Potions
# super_attack = SuperPotion(arbuck, eye_of_newt)
# super_strength = SuperPotion(kwuarm, limpwurt_root)
# super_defence = SuperPotion(cadantine, white_berries)
# super_magic = SuperPotion(lantadyme, potato_cactus)
# super_ranging = SuperPotion(dwarf_weed, wine_of_zamorak)
# super_necromancy = SuperPotion(irit, blood_of_orcus)

# # Create Extreme Potions
# extreme_attack = ExtremePotion(avantoe, super_attack)
# extreme_strength = ExtremePotion(dwarf_weed, super_strength)
# extreme_defence = ExtremePotion(lantadyme, super_defence)
# extreme_magic = ExtremePotion(ground_mud_rune, super_magic)
# extreme_ranging = ExtremePotion(grenwall_spike, super_ranging)
# extreme_necromancy = ExtremePotion(ground_miasma_rune, super_necromancy)


# # Drink Super Potions and apply effects
# alchemist.drinkPotion(super_attack)
# alchemist.drinkPotion(super_strength)
# alchemist.drinkPotion(super_defence)
# alchemist.drinkPotion(super_magic)
# alchemist.drinkPotion(super_ranging)
# alchemist.drinkPotion(super_necromancy)

# # Drink Extreme Potions and apply effects
# alchemist.drinkPotion(extreme_attack)
# alchemist.drinkPotion(extreme_strength)
# alchemist.drinkPotion(extreme_defence)
# alchemist.drinkPotion(extreme_magic)
# alchemist.drinkPotion(extreme_ranging)
# alchemist.drinkPotion(extreme_necromancy)