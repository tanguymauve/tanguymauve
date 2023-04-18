team = []
bestcards = []
bestlinkpartner = []
category = ["Saiyan", "Namek"]


i = 0
usercategory = input("Entrer la catégorie de votre team\n")
for item  in category:
    if usercategory == item:
        print("Great!")
    else:
        usercategory = input("The category is not in the list, type another category\n")


class Character:
    def __init__(self, data):
        self.name = data["name"]
        self.title = data["title"]
        self.maxLevel = data["maxLevel"]
        self.maxSALevel = data["maxSALevel"]
        self.rarity = data["rarity"]
        self.characterClass = data["class"]
        self.type = data["type"]
        self.cost = data["cost"]
        self.id = data["id"]
        self.imageURL = data["imageURL"]
        self.leaderSkill = data["leaderSkill"]
        self.ezaLeaderSkill = data["ezaLeaderSkill"]
        self.superAttack = data["superAttack"]
        self.ezaSuperAttack = data["ezaSuperAttack"]
        self.ultraSuperAttack = data["ultraSuperAttack"]
        self.ezaUltraSuperAttack = data["ezaUltraSuperAttack"]
        self.passive = data["passive"]
        self.ezaPassive = data["ezaPassive"]
        self.links = data["links"]
        self.categories = data["categories"]
        self.kiMeter = data["kiMeter"]
        self.baseHP = data["baseHP"]
        self.maxLevelHP = data["maxLevelHP"]
        self.freeDupeHP = data["freeDupeHP"]
        self.rainbowHP = data["rainbowHP"]
        self.baseAttack = data["baseAttack"]
        self.maxLevelAttack = data["maxLevelAttack"]
        self.freeDupeAttack = data["freeDupeAttack"]
        self.rainbowAttack = data["rainbowAttack"]
        self.baseDefence = data["baseDefence"]
        self.maxDefence = data["maxDefence"]
        self.freeDupeDefence = data["freeDupeDefence"]
        self.rainbowDefence = data["rainbowDefence"]
        self.kiMultiplier = data["kiMultiplier"]
        self.transformations = data["transformations"]

    def display_info(self):
        print("Name:", self.name)
        print("Title:", self.title)
        print("Max Level:", self.maxLevel)
        print("Max SA Level:", self.maxSALevel)
        print("Rarity:", self.rarity)
        print("Class:", self.class_type)
        print("Type:", self.type)
        print("Cost:", self.cost)
        print("ID:", self.id)
        print("Image URL:", self.imageURL)
        print("Leader Skill:", self.leaderSkill)
        print("EZA Leader Skill:", self.ezaLeaderSkill)
        print("Super Attack:", self.superAttack)
        print("EZA Super Attack:", self.ezaSuperAttack)
        print("Ultra Super Attack:", self.ultraSuperAttack)
        print("EZA Ultra Super Attack:", self.ezaUltraSuperAttack)
        print("Passive:", self.passive)
        print("EZA Passive:", self.ezaPassive)
        print("Links:", self.links)
        print("Categories:", self.categories)
        print("Ki Meter:", self.kiMeter)
        print("Base HP:", self.baseHP)
        print("Max Level HP:", self.maxLevelHP)
        print("Free Dupe HP:", self.freeDupeHP)
        print("Rainbow HP:", self.rainbowHP)
        print("Base Attack:", self.baseAttack)
        print("Max Level Attack:", self.maxLevelAttack)
        print("Free Dupe Attack:", self.freeDupeAttack)
        print("Rainbow Attack:", self.rainbowAttack)
        print("Base Defense:", self.baseDefence)
        print("Max Defense:", self.maxDefence)
        print("Free Dupe Defense:", self.freeDupeDefence)
        print("Rainbow Defense:", self.rainbowDefence)
        print("KI Multiplier:", self.kiMultiplier)
        print("Transformations:", self.transformations)



