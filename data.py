from random import choice, randrange, random

class Data:
    def __init__(self): 
        self.version = '1.1.5'
        self.races = (Human, Dragonborn, Elf, Gnome, Halfling, Dwarf, HalfElf, HalfOrc)
        self.classes = (Barbarian, Cleric, Bard, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard)
        self.attributes = {
            "languages": ['Abyssal', 'Celestial', 'Draconic', 'Deep Speech', 'Dwarvish', 'Elven', 'Giant', 'Gnomish', 'Goblin', 'Halfling', 'Infernal', 'Orc', 'Sylvan', 'Undercommon'],
            "deities": ["Auril", "Azuth", "Bhaal", "Cyric", "Helm", "Leira", "Malar", "Savra", "Selune", "Shar", "Sune", "Talona", "Talos", "Tempus", "Torm", "Tyr", "Umberlee", "Waukeen"],
            "hair_colors": ['Black', 'Brown', 'Blond', 'Red', 'White', 'Grey'],
            "hair_types": ['Curly', 'Wavy', 'Straight', 'Flowing', 'Frizzy', 'Spiky', 'Touseled', 'Unkempt'],
            "eye_colors": ['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'],
            "appearance": ['Jewelry', 'Piercings', 'Formal Clothing', 'Ragged', 'Missing Teeth', 'Scar', 'Tattoos', 'Birthmark', 'Bald', 'Braided Hair', 'Beautiful', 'Ugly'],
            "talents": ['Musical', 'Fluent In Many Languages', 'Lucky', 'Perfect Memory', 'Good With Animals', 'Great At Games', 'Artist', 'Skilled Dancer', 'Juggles', 'Expert Horseback Rider'],
            "mannerisms": ['Prone To Singing Or Whistling', 'Loves To Rhyme', 'Slurs Words', 'Enunciates Clearly', 'Speaks Loudly', 'Whispers', 'Comedian', 'Bites Fingernails', 'Taps Fingers'],
            "traits": ['Argumentative', 'Arrogant', 'Blustering', 'Rude', 'Curious', 'Friendly', 'Honest', 'Hot Tempered', 'Irritable', 'Quiet'],
        }
        
        # Currency Module
        self.exchangeRate = [round(100*random()), round(100*random())]

    @property
    def PickRandomRace(self): return choice(self.races)
    
    @property
    def PickRandomClass(self): return choice(self.classes)
    
    def PickRandomAttributes(self):
        attrb = {
            'deity': choice(self.attributes['deities']),
            'hair_color': choice(self.attributes['hair_colors']),
            'hair_type': choice(self.attributes['hair_types']),
            'eye_color': choice(self.attributes['eye_colors']),
            'appearance': choice(self.attributes['appearance']),
            'talent': choice(self.attributes['talents']),
            'mannerism': choice(self.attributes['mannerisms']),
        }
        
        return attrb

    @property
    def __repr__(self): return f'Dataset Version {self.version}'

class Race:
    def __init__(self, race:str='', firstNames=['None'], lastNames=['None'], attributes=['None']):
        self.race = race
        self.firstNames = firstNames
        self.lastNames = lastNames
        self.attributes = attributes

    def __repr__(self): return f'{self.race, self.firstNames, self.lastNames, self.attributes}'

class Human(Race):
    def __init__(self):
        super().__init__(self)
        self.race = 'Human'
        self.firstName = choice([
            'Aseir', 'Bardeid', 'Haseid', 'Khemed', 'Mehmen', 'Sudeiman', 'Zasheir',
            'Darvin', 'Dorn', 'Evendur', 'Gorstag', 'Grim', 'Helm', 'Malark', 'Morn', 'Randal', 'Stedd',
            'Bor', 'Fodel', 'Glar', 'Grigor', 'Igan', 'Ivor', 'Kosef', 'Mival', 'Orel', 'Pavel', 'Sergor',
            'Ander', 'Blath', 'Bran', 'Frath', 'Geth', 'Lander', 'Luth', 'Malcer', 'Stor', 'Taman', 'Urth',
            'Aoth', 'Bareris', 'Ehput Ki', 'Kethoth', 'Mumed', 'Ramas', 'So Kehur', 'Thazar De', 'Urhur',
            'Borivik', 'Faurgar', 'Jandar', 'Kanithar', 'Madislak', 'Ralmevik', 'Shaumar', 'Vladislak',
            'Chien', 'Huang', 'Kao', 'Kung', 'Lao', 'Ling', 'Mei', 'Pin', 'Shin', 'Sum', 'Tan', 'Wan',
            'Anton', 'Diero', 'Marcon', 'Pieron', 'Rimardo', 'Romero', 'Salazar', 'Umbero'
        ])
        self.lastName = choice([
            'Basha', 'Dumein', 'Jassan', 'Khalid', 'Mostana', 'Pashar', 'Rein',
            'Amblecrown', 'Buckman', 'Dundragon', 'Evenwood', 'Greycastle', 'Tallstag',
            'Bersk', 'Chernin', 'Dotsk', 'Kulenov', 'Marsk', 'Nemetsk', 'Shemov', 'Starag',
            'Brightwood', 'Helder', 'Hornraven', 'Lackman', 'Stormwind', 'Windrivver',
            'Ankhalab', 'Anskuld', 'Fezim', 'Hahpet', 'Nathandem', 'Sepret', 'Uuthrakt',
            'An', 'Chen', 'Chi', 'Fai', 'Jiang', 'Jun', 'Lian', 'Long', 'Meng', 'On', 'Shan', 'Shui', 'Wen',
            'Agosto', 'Astorio', 'Calabra', 'Domine', 'Falone', 'Marivaldi', 'Pisacar', 'Ramondo'
        ])
        self.attributes = {
            'age': randrange(RollDice('1d6'), 15),
            'height': randrange(RollDice('2d4'), 58),
            'weight': randrange(RollDice('2d6'), 120),
            'size': 'Medium',
            'speed': 30,
            'traits': ['Versatility'],
            'languages': ['Elven', 'Draconic', 'Gnoll', 'Gnome', 'Goblin', 'Orc', 'Sylvan'],
        }
        
class Dragonborn(Race):
    def __init__(self):
        super().__init__(self)
        self.race = 'Dragonborn'
        self.firstName = choice(['Agon', 'Egon', 'Sugissa', 'Qixiris', 'Nysriel', 'Qicoria', 'Phidalynn', 'Wraxiris', 'Orinn', 'Yrsaadi', 'Mathtuan', 'Nysqorel', 'Zenpora', 'Wradalynn'])
        self.lastName = choice(['Shunxash', 'Girrhiliar', 'Nyelkanshteth', 'Dommicmellir', 'Preapinshtondeth', 'Karjualath', 'Cardaseargual', 'Fambucoth', 'Priarindraandin', 'Aapos'])
        self.attributes = {
            'age': randrange(RollDice('6d6'), 79),
            'height': randrange(RollDice('2d6'), 182),
            'weight': randrange(RollDice('1d6'), 210),
            'size': 'Medium',
            'speed': 30,
            'traits': ['Draconic Ancestory', 'Increased Resistance'],
            'languages': ['Draconic', 'Undercommon']            
        }

class Elf(Race):
    def __init__(self):
        super().__init__(self)
        self.race = 'Elf'
        self.firstName = choice([
            'Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Beiro', 'Berrian', 'Carric', 'Enialis', 'Erdan', 
            'Erevan', 'Galinndan', 'Hadarai', 'Heian', 'Himo', 'Immeral', 'Ivellios', 'Laucian', 'Mindartis', 
            'Paelias', 'Peren', 'Quarion', 'Riardon', 'Rolen', 'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis'
        ])
        self.lastName = choice(['Amakiir', 'Amastacia', 'Galanodel', 'Holimion', 'Ilphelkiir', 'Liadon', 'Meliamne', 'Naïlo', 'Siannodel', 'Xiloscient'])
        self.attributes = {
            'age': randrange(RollDice('6d6'), 110),
            'height': randrange(RollDice('2d6'), 58),
            'weight': randrange(RollDice('1d6'), 85),
            'size': 'Medium',
            'speed': 30,
            'traits': ['Darkvision', 'Fey Ancestory'],
            'languages': ['Elven', 'Draconic', 'Gnoll', 'Gnome', 'Goblin', 'Orc', 'Sylvan'],
        }

class Gnome(Race):
    def __init__(self):
        super().__init__(self)
        self.race = 'Gnome'
        self.firstName = choice(['Boddynock', 'Dimble', 'Fonkin', 'Gimble', 'Glim', 'Gerbo', 'Jebeddo', 'Namfoodle', 'Roondar', 'Seebo', 'Zook'])
        self.lastName = choice(['Beren', 'Daergel', 'Folkor', 'Garrick', 'Nackle', 'Murnig', 'Ningel', 'Raulnor', 'Scheppen', 'Turen'])
        self.nicknames = choice(['Aleslosh', 'Ashhearth', 'Badger', 'Cloak', 'Doublelock', 'Filchbatter', 'Fnipper', 'Oneshoe', 'Sparklegem', 'Stumbleduck'])
        self.attributes = {
            'age': randrange(RollDice('6d6'), 40),
            'height': randrange(RollDice('2d4'), 36),
            'weight': randrange(RollDice('1d6'), 40),
            'size': 'Small',
            'speed': 20,
            'traits': ['Tinker'],
            'languages': ['Gnomish', 'Draconic', 'Dwarvish', 'Elven', 'Giant', 'Goblin', 'Orc']
        }

class Halfling(Race):
    def __init__(self):
        super().__init__(self)
        self.race = 'Halfling'
        self.firstName = choice(['Alton', 'Ander', 'Cade', 'Corrin', 'Eldon', 'Errich', 'Finnan', 'Garret', 'Lindal', 'Lyle', 'Merric', 'Milo', 'Osborn', 'Perrin', 'Reed', 'Roscoe', 'Wellby'])
        self.lastName = choice(['Brushgather', 'Goodbarrel', 'Greenbottle', 'Highhill', 'Hilltopple', 'Leagallow', 'Tealeaf', 'Thorngage', 'Tosscobble', 'Underbough'])
        self.attributes = {
            'age': randrange(RollDice('3d5'), 20),
            'height': randrange(RollDice('2d4'), 32),
            'weight': randrange(RollDice('1d4'), 30),
            'size': 'Small',
            'speed': 20,
            'traits': ['Brave', 'Halfling Nimbleness'],
            'languages': ['Halfling', 'Dwarvish', 'Elven', 'Gnomish', 'Goblin', 'Orc']
        }

class Dwarf(Race):
    def __init__(self):
        super().__init__(self)
        self.race = 'Dwarf'
        self.firstName = choice(['Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor', 'Bruenor', 'Dain', 'Darrak', 'Delg', 'Eberk', 'Einkil', 'Fargrim', 'Flint', 'Gardain', 'Harbek', 'Kildrak', 'Morgran', 'Orsik', 'Oskar', 'Rangrim', 'Rurik','Taklinn', 'Thoradin', 'Thorin', 'Tordek', 'Traubon', 'Travok', 'Ulfgar', 'Veit', 'Vondal'])
        self.lastName = choice(['Balderk', 'Battlehammer', 'Brawnanvil', 'Dankil', 'Fireforge', 'Frostbeard', 'Gorunn', 'Holderhek', 'Ironfist', 'Loderr', 'Lutgehr', 'Rumnaheim', 'Strakeln', 'Torunn', 'Ungart'])
        self.clan = choice(['Balderk', 'Dankil', 'Gorunn', ' Holderhek', 'Loderr', 'Lutgehr', 'Rumnaheim', 'Strakeln', 'Torunn', 'Ungart'])
        self.attributes = {
            'age': randrange(RollDice('5d6'), 40),
            'height': randrange(RollDice('2d4'), 45),
            'weight': randrange(RollDice('2d6'), 130),
            'size': 'Medium',
            'speed': 20,
            'traits': ['Darkvision', 'Dwarven Resilience'],
            'languages': ['Dwarvish', 'Giant', 'Gnomish', 'Goblin', 'Orc', 'Undercommon'],
        }

class HalfElf(Elf):
    def __init__(self):
        super().__init__()
        self.race = 'Half-Elf'
        self.attributes = {
            'age': randrange(RollDice('2d6'), 20),
            'height': randrange(RollDice('2d8'), 55),
            'weight': randrange(RollDice('2d4'), 100),
            'size': 'Medium',
            'speed': 30,
            'traits': ['Darkvision', 'Fey Ancestory'],
            'languages': ['Dwarvish', 'Giant', 'Gnomish', 'Goblin', 'Orc', 'Undercommon'],
        }

class HalfOrc(Race):
    def __init__(self):
        super().__init__(self)
        self.race = 'Half-Orc'
        self.firstName = choice(['Dench', 'Feng', 'Gell', 'Henk', 'Holg', 'Imsh', 'Keth', 'Krusk', 'Ront', 'Shump', 'Thokk'])
        self.lastName = ''
        self.attributes = {
            'age': randrange(RollDice('1d6'), 14),
            'height': randrange(RollDice('2d12'), 58),
            'weight': randrange(RollDice('2d6'), 150),
            'size': 'Medium',
            'speed': 30,
            'traits': ['Darkvision', 'Savage Attacks'],
            'languages': ['Orc', 'Draconic', 'Giant', 'Gnoll', 'Goblin', 'Abyssal']
        }

class Class:
    def __init__(self, cl='', weapons=[], armor=[], skills=[], abilities=[], hp=0, gold='', background='', saving_throws=[], spells=[]):
        self.type = cl
        self.weapons = weapons
        self.armor = armor
        self.skills = skills
        self.abilities = abilities
        self.hp = hp
        self.gold = RollDice(gold)
        self.background = background
        self.saving_throws = saving_throws
        self.spells = spells

    def GenerateClass(self): 
        return f'''Class Information
        type: {self.type}
        weapon: {choice(self.weapons)}
        armor: {choice(self.armor)}
        ability: {choice(self.abilities) if len(self.abilities) > 0 else []}
        spells: {self.spells}
        skill: {choice(self.skills)}
        hp: {self.hp}
        gold: {self.gold}
        background: {self.background}
        saving throws: {self.saving_throws}
        '''

class Barbarian(Class):
    def __init__(self):
        super().__init__('Barbarian',
                       ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear', 'Battleaxe', 'Greatsword', 'Greataxe', 'Warhammer', 'Lance', 'Longsword'],
                       ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Breastplate', 'Halfplate'],
                       ['Athletics', 'Animal Handling', 'Intimidation', 'Nature', 'Perception', 'Survival'],
                       ['Rage', 'Unarmored Defense', 'Reckless Attack'], 12, '4d4', 'outlander', ['Strength', 'Constitution'], ['None'])

class Bard(Class):
    def __init__(self):
        super().__init__('Bard', 
                         ['Club', 'Longsword', 'Rapier', 'Shortbow', 'Dagger', 'Mace', 'Sickle', 'Quarterstaff', 'Spear', 'Crossbow, light', 'Dart', 'Sling'],
                         ['Padded', 'Leather', 'Studded Leather'],
                         ['Acrobatics', 'Animal Handling', 'Arcana', 'Athletics', 'Deception', 'History', 'Insight', 'Intimidation', 'Investigation', 'Medicine', 
                          'Nature', 'Perception', 'Performace', 'Persuasion', 'Religion', 'Sleight of Hand', 'Stealth', 'Survival'], ['Jack of All Trades', "Song of Rest"], 
                         6, '5d4', 'entertainer', ['Dexterity', 'Charisma'], ['Dancing Lights', 'Vicious Mockery', 'Charm Person', 'Detect Magic', 'Healing Word', 'Thunderwave'])

class Cleric(Class):
    def __init__(self):
        super().__init__('Cleric', 
                         ['Club', 'Longsword', 'Rapier', 'Shortbow', 'Dagger', 'Mace', 'Sickle', 'Quarterstaff', 'Spear', 'Crossbow, light', 'Dart', 'Sling'],
                         ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Breastplate', 'Halfplate'], ['Turn Undead'],
                         [], 8, '5d4', 'acolyte', ['Wisdom', 'Charisma'], ['Light', 'Mending', 'Spare the Dying', 'Cure Wounds', 'Guiding Bolt', 'Inflict Wounds'])

class Druid(Class):
    def __init__(self):
        super().__init__('Druid', ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear'], ['Padded', 'Leather', 'Studded Leather'],
                         ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival'], ['Wild Shape'], 
                         8, '2d4', 'hermit', ['Intelligence', 'Wisdom'], ['Thorn Whip', 'Produce Flame', 'Detect Magic', 'Cure Wounds', 'Mending', 'Purify Food and Drink', 'Resistance'])

class Fighter(Class):
    def __init__(self):
        super().__init__('Fighter', 
                         ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear', 'Battleaxe', 'Greatsword', 'Greataxe', 'Warhammer', 'Lance', 'Longsword'],
                         ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Breastplate', 'Halfplate', 'Ringmail', 'Chainmail', 'Splint', 'Plate'],
                         ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', "Survival"], ['Two-Weapon Fighting', 'Second Wind'],
                         10, '6d4', 'soldier', ['Strength', 'Constitution'], ['None'])

class Monk(Class):
    def __init__(self):
        super().__init__('Monk', 
                        ['Club', 'Shortsword', 'Dagger', 'Handaxe', 'Javelin', 'Nunchaku', 'Quarterstaff', 'Sling'], ['None'], 
                        ['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth'], ['Martial Arts', 'Stunning Fist', 'Unarmored Movement'], 8, '5d4', 
                        'hermit', ['Strength', 'Dexterity'], ['None'])

class Paladin(Class):
    def __init__(self):
        super().__init__('Paladin', 
                        ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear', 'Battleaxe', 'Greatsword', 'Greataxe', 'Warhammer', 'Lance', 'Longsword'], ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Breastplate', 'Halfplate', 'Ringmail', 'Chainmail', 'Splint', 'Plate'],
                        ['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion'], ['Divine Sense', 'Lay on Hands'], 10, '6d4',
                        'noble', ['Wisdom', 'Charisma'], ['Cure Wounds', 'Bless', 'Divine Favor'])

class Ranger(Class):
    def __init__(self):
        super().__init__('Ranger',
                        ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear', 'Battleaxe', 'Greatsword', 'Greataxe', 'Warhammer', 'Lance', 'Longsword'], ['Padded', 'Leather', 'Studded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Breastplate', 'Halfplate'],
                        ['Animal Handling', 'Athletics', 'Insight', 'Investigation', 'Nature', 'Perception', 'Stealth', 'Survival'],
                        ['Favored Enemy', 'Natural Explorer'], 10, '6d4', 'outlander', ['Strength', 'Dexterity'], ['Alarm', 'Fog Cloud', 'Longstrider'])

class Rogue(Class):
    def __init__(self):
        super().__init__('Rogue',
                        ['Crossbow, hand', 'Sap', 'Shortbow', 'Rapier', 'Sword, short', 'Club', 'Dagger', 'Javelin', 'Mace, light', 'Mace, heavy', 'Shortspear', 'Sickle', 
                         'Spear', 'Gauntlet, spiked', 'Greatclub', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Crossbow, repeating light', 'Crossbow, repeating heavy'], 
                        ['Padded', 'Leather', 'Studded Leather'],
                        ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Performace', 'Persuasion', 'Sleight of Hand', 'Survival'], 
                        ['Expertise', 'Sneak Attack', 'Theives\' Cant'], 8, '5d4', 'charlatan', ['Dexterity', 'Intelligence'], ['None'])

class Sorcerer(Class):
    def __init__(self):
        super().__init__('Sorcerer',
                        ['Dagger', 'Dart', 'Sling', 'Quarterstaff'], ['None'],
                        ['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion'], ['Sorcerous Origins', 'Font of Magic'], 6, '3d4',
                        'hermit', ['Constitution', 'Charisma'],
                        ['Light', 'Prestidigitation', 'Ray of Frost', 'Shocking Grasp', 'Shield', 'Magic Missle'])

class Warlock(Class):
    def __init__(self):
        super().__init__('Warlock',
                        ['Club', 'Longsword', 'Rapier', 'Shortbow', 'Dagger', 'Mace', 'Sickle', 'Quarterstaff', 'Spear', 'Crossbow, light', 'Dart', 'Sling'], ['Padded', 'Leather', 'Studded Leather'],
                        ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion'], ['Otherwordly Patron', 'Pact Magic'], 
                        8, '3d4', 'charlatan', ['Widsom', 'Charisma'],
                        ['Eldritch Blast', 'Chill Touch', 'Charm Person', 'Witch Bolt'])

class Wizard(Class):
    def __init__(self):
        super().__init__('Wizard',
                        ['Dagger', 'Dart', 'Sling', 'Quarterstaff', 'Crossbow, light'], ['None'],
                        ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion'], ['Arcane Recovery', 'Arcane Tradition'], 
                        6, '3d4', 'sage', ['Intelligence', 'Wisdom'],
                        ['Mage Hand', 'Light', 'Ray of Frost', 'Burning Hands', 'Charm Person', 'Mage Armor', 'Magic Missle', 'Sleep'])

# Base Character Traits
class Character:
    def __init__(self):
        
        self.data = Data()
        self.stats = self.RollStats
        self.race = self.data.PickRandomRace()
        self.cl = self.data.PickRandomClass()
        self.langs = list(set([choice(self.race.attributes.get('languages')) for i in range(randrange(0, len(self.race.attributes.get('languages'))))]))
        self.spells = list(set([choice(self.cl.spells) for i in range(randrange(0, len(self.cl.spells)))]))
        self.name = f'{self.race.firstName} {self.race.lastName}'
        self.info = self.data.PickRandomAttributes()
        self.coins = [randrange(0, 10), randrange(0, 6), randrange(0, 4)]
        self.favour = randrange(0, 100)
        self.saving_throw_values = [throw for throw in self.cl.saving_throws]

    @property
    def RollStats(self): 
        stats = { 'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 0, 'cha': 0 }
        
        totalStatNum = 0
        
        for stat in stats:
            newStat = randrange(0, 10)
            totalStatNum += newStat
            
            while totalStatNum > 30: 
                totalStatNum -= newStat
                newStat = randrange(0, 10)
                totalStatNum += newStat
            
            stats[stat] = newStat
            
        return stats

    @property
    def details(self):
        
        return f'''
Character Details
Name: {self.name}
Race: {self.race.race}
Class: {self.cl.type}
Age: {self.race.attributes.get('age')}
Height: {self.race.attributes.get('height')}
Weight: {self.race.attributes.get('weight')}
Size: {self.race.attributes.get('size')}
Speed: {self.race.attributes.get('speed')}
Trait(s): {StringifyArr(self.race.attributes.get('traits'))}
Language(s): {StringifyArr(self.langs) if self.langs != [] else 'Common'}
Spell(s): {StringifyArr(self.spells) if self.spells != [] else 'None'}
Saving Throw(s): {StringifyArr(self.saving_throw_values)}
Worships: {self.info.get('deity')}
Divine Favour: {self.favour}

Appearance
Hair: {self.info.get('hair_type')} {self.info.get('hair_color')}
Eye Color: {self.info.get('eye_color')}
Looks: {self.info.get('appearance')}
Talent: {self.info.get('talent')}
Mannerism: {self.info.get('mannerism')}

Commerce
Coins Held: {self.coins[2]} gold, {self.coins[1]} silver {self.coins[0]} copper

Exchange Rate
1 Gold = {self.data.exchangeRate[0]} Silver
1 Silver = {self.data.exchangeRate[1]} Copper
'''

    @property
    def __str__(self): return f'Character({self.name}, {self.race.race}, {self.cl.type})'

# Independent Functions 

def RollDice(diceNum:str='4d4', startPoint:int=0):

    for num in [randrange(1, int(diceNum.split('d')[1])) for die in range(int(diceNum.split('d')[0]))]: startPoint += num
    return startPoint

def isBool(strBool: str=''): return True if strBool == 'yes' or strBool == 'y' else False

def StringifyArr(arr=[]):

    arrString = ''
    for i, string in enumerate(arr):
        if len(arr)-1 == i: arrString += string
        else: arrString += f'{string}, '
    return arrString