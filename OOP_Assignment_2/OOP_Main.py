'''
File: OOP_Main.py
Description: The main code file/module
Author: Alisher Kenja
StudentID: 110414870
EmailID: kenay030
This is my own work as defined by the University's Academic Misconduct Policy.
'''

# Github Repository
# https://github.com/KanjiY/OOP_Assignment_2.git


from abc import ABC, abstractclassmethod


class Alchemist:
    def __init__(self, attack, strength, defence, magic, ranged, necromancy, labratory):
        self.__attack = attack
        self.__strength = strength
        self.__defence = defence
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__labratory = labratory
        # Recipes for creating potions stored in a Dictionary
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
        """Mixes potions based on provided ingredients."""
        # Sets the Potions for the type of recipe the user inserts
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

        # tries to crate the potions with the ingredients in both orders then returns the relevent message
        potion = recipes.get((ingredient1, ingredient2))
        if potion is None:
            potion = recipes.get((ingredient2, ingredient1))
        message = potion if potion else "Invalid combination of ingredients"
        return f"{message}" if potion else message
        
    def drinkPotion(self, potion):
        """Applies a Buff to the statistic bassed on the potion and potion type"""
        # Checks if the potion drank is a SuperPotion
        if isinstance(potion, SuperPotion):
            boost = potion.calculateBoost()
            stat = potion.getStat()
            
            # Applies the bonus only to the stat where it makes sense
            if stat == "attack":
                self.__attack += boost
            elif stat == "strength":
                self.__strength += boost
            elif stat == "defence":
                self.__defence += boost
            elif stat == "magic":
                self.__magic += boost
            elif stat == "ranged":
                self.__ranged += boost
            elif stat == "necromancy":
                self.__necromancy += boost
            return f"Drank SuperPotion, {stat.capitalize()} boosted by {boost}"

        elif isinstance(potion, ExtremePotion):
            boost = potion.calculateBoost()
            stat = potion.getStat()

            if stat == "attack":
                self.__attack += boost
            elif stat == "strength":
                self.__strength += boost
            elif stat == "defence":
                self.__defence += boost
            elif stat == "magic":
                self.__magic += boost
            elif stat == "ranged":
                self.__ranged += boost
            elif stat == "necromancy":
                self.__necromancy += boost
            return f"Drank ExtremePotion, {stat.capitalize()} boosted by {boost}"

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
        """Re-refines all the reagents"""
        # Refine all herbs and catalysts in the laboratory
        for herb in self.__labratory.getHerbs():
            herb.refine()
        for catalyst in self.__labratory.getCatalysts():
            catalyst.refine()



class Laboratory:
    
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self, name, ingredient1, ingredient2):
        """Creates new potions based on the reagents used """
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

    def addReagent(self, reagent_name, potency, quality=None):
        """Adds a new reagent to the laboratory."""
        if quality is not None:
            # Create a Catalyst object and add it to the list of reagents
            reagent = Catalyst(quality, reagent_name, potency)
        else:
            # Create a Herb object and add it to the list of reagents
            reagent = Herb(reagent_name, potency)
        
        self.__reagents.append(reagent)
        print(f"{reagent.getName()} added to the laboratory.")


class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost
        
    @abstractclassmethod
    def calculateBoost(self):
        pass

    @property
    def getName(self):
        return self.__name
    
    @property
    def getStat(self):
        return self.__stat
    
    @property
    def getBoost(self):
        return self.__boost
    
    @Boost.setter
    def setBoost(self, boost):
        self.__boost = boost
        
class SuperPotion(Potion):
    def __init__(self, herb, catalyst):
        self.__herb = herb
        self.__catalyst = catalyst
        
    def calculateBoost(self, herbPotency, catalystPotency, catalystQuality):
        """Calculates boost based off formula in Documentation"""
        # Get the potency values of the herb and catalyst
        herbPotency = self.__herb.getPotency()
        catalystPotency = self.__catalyst.getPotency()

        # Get the quality value of the catalyst
        catalystQuality = self.__catalyst.getQuality()

        # Calculate the boost based on the formula
        boost = herbPotency + (catalystPotency * catalystQuality) * 1.5
        # Round the result by two decimals
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
        """Calculates boost based off formula in Documentation"""
        # Check if it's a SuperPotion
        if isinstance(self.__potion, SuperPotion):  
            # Get boost value of the SuperPotion
            super_potion_boost = self.__potion.calculateBoost()  
            boost = (self.__reagent.getPotency() * super_potion_boost) * 3.0
            # Round the result by two decimals
            return round(boost, 2)  
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
    
    @property
    def getName(self):
        return self.__name

    @property
    def getPotency(self):
        return self.__potency

    @Potency.setter
    def setPotency(self, potency):
        self.__potency = potency
        
        

class Herb(Reagent):
    def __init__(self, name, potency):
        super().__init__(name, potency)
        self.__grimy = True
        
    def refine(self):
        """Refines the Herb if its has not already been refined or is not grimy"""
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
        """Refines the Catalyst if its has not already been refined or is not grimy"""
        if self.__quality < 8.9:
            self.__quality += 1.1
            print(f"Quality of {self.getName()} increased to {self.__quality}.")
        else:
            self.__quality = 10
            print(f"{self.getName()} cannot be refined any further. Quality set to 10.")
    
    @property
    def getQuality(self):
        return self.__quality