'''
File: OOP_Main.py
Description: The main code file/module
Author: Alisher Kenja
StudentID: 110414870
EmailID: kenay030
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractclassmethod


class Alchemist:
    # The attributes in Alchemist from attack to necromancy are values between 0 and 100 which indicate the
    # strength of that attribute. An alchemist knows the following recipes that can create two types of potions,
    # super potions and extreme potions. The recipe of a super potions consists of a herb and a catalyst. The
    # recipe of an extreme potion consists of a herb or catalyst and a super potion:

    # The alchemist knows the recipe but the recipes are stores in the labratory
    # An alchemist can mix a potion and will make use of the functionality in a laboratory for it.
    # If an alchemist drinks a potion then it will increase their attack, strength, defence, magic, range, or
    # necromancy depending on what the potion’s status is.
    # When an alchemist collects a reagent then they will add it to its laboratory.
    # Refining reagents means that an alchemist will refine all herbs and catalysts in the laboratory
    def __init__(self, attack, strength, defence, magic, ranged, necromancy, labratory):
        self.__attack = attack
        self.__strength = strength
        self.__defence = defence
        self.__defence = defence
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__labratory = labratory
        self.__recipes= {"Super Attack: Irit, Eye of Newt"
                        "Super Strength: Kwuarm, Limpwurt Root"
                        "Super Defence: Cadantine, White Berries"
                        "Super Magic: Lantadyme, Potato Cactus"
                        "Super Ranging: Dwarf Weed, Wine of Zamorak"
                        "Super Necromancy: Arbuck, Blood of Orcus"
                        "Extreme Attack: Avantoe, Super Attack"
                        "Extreme Strength: Dwarf Weed, Super Strength"
                        "Extreme Defence: Lantadyme, Super Defence"
                        "Extreme Magic: Ground Mud Rune, Super Magic"
                        "Extreme Ranging: Grenwall Spike, Super Ranging"
                        "Extreme Necromancy: Ground Miasma Rune, Super Necromancy"}
    
    def mixPotions(self, ingredient1, ingredient2):
        recipes = {
            ("Irit", "Eye of Newt"): "New - Super Attack Potion created",
            ("Kwuarm", "Limpwurt Root"): "New - Super Strength Potion created",
            ("Cadantine", "White Berries"): "New - Super Defence Potion created",
            ("Lantadyme", "Potato Cactus"): "New - Super Magic Potion created",
            ("Dwarf Weed", "Wine of Zamorak"): "New - Super Ranging Potion created",
            ("Arbuck", "Blood of Orcus"): "New - Super Necromancy Potion created",
            ("Avantoe", "Super Attack"): "New - Extreme Attack Potion created",
            ("Dwarf Weed", "Super Strength"): "New - Extreme Strength Potion created",
            ("Lantadyme", "Super Defence"): "New - Extreme Defence Potion created",
            ("Ground Mud Rune", "Super Magic"): "New - Extreme Magic Potion created",
            ("Grenwall Spike", "Super Ranging"): "New - Extreme Ranging Potion created",
            ("Ground Miasma Rune", "Super Necromancy"): "New - Extreme Necromancy Potion created"
        }

        potion = recipes.get((ingredient1, ingredient2))
        if potion is None:
            potion = recipes.get((ingredient2, ingredient1))
        message = potion if potion else "Invalid combination of ingredients"
        return f"{message}" if potion else message
        
    def drinkPotion(self, potion):
        if isinstance(potion, SuperPotion):
            # Calculate boost for SuperPotion
            boost = potion.calculateBoost()

            # Update attributes based on boost
            self.__attack += boost
            self.__strength += boost
            # ... Update other attributes based on potion type
            return f"Drank SuperPotion, attributes boosted by {boost}"
        
        elif isinstance(potion, ExtremePotion):
            # Calculate boost for ExtremePotion
            boost = potion.calculateBoost()

            # Update attributes based on boost
            self.__attack += boost
            self.__strength += boost
            # ... Update other attributes based on potion type
            return f"Drank ExtremePotion, attributes boosted by {boost}"
        
        else:
            return "Invalid potion type"
    
    @property
    def getLabratory(self):
        return self.__labratory

    @property
    def getRecipes(self):
        return self.__recipes
    
    def collectReagent(self, reagent, ):
        self.__labratory.addReagent(reagent)
            
    def refineReagents(self):
        # Refine all herbs and catalysts in the laboratory
        for herb in self.__labratory.getHerbs():
            herb.refine()
        for catalyst in self.__labratory.getCatalysts():
            catalyst.refine()



class Laboratory:
    # The laboratory stores the potions, herbs, and catalysts.
    # It provides functionality for an alchemist to mix potions: Each potion that is mixed has a name and its first
    # ingredient is either a herb or a catalyst that is stored in the laboratory. The second ingredient is either a
    # catalyst or another potion. Depending on the potion type, the proper potion must be created. Which
    # attribute of an alchemist the potion is increasing is specified in the status of the potions.
    # Reagents can be added to the laboratory. To keep it simple, this functionality specifies the amount of
    # reagents being available in the laboratory.
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, ingredient1, ingredient2):
        if isinstance(ingredient1, (Herb, Catalyst)) and isinstance(ingredient2, (Herb, Catalyst, SuperPotion)):
            if isinstance(ingredient2, SuperPotion):
                # Create an ExtremePotion based on the given ingredients
                new_potion = ExtremePotion(ingredient1, ingredient2)
            else:
                # Create a SuperPotion based on the given ingredients
                new_potion = SuperPotion(ingredient1, ingredient2)

            self.__potions.append(new_potion)
            print(f"{name} potion successfully mixed.")
        else:
            print("Invalid ingredients for mixing a potion.")

    def addReagent(self, reagent):
        if isinstance(reagent, Reagent):
            if isinstance(reagent, Herb):
                self.__herbs.append(reagent)
            elif isinstance(reagent, Catalyst):
                self.__catalysts.append(reagent)
            print(f"{reagent.getName()} added to the laboratory.")
        else:
            print("Invalid Reagent. Cannot add to the laboratory.")


class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost
        
    @abstractclassmethod
    def calculateBoost(self):
        pass

    def getName(self):
        return self.__name
    
    def getStat(self):
        return self.__stat
        
    def getBoost(self):
        return self.__boost
    
    def setBoost(self, boost):
        self.__boost = boost
        
class SuperPotion(Potion):
    def __init__(self, herb, catalyst):
        self.__herb = herb
        self.__catalyst = catalyst
        
    def calculateBoost(self, herbPotency, catalystPotency, catalystQuality):
        # potency of its herb + (potency of its catalyst * quality of its catalyst) * 1.5. The result 
        # should be rounded by 2 decimals.
        herbPotency = self.__herb.getPotency()
        catalystPotency = self.__catalyst.getPotency()
        catalystQuality = self.__catalyst.getQuality()

        boost = herbPotency + (catalystPotency * catalystQuality) * 1.5
        return round(boost, 2)
    
    @property
    def getHerb(self):
        return self.__herb
    
    @property
    def getCatalyst(self):
        return self.__catalyst
    
    
class ExtremePotion(Potion):
    def __init__(self, reagent, potion):
        self.__reagent = reagent
        self.__potion = potion
        
    def calculateBoost(self):
        #(potency of its reagent * boost value of its super potion) * 3.0. The result should be
        # rounded by two decimals
        
        # Calculate boost for Extreme Potion
        if isinstance(self.__potion, SuperPotion):  # Check if it's a SuperPotion
            super_potion_boost = self.__potion.calculateBoost()  # Get boost value of the SuperPotion
            boost = (self.__reagent.getPotency() * super_potion_boost) * 3.0
            return round(boost, 2)  # Round the result by two decimals
        else:
            return 0  # Return 0 if it's not a valid SuperPotion
    
    @property
    def getReagent(self):
        return self.__reagent
    
    @property
    def getPotion(self):
        return self.__potion
            



class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractclassmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, potency):
        self.__potency = potency
        
        

class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True
        
    def refine(self):
        # : Refining leads to a herb that is not grimy and will multiply its existing potency by 2.5. It will
        # print this information on the screen as well
        if self.__grimy:
            self.__grimy = False
            self.setPotency(self.getPotency() * 2.5)
            print(f"{self.getName()} has been refined. It is no longer grimy. Potency multiplied by 2.5.")
        else:
            print(f"{self.getName()} is already refined and not grimy.")
    
    @property       
    def getGrimy(self):
        return self.__grimy
    
    @property
    def setGrimy(self, grimy):
        self.__grimy = grimy

class Catalyst(Reagent):
    def __init__(self, quality, name, potency):
        super().__init__(name, potency)
        self.__quality = quality
    
    def refine(self):
        # If the quality of the catalyst is below 8.9 then its quality will be increased by 1.1 and this
        # information is printed on the screen. If its quality is equal or above 8.9 then its quality is set to 10.
        # It should print on the screen the quality and say that “it cannot be refined any further”.
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"Quality of {self.getName()} increased to {self.__quality}.")
        else:
            self.__quality = 10
            print(f"{self.getName()} cannot be refined any further. Quality set to 10.")
    
    @property
    def getQuality(self):
        return self.__quality
    
    
    
# self.__potions = ["Super Attack", "Super Strength", "Super Defence", "Super Magic", "Super Ranging", "Super Necromancy",
#                     "Extreme Attack", "Extreme Strength", "Extreme Defence", "Extreme Magic", "Extreme Ranging", "Extreme Necrmancy"]
# self.__herbs = ["Arbuck", "Avantoe", "Cadantine", "Dwarf Weed", "Ifrit", "Kwuarm", "Lantadyme", "Torstol"]
# self.__catalysts = ["Eye of Newt", "Limpwurt Root", "White Berries", "Potato Cactus", "Wine of Zamorak", 
#                     "Blood of Orcus", "Ground Mud Rune", "Grenwall Spike", "Ground Miasma Rune"]



lab = Laboratory
alchemist =  Alchemist(50, 50, 50, 50, 50, 50, lab)

newPotion = alchemist.mixPotions("Eye of Newt", "Irit")
print(newPotion)

drankThePotion = alchemist.drinkPotion("Super")
