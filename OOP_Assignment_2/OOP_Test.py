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

class TestAlchemist(unittest.TestCase):
    def setUp(self):
        # Initialize necessary objects for testing
        self.lab = Laboratory()
        self.alchemist = Alchemist(attack=50, strength=60, defence=70, magic=80, ranged=90, necromancy=100, labratory=self.lab)
        self.herb = Herb("Irit", 1.0)
        self.catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
        self.super_potion = SuperPotion(self.herb, self.catalyst)
        self.extreme_potion = ExtremePotion(self.catalyst, self.super_potion)

    def test_mix_potions(self):
        result = self.alchemist.mixPotions("Irit", "Eye of Newt")
        self.assertEqual(result, "Super Attack Potion created")

    def test_drink_super_potion(self):
        boost = self.alchemist.drinkPotion(self.super_potion)
        self.assertEqual(boost, "Drank SuperPotion, attributes boosted by 15")

    def test_drink_extreme_potion(self):
        boost = self.alchemist.drinkPotion(self.extreme_potion)
        self.assertEqual(boost, "Drank ExtremePotion, attributes boosted by 25")

    def test_collect_reagent(self):
        self.alchemist.collectReagent(self.herb)
        self.assertIn(self.herb, self.lab.getHerbs())

    def test_refine_reagents(self):
        self.alchemist.collectReagent(self.catalyst)
        self.alchemist.refineReagents()
        self.assertEqual(self.catalyst.getQuality(), 10)  # Assuming quality 10 after refinement

    # Add more test cases for other methods as needed...

if __name__ == '__main__':
    unittest.main()


# Test cases for Laboratory class
def Test_lab_mix_potion():
    lab = Laboratory()
    # Implement tests for mixing potions in the lab
    assert lab.mixPotion() == expected_potion  # Provide expected potion object
    
def Test_lab_add_reagent():
    lab = Laboratory()
    herb = Herb("Irit", 1.0)
    lab.addReagent(herb)
    # Implement tests to check if reagents are added to the lab

# Test cases for Herb class
def Test_herb_refine():
    herb = Herb("Irit", 1.0)
    herb.refine()
    # Implement tests to verify if herb refining works as expected

# Test cases for Catalyst class
def Test_catalyst_refine():
    catalyst = Catalyst("Eye of Newt", 4.3, 1.0)
    catalyst.refine()
    # Implement tests to verify if catalyst refining works as expected

# Test cases for SuperPotion class
def Test_super_potion_calculate_boost():
    super_potion = SuperPotion(Herb("Irit", 1.0), Catalyst("Eye of Newt", 4.3, 1.0))
    boost = super_potion.calculateBoost()
    # Implement tests to check if the boost calculation is correct

# Test cases for ExtremePotion class
def Test_extreme_potion_calculate_boost():
    extreme_potion = ExtremePotion(Herb("Avantoe", 3.0), SuperPotion(Herb("Irit", 1.0), Catalyst("Eye of Newt", 4.3, 1.0)))
    boost = extreme_potion.calculateBoost()
    # Implement tests to check if the boost calculation is correct



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