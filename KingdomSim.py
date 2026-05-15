import random
import time
import pickle


#================================================== TUTORIAL =====================================================



# ================================================= STATS =======================================================

name = ("kingdom name")
play = ("menu")
strength = 3
maxstrength = 3
money = 1000000000000000000
day = 1
happiness = 50
people = 50
maxpeople = 50
next = ("awake")
exmoney = 5000
hpotion = 0
famount = 0
healed = 0
mode = ("0")
bread = 10

maximumPlayerdamage = 15
minimumPlayerdamage = 5
currentSword = ("None")

enemyHealthEASY = 100
minimumEnemydamageEASY = 2
maximumEnemydamageEASY = 7
enemyHealthMEDIUM = 200
minimumEnemydamageMEDIUM = 7
maximumEnemydamageMEDIUM = 12
enemyHealthHARD = 300
minimumEnemydamageHARD = 10
maximumEnemydamageHARD = 20

minimumEnemycoinsEASY = 50
maximumEnemycoinsEASY = 150
minimumEnemycoinsMEDIUM = 100
maximumEnemycoinsMEDIUM = 500
minimumEnemycoinsHARD = 150
maximumEnemycoinsHARD = 800

pmoney = 2

wfight = 0
lfight = 0

multiplier1 = 0
multiplier2 = 1
multiplier3 = random.randint(1,5)
multiplier4 = 0

bronze = 0
iron = 0
roman = 0
medievil = 0
electric = 0
modern = 0

log1 = ("")
log2 = ("")
log3 = ("")
log4 = ("")
log5 = ("")

#============ STONE AGE =============
itemlock1 = ("UNLOCKED")
itemlock2 = ("UNLOCKED")
itemlock3 = ("UNLOCKED")
itemlock4 = ("UNLOCKED")
itemlock5 = ("UNLOCKED")

#=========== BRONZE AGE =============
agelock1 = ("LOCKED")

itemlock6 = ("LOCKED")
itemlock7 = ("LOCKED")
itemlock8 = ("LOCKED")
itemlock9 = ("LOCKED")
itemlock10 = ("LOCKED")

#=========== IRON AGE =============
agelock2 = ("LOCKED")

itemlock11 = ("LOCKED")
itemlock12 = ("LOCKED")
itemlock13 = ("LOCKED")
itemlock14 = ("LOCKED")
itemlock15 = ("LOCKED")

#=========== ROMANS AGE =============
agelock3 = ("LOCKED")

itemlock16 = ("LOCKED")
itemlock17 = ("LOCKED")
itemlock18 = ("LOCKED")
itemlock19 = ("LOCKED")
itemlock20 = ("LOCKED")

#=========== MEDIEVIL AGE =============
agelock4 = ("LOCKED")

itemlock21 = ("LOCKED")
itemlock22 = ("LOCKED")
itemlock23 = ("LOCKED")
itemlock24 = ("LOCKED")
itemlock25 = ("LOCKED")

#=========== ELECTRIC AGE =============
agelock5 = ("LOCKED")

itemlock26 = ("LOCKED")
itemlock27 = ("LOCKED")
itemlock28 = ("LOCKED")
itemlock29 = ("LOCKED")
itemlock30 = ("LOCKED")

#=========== MODERN AGE =============
agelock6 = ("LOCKED")

itemlock31 = ("LOCKED")
itemlock32 = ("LOCKED")
itemlock33 = ("LOCKED")
itemlock34 = ("LOCKED")
itemlock35 = ("LOCKED")

number = -1
era = ["Bronze Age","Iron Age","Roman Age","Medievil Age","Electric Age","Modern Age"]

currentEra = ("Stone Age")

loop = 1

#============================================ HELPER FUNCTIONS ==================================================
def filler():
    print ("")
    print ("===============================================")
    print ("")


def filler2():
    for i in range(100):
        print ("")

# Centralized lock/stat unlock helper used by era progression.
def unlock_era(era_name, unlock_items, enemy_stats):
    for item in unlock_items:
        globals()[item] = "UNLOCKED"
    for stat, value in enemy_stats.items():
        globals()[stat] = value


SAVE_FIELDS = [
    "money", "exmoney", "day", "happiness", "people", "maxpeople", "hpotion", "bread",
    "maximumPlayerdamage", "minimumPlayerdamage", "wfight", "lfight", "currentSword",
    "itemlock1", "itemlock2", "itemlock3", "itemlock4", "itemlock5", "itemlock6", "itemlock7",
    "itemlock8", "itemlock10", "itemlock11", "itemlock12", "itemlock13", "itemlock14",
    "itemlock15", "itemlock16", "itemlock17", "itemlock18", "itemlock19", "itemlock20",
    "itemlock21", "itemlock22", "itemlock23", "itemlock24", "itemlock25", "itemlock26",
    "itemlock27", "itemlock28", "itemlock29", "itemlock30", "itemlock31", "itemlock32",
    "itemlock33", "itemlock34", "itemlock35", "name", "currentEra", "number"
]


# Save all persisted globals to .dat files.
def save_game_data():
    for field in SAVE_FIELDS:
        pickle.dump(globals()[field], open(f"{field}.dat", "wb"))
    # Keep legacy behavior intact: itemlock9.dat stores itemlock8.
    pickle.dump(itemlock8, open("itemlock9.dat", "wb"))


# Load all persisted globals from .dat files.
def load_game_data():
    for field in SAVE_FIELDS:
        globals()[field] = pickle.load(open(f"{field}.dat", "rb"))
    globals()["itemlock9"] = pickle.load(open("itemlock9.dat", "rb"))



ERA_NAMES = ["Stone Age", "Bronze Age", "Iron Age", "Roman Age", "Medievil Age", "Electric Age", "Modern Age"]
CURRENT_ERA_INDEX = {name: i for i, name in enumerate(ERA_NAMES)}

WEAPONS = [
    ("Pebble", 1000, 2, 0),("Stone", 5000, 5, 0),("Rock", 7500, 7, 0),("Chissled Stone", 12000, 12, 0),("Sharpened Rock", 16000, 15, 0),
    ("Socketed Axe", 30000, 17, 1),("Dagger", 45000, 20, 1),("Sickle Sword", 60000, 24, 1),("Reinforced Axe", 90000, 27, 1),("Dead Oak Bow", 120000, 30, 1),
    ("Iron Spear", 165000, 34, 2),("Steel Sword", 200000, 37, 2),("Lance", 220000, 40, 2),("Axe", 235000, 43, 2),("Bow", 260000, 46, 2),
    ("Pugio", 350000, 50, 3),("Gladius", 385000, 54, 3),("Spatha", 400000, 57, 3),("Javelin", 435000, 60, 3),("Falx", 495000, 64, 3),
    ("Lance MkII", 515000, 68, 4),("Mace", 545000, 72, 4),("Crossbow", 600000, 76, 4),("Tribuchet", 630000, 79, 4),("Longbow", 675000, 83, 4),
    ("Fire Lance", 735000, 87, 5),("Proto-gun", 795000, 91, 5),("Gattling Gun", 850000, 95, 5),("Flintlock", 900000, 99, 5),("Revolver", 975000, 104, 5),
    ("Glock", 1045000, 109, 6),("Uzi", 1100000, 114, 6),("Maxim Gun", 1150000, 119, 6),("AK-47", 1200000, 124, 6),("M1 Garand", 1300000, 130, 6),
]

FOOD_BY_ERA = ["Foraged Berries", "Grain Sack", "Smoked Meat", "Olive Basket", "Royal Rations", "Canned Crate", "Nutrition Pack"]
POTION_BY_ERA = ["Herbal Poultice", "Copper Tonic", "Iron Elixir", "Roman Remedy", "Knight's Draught", "Voltage Vial", "Nano Medkit"]

def era_price(base_price):
    return base_price * (CURRENT_ERA_INDEX.get(currentEra, 0) + 1)

def buy_scaling_item(label, base_price, stock_var):
    global money
    price = era_price(base_price)
    filler()
    print(f"1: {label} ({price} Coins)")
    print("")
    choice = input("Number: ")
    if choice != "1":
        return
    amount = int(input("Quantity: "))
    total = price * amount
    if money < total:
        print("You do not have enough Coins to purchase this item")
        return
    money -= total
    globals()[stock_var] += amount
    print(f"You have successfully purchased {amount} {label}!")

def show_weapons_and_buy():
    global money, minimumPlayerdamage, maximumPlayerdamage, currentSword
    current_era = CURRENT_ERA_INDEX.get(currentEra, 0)
    equipped_idx = next((i for i, w in enumerate(WEAPONS) if w[0] in currentSword), -1)
    filler()
    print("================ Weapons ================")
    for i, (name, price, dmg, era_idx) in enumerate(WEAPONS, start=1):
        if era_idx > current_era:
            continue
        status = "LOCKED" if i - 1 <= equipped_idx else "UNLOCKED"
        print(f"{i}: {name:<22} ({price:,} Coins) ({status})")
    item = input("Number: ")
    if not item.isdigit():
        return
    idx = int(item) - 1
    if idx < 0 or idx >= len(WEAPONS):
        return
    name, price, dmg, era_idx = WEAPONS[idx]
    if era_idx > current_era:
        print("That weapon has not been unlocked for your era.")
        return
    if idx <= equipped_idx:
        print("That weapon is locked because it is weaker than your equipped weapon.")
        return
    if money < price:
        print("You do not have enough Coins to purchase this item")
        return
    if input("Confirm (yes/no): ") != "yes":
        return
    money -= price
    minimumPlayerdamage = 5 + dmg
    maximumPlayerdamage = 15 + dmg
    currentSword = f"{name} (+{dmg} Damage)"
    print(f"You have successfully purchased 1 {name}!")

KINGDOM_SIMULATOR_ART = r"""
 _   ___                 _                   _____ _                 _       _
| | / (_)               | |                 /  ___(_)               | |     | |
| |/ / _ _ __   __ _  __| | ___  _ __ ___   \ `--. _ _ __ ___  _   _| | __ _| |_ ___  _ __
|    \| | '_ \ / _` |/ _` |/ _ \| '_ ` _ \   `--. \ | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
| |\  \ | | | | (_| | (_| | (_) | | | | | | /\__/ / | | | | | | |_| | | (_| | || (_) | |
\_| \_/_|_| |_|\__, |\__,_|\___/|_| |_| |_| \____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|
                  __/ |
                 |___/
"""

ENEMY_ART = r"""
 ____  __ _  ____  _  _  _  _
(  __)(  ( \(  __)( \/ )( \/ )
 ) _) /    / ) _) / \/ \ )  /
(____)\_)__)(____)\_)(_/(__/
"""

YOU_ART = r"""
 _  _  __   _  _
( \/ )/  \ / )( \
 )  /(  O )) \/ (
(__/  \__/ \____/
"""

ASCII_DIGITS = {
    "0": [" ___ ", "/ _ \\", ") _ (", "\\___/"],
    "1": ["  _  ","/_ ( "," ) | ","/__( "],
    "2": [" ___ ", "/__ (", " ( / ", "/___\\"],
    "3": [" ___ ", "(__ \\", " (_ |", "(___/"],
    "4": [" _  _", ") () (", " \\_  |", "   )_("],
    "5": ["  ___ ", " ) __\\", " '- ) ", " )___\\"],
    "6": [" _    ", ") |_  ", "| ( \\", "\\___/"],
    "7": [" ___ ", "\\_  (", "  / |", "  )_("],
    "8": [" ___ ", "/ _ \\", ") _ (", "\\___/"],
    "9": [" ___ ", "/ _ \\", "`-_((", "  )_/"],
}
ASCII_PLUS = [
    "      ",
    " _ _  ",
    "(_|_) ",
    "  |   ",
]
ASCII_MINUS = [
    "      ",
    "      ",
    " _____",
    "      ",
]

def render_ascii_number(value):
    value_str = str(abs(int(value)))
    lines = ["" for _ in range(4)]
    for ch in value_str:
        glyph = ASCII_DIGITS.get(ch, ASCII_DIGITS["0"])
        for i in range(4):
            lines[i] += glyph[i] + "  "
    return "\n".join(lines)

def render_ascii_delta(value):
    sign = ASCII_PLUS if value >= 0 else ASCII_MINUS
    num = render_ascii_number(value)
    sign_text = "\n".join(sign)
    return f"{sign_text}\n{num}"

#============================================== DISPLAY FUNCTIONS =================================================
def data():
    print ("Type [cmds] in the command box for list of commands")
    print ("")
    print ("============= Stats ============")
    print ("")
    print ("Age:              ",currentEra)
    print ("")
    print ("Day:              ",day)
    print ("")
    print ("Money:            ",money,"Coins")
    print ("")
    print ("Population:       ",people)
    print ("")
    print ("Max Population:   ",maxpeople)
    print ("")
    print ("Happiness:        ",happiness)
    print ("")
    print ("Food:             ",bread)
    print ("")
    print ("Sword:            ",currentSword)
    print ("")
    print ("================================")
    print ("")
    print ("Fights Won:   ", wfight)
    print ("")
    print ("Fights Lost:  ", lfight)
    print ("")
    print ("Logs:")
    print (log1)
    print (log2)
    print (log3)
    print (log4)
    print (log5)
    filler()


def stats():
    print ("=========== INFO ===========")
    print (ENEMY_ART)
    print ("Enemy Health:")
    print(render_ascii_number(ehealth))
    print (YOU_ART)
    print ("Your Health:")
    print(render_ascii_number(phealth))
    print ("============================")
    print ("")


def turn():
    print ("============ Your Turn ===========")
    print ("                                 |")
    print ("1: Strike                        |")
    print ("2: Block                         |")
    print ("3: Heal (",hpotion,"Potions Left)        |")
    print ("                                 |")
    print ("======== Type the number ========")
    print ("")


def modes():
    print ("")
    print ("============= Modes =============")
    print ("                                |")
    print ("1: Easy                         |")
    print ("                                |")
    print ("2: Medium                       |")
    print ("                                |")
    print ("3: Hard                         |")
    print ("                                |")
    print ("======== Type the number ========")
    print ("")


def shop():
    print ("")
    print ("========== Catagories ===========")
    print ("                                |")
    print ("1: Potions                      |")
    print ("2: Food                         |")
    print ("3: Weapons                      |")
    print ("                                |")
    print ("======== Type the number ========")
    print ("Type (exit) to close the shop")
    print ("")


def inv():
    print ("")
    print ("======== Inventory ========")
    print ("")
    print (hpotion, "x - Health Potions")
    filler()

#================================================== OPTIONS ======================================================


#============================================== GAME OPTIONS ====================================================

while loop == 1:
    while play == ("menu"):
        filler2()
        filler()
        print ("============ Main Menu =============")
        print ("")
        print ("1: New game")
        print ("2: Load last save")
        print ("")
        print ("========= Type The Number ==========")
        print ("")
        cmd = input("Command: ")
        if cmd == ("1"):
            filler2()
            time.sleep(1)
            print ("")
            print(KINGDOM_SIMULATOR_ART)
            print ("Welcome to Kingdom Simulator! Here you will have to manage your own kingdom by expanding your population, fighting for coins, buying items, and MORE!")
            print ("")
            time.sleep(1)
            print ("To get started, type your Kingdom name. You can call it anything you want!")
            print ("")
            time.sleep(1)
            print ("==================================================")
            print ("")
            name = input("Kingdom Name: ")
            print ("")
            time.sleep(1)
            print (name, "it is! To get a list of all the commands, type [cmds] in the command box")
            print ("==================================================")
            print ("")
            print ("Please be patient. This may take a few moments")
            print ("")
            print ("==================================================")
            time.sleep(2)
            play = ("playing")
            break

        if cmd == ("2"):
            filler()
            print ("Are you sure? Yes / No")
            print ("")
            cmd = input("Command: ")
            if cmd == ("yes"):
                print ("Loading saved data...")
                time.sleep(1)
                print ("Please wait a few seconds for the game to load (BETA)")
                time.sleep(2)

                load_game_data()
                
                
                print ("")
                print ("Game loaded")
                filler()
                time.sleep(2)
                play = ("playing")
                break

    #=============================================== GAME START =====================================================
    filler2()
    while play == ("playing"):
        if next == ("awake"):
            protest = random.randint(0,20)
            if protest == 2:
                log2 = ("Your people have started a protest for you to pay them!")
                filler()
                pmoney = 0

            print ("")
            data()
            cmd = input("Command: ")
            filler2()
            if pmoney == 0:
                if cmd == ("pay"):
                    filler()
                    pmoney = pmoney + 1
                    log2 = ("The protest has stopped. This doesn't mean they won't do it again!")
                    filler()
                    
                if pmoney == 0:
                    leave = random.randint(5,15)
                    people = people - leave
                    filler()
                    log2 = (leave, "people have left your Kingdom beacuase you did not pay them!")
    #================================================ CHECKERS ============================================================
            if happiness < 1:
                    print ("Your people are not happy. They left your Kingdom and you soon became broke")
                    money = 0
                    break
    #================================================== CMDS ===============================================================
            if cmd == ("cmds"):
                filler()
                print ("======================== COMMANDS =========================")
                print ("                                                          |")
                print ("1: (Sleep) To end the day                                 |")
                print ("                                                          |")
                print ("2: (Tax) To gain money from your people                   |")
                print ("                                                          |")
                print ("3: (Pay) To pay money to your people                      |")
                print ("                                                          |")
                print ("4: (Expand) Increase your max population size             |")
                print ("                                                          |")
                print ("5: (Fight) Fight enemies for extra coins                  |")
                print ("                                                          |")
                print ("6: (Stats) See your progress                              |")
                print ("                                                          |")
                print ("7: (Inv) See whats in your inventory                      |")
                print ("                                                          |")
                print ("8: (Shop) Buy items to help you fight or feed your people |")
                print ("                                                          |")
                print ("9: (Expand) Go up in Era's to gain better weapons         |")
                print ("                                                          |")
                print ("10: (Save) Save Your game progress                        |")
                print ("                                                          |")
                print ("===========================================================")
                

    #=================================================== SLEEP ==============================================================
            if cmd == ("sleep"):
                next = ("sleep")
                strength = maxstrength
                log5 = ("Your Strength has been restored: ", strength, "Strength Left")

    #==================================================== TAX ===============================================================
            if cmd.lower() == "tax":
                if happiness < 1:
                    print("Your people are not happy. They left your Kingdom and you soon became broke")
                    money = 0
                    break
                else:
                    multiplier3 = random.randint(1, 5)
                    happiness -= multiplier3
                    money += random.randint(25, 50)
                    log2 = ("You have taxed the people but they were not happy: -", multiplier3, "Happiness")
                    strength -= 1
                    log1 = ("Your Strength has gone down: ", strength, "Strength Left")
    #====================================================== PAY =============================================================
            if cmd == ("pay"):
                if people < 1:
                   print ("You have no-one left in", name,". You quickly became broke and unpopular")
                   people = 0
                   money = 0
                   break
                else:
                    money -= 5
                    happiness += 5
                    strength -= 1
                    log5 = ("Your Strength has gone down: ", strength, "Strength Left")

            if cmd == ("Pay"):
                if people < 1:
                   print ("You have no-one left in", name,". You quickly became brokeand unpopular")
                   people = 0
                   money = 0
                   break
                else:
                    money -= 5
                    happiness += 5
                    strength -= 1
                    log5 = ("Your Strength has gone down: ", strength, "Strength Left")

    #===================================================== EXPAND =======================================================
            if cmd == "expand" and number <= 6:
                if money > exmoney:
                    money -= exmoney
                    filler()
                    multiplier2 += 1
                    maxpeople *= multiplier2
                    exmoney *= 2
                    maxstrength = 4
                    number += 1
                    currentEra = era[number]
                    print(f"You are now {currentEra} and can now have up to {maxpeople} people in {name} Kingdom")
                    strength -= 1
                    log5 = f"Your Strength has gone down: {strength} Strength Left"
                    unlock_data = {
                        "Bronze Age": (
                            ["bronze", "agelock1", "itemlock6", "itemlock7", "itemlock8", "itemlock9", "itemlock10"],
                            {"enemyHealthEASY": 200, "minimumEnemydamageEASY": 5, "maximumEnemydamageEASY": 10, "enemyHealthMEDIUM": 300, "minimumEnemydamageMEDIUM": 7, "maximumEnemydamageMEDIUM": 15, "enemyHealthHARD": 400, "minimumEnemydamageHARD": 15, "maximumEnemydamageHARD": 25, "minimumEnemycoinsHARD": 300, "maximumEnemycoinsHARD": 1200, "minimumEnemycoinsMEDIUM": 200, "maximumEnemycoinsMEDIUM": 700, "minimumEnemycoinsEASY": 100, "maximumEnemycoinsEASY": 500}
                        ),
                        "Iron Age": (
                            ["agelock2", "itemlock11", "itemlock12", "itemlock13", "itemlock14", "itemlock15"],
                            {"enemyHealthEASY": 300, "minimumEnemydamageEASY": 7, "maximumEnemydamageEASY": 15, "enemyHealthMEDIUM": 400, "minimumEnemydamageMEDIUM": 12, "maximumEnemydamageMEDIUM": 18, "enemyHealthHARD": 600, "minimumEnemydamageHARD": 15, "maximumEnemydamageHARD": 30, "minimumEnemycoinsHARD": 600, "maximumEnemycoinsHARD": 1700, "minimumEnemycoinsMEDIUM": 500, "maximumEnemycoinsMEDIUM": 900, "minimumEnemycoinsEASY": 300, "maximumEnemycoinsEASY": 800}
                        ),
                        "Roman Age": (
                            ["agelock3", "itemlock16", "itemlock17", "itemlock18", "itemlock19", "itemlock20"],
                            {"minimumEnemydamageEASY": 12, "maximumEnemydamageEASY": 18, "minimumEnemydamageMEDIUM": 15, "maximumEnemydamageMEDIUM": 25, "minimumEnemydamageHARD": 20, "maximumEnemydamageHARD": 40, "minimumEnemycoinsHARD": 1200, "maximumEnemycoinsHARD": 2000, "minimumEnemycoinsMEDIUM": 800, "maximumEnemycoinsMEDIUM": 1100, "minimumEnemycoinsEASY": 600, "maximumEnemycoinsEASY": 1000}
                        ),
                        "Medievil Age": (
                            ["agelock4", "itemlock21", "itemlock22", "itemlock23", "itemlock24", "itemlock25"],
                            {"minimumEnemydamageEASY": 15, "maximumEnemydamageEASY": 25, "minimumEnemydamageMEDIUM": 20, "maximumEnemydamageMEDIUM": 30, "minimumEnemydamageHARD": 25, "maximumEnemydamageHARD": 45, "minimumEnemycoinsHARD": 2000, "maximumEnemycoinsHARD": 4000, "minimumEnemycoinsMEDIUM": 1500, "maximumEnemycoinsMEDIUM": 2000, "minimumEnemycoinsEASY": 1000, "maximumEnemycoinsEASY": 1400}
                        ),
                        "Electric Age": (
                            ["agelock5", "itemlock26", "itemlock27", "itemlock28", "itemlock29", "itemlock30"],
                            {"minimumEnemydamageEASY": 20, "maximumEnemydamageEASY": 30, "minimumEnemydamageMEDIUM": 25, "maximumEnemydamageMEDIUM": 37, "minimumEnemydamageHARD": 30, "maximumEnemydamageHARD": 55, "minimumEnemycoinsHARD": 8000, "maximumEnemycoinsHARD": 10000, "minimumEnemycoinsMEDIUM": 4500, "maximumEnemycoinsMEDIUM": 7000, "minimumEnemycoinsEASY": 2000, "maximumEnemycoinsEASY": 3000}
                        ),
                        "Modern Age": (
                            ["agelock6", "itemlock31", "itemlock32", "itemlock33", "itemlock34", "itemlock35"],
                            {"minimumEnemydamageEASY": 25, "maximumEnemydamageEASY": 37, "minimumEnemydamageMEDIUM": 30, "maximumEnemydamageMEDIUM": 45, "minimumEnemydamageHARD": 35, "maximumEnemydamageHARD": 60, "minimumEnemycoinsHARD": 20000, "maximumEnemycoinsHARD": 50000, "minimumEnemycoinsMEDIUM": 10000, "maximumEnemycoinsMEDIUM": 15000, "minimumEnemycoinsEASY": 5000, "maximumEnemycoinsEASY": 9000}
                        )
                    }
                    if currentEra in unlock_data:
                        unlock_era(currentEra, *unlock_data[currentEra])
                else:
                    amount = exmoney - money
                    print(f"You do not have the required amount of Coins. You need {amount} Coins to expand")
                    time.sleep(2)
            elif number > 6:
                filler()
                print("You are already at the top Age")
                filler()
                time.sleep(2)

    #==================================================== SHOP =========================================================

            if cmd == ("shop"):
                while cmd == ("shop"):
                    shop()
                    spage = input("Page Number: ")
                    if spage == ("1"):
                        buy_scaling_item(POTION_BY_ERA[CURRENT_ERA_INDEX.get(currentEra, 0)], 500, "hpotion")
                    if spage == ("2"):
                        buy_scaling_item(FOOD_BY_ERA[CURRENT_ERA_INDEX.get(currentEra, 0)], 20, "bread")
                    if spage == ("3"):
                        show_weapons_and_buy()
                    if spage == ("exit"):
                        print("You have closed the shop")
                        break

            if cmd == ("fight"):
                strength = 0
                modes()
                mode = input("1, 2 or 3: ")
                filler2()
                if mode == ("1"):
                    #=================== ENEMY STATS ====================
                    ehealth = enemyHealthEASY
                    edamage = 0
                    eblock = 0
                    enemy = 1
                    #================== PLAYER STATS ====================
                    phealth = 100
                    pdamage = 0
                    eblock = 0
                    #====================================================
                    while ehealth > 0:
                        if phealth < 1:
                            break
                        filler()
                        stats()
                        turn()
                        cmd = input("Fight: ")
                        filler()
                        enemy = random.randint(1,2)
                        if cmd == ("1"):
                            filler2()
                            pdamage = random.randint(minimumPlayerdamage,maximumPlayerdamage)
                            if enemy == 1:
                                ehealth = ehealth - pdamage
                                edamage = random.randint(minimumEnemydamageEASY,maximumEnemydamageEASY)
                                phealth = phealth - edamage
                                print("You dealt:")
                                print(render_ascii_delta(-pdamage))
                                print("Enemy dealt:")
                                print(render_ascii_delta(-edamage))
                            if enemy == 2:
                                eblock = random.randint(5,15)# Tuning note: adjust only these numeric ranges to rebalance combat.
                                pdamage = pdamage - eblock
                                if pdamage < 1:
                                    print ("The enemy blocked your attack! You did 0 damage")
                                elif pdamage > 1:
                                    ehealth = ehealth - pdamage
                                    print ("The enemy blocked your attack! You did", pdamage, "damage")
                        if cmd == ("2"):
                            filler2()
                            pblock = random.randint(10,30)
                            if enemy == 2:
                                print ("The enemy did not attack! You did not get hurt")
                            if enemy == 1:
                                edamage = random.randint(minimumEnemydamageEASY,maximumEnemydamageEASY)
                                if edamage >= 0:
                                    edamage = edamage - pblock
                                    phealth = phealth - edamage
                                    print ("Enemy dealt:")
                                    print(render_ascii_delta(-edamage))
                                if edamage < 1:
                                    edamage = edamage - pblock
                                    phealth = phealth + edamage
                                    print ("Enemy dealt:")
                                    print(render_ascii_delta(-edamage))
                        if cmd == ("3"):
                            filler2()
                            if phealth >= 1:
                                if hpotion > 0:
                                    phealth = 100
                                    print ("You have healed yourself!")
                                    hpotion = hpotion - 1
                                    print ("You have used 1 Health potion. Only",hpotion, "are left")
                            if hpotion == 0:
                                print ("")
                                edamage = random.randint(minimumEnemydamageEASY,maximumEnemydamageEASY)
                                phealth = phealth - edamage
                                print ("You do not have any health potions to use! Enemy dealt:")
                                print(render_ascii_delta(-edamage))

                if mode == ("2"):
                    #=================== ENEMY STATS ====================
                    ehealth = enemyHealthMEDIUM
                    edamage = 0
                    eblock = 0
                    enemy = 1
                    #================== PLAYER STATS ====================
                    phealth = 100
                    pdamage = 0
                    eblock = 0
                    #====================================================
                    while ehealth > 0:
                        if phealth < 1:
                            break
                        filler()
                        stats()
                        turn()
                        cmd = input("Fight: ")
                        filler()
                        enemy = random.randint(1,2)
                        if cmd == ("1"):
                            filler2()
                            pdamage = random.randint(minimumPlayerdamage,maximumPlayerdamage)
                            if enemy == 1:
                                ehealth = ehealth - pdamage
                                edamage = random.randint(minimumEnemydamageMEDIUM,maximumEnemydamageMEDIUM)# Tuning note: adjust only these numeric ranges to rebalance combat.
                                phealth = phealth - edamage
                                print("You dealt:")
                                print(render_ascii_delta(-pdamage))
                                print("Enemy dealt:")
                                print(render_ascii_delta(-edamage))
                            if enemy == 2:
                                eblock = random.randint(10,20)# Tuning note: adjust only these numeric ranges to rebalance combat.
                                pdamage = pdamage - eblock
                                if pdamage < 1:
                                    print ("The enemy blocked your attack! You did 0 damage")
                                elif pdamage > 1:
                                    ehealth = ehealth - pdamage
                                    print ("The enemy blocked your attack! You did", pdamage, "damage")
                        if cmd == ("2"):
                            filler2()
                            pblock = random.randint(10,30)
                            if enemy == 2:
                                print ("The enemy did not attack! You did not get hurt")
                            if enemy == 1:
                                edamage = random.randint(minimumEnemydamageMEDIUM,maximumEnemydamageMEDIUM)# Tuning note: adjust only these numeric ranges to rebalance combat.
                                if edamage >= 0:
                                    edamage = edamage - pblock
                                    phealth = phealth - edamage
                                    print ("Enemy dealt:")
                                    print(render_ascii_delta(-edamage))
                                if edamage < 1:
                                    edamage = edamage - pblock
                                    phealth = phealth + edamage
                                    print ("Enemy dealt:")
                                    print(render_ascii_delta(-edamage))
                        if cmd == ("3"):
                            filler2()
                            if phealth >= 1:
                                if hpotion > 0:
                                    phealth = 100
                                    print ("You have healed yourself!")
                                    hpotion = hpotion - 1
                                    print ("You have used 1 Health potion. Only",hpotion, "are left")
                            if hpotion == 0:
                                print ("")
                                edamage = random.randint(minimumEnemydamageMEDIUM,maximumEnemydamageMEDIUM)# Tuning note: adjust only these numeric ranges to rebalance combat.
                                phealth = phealth - edamage
                                print ("You do not have any health potions to use! Enemy dealt:")
                                print(render_ascii_delta(-edamage))

                if mode == ("3"):
                    #=================== ENEMY STATS ====================
                    ehealth = enemyHealthHARD
                    edamage = 0
                    eblock = 0
                    enemy = 1
                    #================== PLAYER STATS ====================
                    phealth = 100
                    pdamage = 0
                    eblock = 0
                    #====================================================
                    while ehealth > 0:
                        if phealth < 1:
                            break
                        filler()
                        stats()
                        turn()
                        cmd = input("Fight: ")
                        filler()
                        enemy = random.randint(1,2)
                        if cmd == ("1"):
                            filler2()
                            pdamage = random.randint(minimumPlayerdamage,maximumPlayerdamage)
                            if enemy == 1:
                                ehealth = ehealth - pdamage
                                edamage = random.randint(minimumEnemydamageHARD,maximumEnemydamageHARD)# Tuning note: adjust only these numeric ranges to rebalance combat.
                                phealth = phealth - edamage
                                print("You dealt:")
                                print(render_ascii_delta(-pdamage))
                                print("Enemy dealt:")
                                print(render_ascii_delta(-edamage))
                            if enemy == 2:
                                eblock = random.randint(15,25)# Tuning note: adjust only these numeric ranges to rebalance combat.
                                pdamage = pdamage - eblock
                                if pdamage < 1:
                                    print ("The enemy blocked your attack! You did 0 damage")
                                elif pdamage > 1:
                                    ehealth = ehealth - pdamage
                                    print ("The enemy blocked your attack! You did", pdamage, "damage")
                        if cmd == ("2"):
                            filler2()
                            pblock = random.randint(10,30)
                            if enemy == 2:
                                print ("The enemy did not attack! You did not get hurt")
                            if enemy == 1:
                                edamage = random.randint(minimumEnemydamageHARD,maximumEnemydamageHARD)# Tuning note: adjust only these numeric ranges to rebalance combat.
                                if edamage >= 0:
                                    edamage = edamage - pblock
                                    phealth = phealth - edamage
                                    print ("Enemy dealt:")
                                    print(render_ascii_delta(-edamage))
                                if edamage < 1:
                                    edamage = edamage - pblock
                                    phealth = phealth + edamage
                                    print ("Enemy dealt:")
                                    print(render_ascii_delta(-edamage))
                        if cmd == ("3"):
                            filler2()
                            if phealth >= 1:
                                if hpotion > 0:
                                    phealth = 100
                                    print ("You have healed yourself!")
                                    hpotion = hpotion - 1
                                    print ("You have used 1 Health potion. Only",hpotion, "are left")
                            if hpotion == 0:
                                print ("")
                                edamage = random.randint(minimumEnemydamageHARD,maximumEnemydamageHARD)# Tuning note: adjust only these numeric ranges to rebalance combat.
                                phealth = phealth - edamage
                                print ("You do not have any health potions to use! Enemy dealt:")
                                print(render_ascii_delta(-edamage))
                    
        
    #====================================================================================================================
            if mode == ("1"):
                if ehealth < 1:
                    ehealth = 100
                    famount = random.randint(minimumEnemycoinsEASY,maximumEnemycoinsEASY)
                    money = money + famount
                    print("You defeated the enemy in EASY mode! You have earned", famount, "Coins")
                    filler()
                    wfight += 1
                if phealth < 1:
                    phealth = 100
                    print ("You are too injured to carry on fighting. You retreated back to", name, "Kingdom")
                    filler()
                    lfight += 1
                    
            if mode == ("2"):
                if ehealth < 1:
                    ehealth = 100
                    famount = random.randint(minimumEnemycoinsMEDIUM,maximumEnemycoinsMEDIUM)
                    money = money + famount
                    print("You defeated the enemy in MEDIUM mode! You have earned", famount, "Coins")
                    filler()
                    wfight += 1
                if phealth < 1:
                    phealth = 100
                    print ("You are too injured to carry on fighting. You retreated back to", name, "Kingdom")
                    filler()
                    lfight += 1

            if mode == ("3"):
                if ehealth < 1:
                    ehealth = 100
                    famount = random.randint(minimumEnemycoinsHARD,maximumEnemycoinsHARD)
                    money = money + famount
                    print("You defeated the enemy in HARD mode! You have earned", famount, "Coins")
                    filler()
                    wfight += 1
                if phealth < 1:
                    phealth = 100
                    print ("You are too injured to carry on fighting. You retreated back to", name, "Kingdom")
                    filler()
                    lfight += 1

            if strength == 0:
                if people < 1:
                   print ("You have no-one left in", name,". You quickly became broke and unpopular")
                   people = 0
                   money = 0
                   play = ("menu")
                   break
                elif happiness < 1:
                    print ("Your people are not happy. They left your Kingdom and you soon became broke")
                    money = 0
                    play = ("menu")
                    break
                else:
                    print ("You are too tired. You went to sleep")
                    next = ("sleep")
                    if bread < people:
                        filler()
                        print ("You have lost 1 Person in your Kingdom. You need to buy more food!")
                        people = people - 1
                        filler()

                    if happiness < 15:
                        filler()
                        print ("You are losing people! Make them happy buy either buying food or giving them money")
                        people = people - 1
                        filler()
    #====================================================================================================================
        if next == ("sleep"):
            strength = maxstrength
            day = day + 1
            bread = bread - 1
            happiness = happiness - 1
            next = ("awake")
        
            if people > bread:
                randompeople = random.randint(1,10)
                log3 = ("You have lost",randompeople,"people in your Kingdom. You need to buy more food!")
                people = people - randompeople

            if happiness < 15:
                log3 = ("You are losing people! Make them happy buy either buying food or giving them money")
                people = people - 1
            leftpeople = maxpeople - people
            
            if maxpeople > people:
                addpeople = random.randint(1,leftpeople)
                people = people + addpeople
                log4 = (addpeople,"people have decided to join your Kingdom!")

        if cmd == ("save"):
            filler2()
            print ("Saving...")
            filler()
            save_game_data()

            time.sleep(1)
            filler2()
            print ("")
            print ("Game has been saved")
            filler()
            time.sleep(2)
            filler2()
            #data()
            
            
            print ("")
            print ("Game loaded")
            filler()

        if cmd == ("cheat"):
            if currentSword == ("Blunt Sword (+15 Damage)"):
                print ("How would you like to cheat?")
                print ("1: Give Money")
                print ("2: Give Health Potions")
                print ("3: Set Damage")
                cheat = input("Command: ")
                cheat = int(cheat)
                if cheat >= 1:
                    print ("Not in service yet!")



        if day == random.randint(40,75):
            print ("You have died from unknown causes")
            break
        if bread < 0:
            print ("You have ran out of food")
        if bread <= -1:
            print ("You have ran out of food")
            bread = 0
        if people > maxpeople:
            print("You have found a bug! You have managed to get more people than you are allowed. This game has now ended.")
            break
        if money < 1:
            print("You have no money left. You can ethier Tax your people OR fight your enemies to steal their Coins")

        if cmd == ("menu"):
            filler()
            print ("Would you like to save before quitting to the main menu? Yes/No")
            print ("")
            cmd = input("Command: ")
            if cmd == ("no"):
                filler()
                print ("All progress will be lost")
                time.sleep(2)
                filler2()
                play = ("menu")
                break
            if cmd == ("yes"):
                filler2()
                filler()
                print ("Saving all current progress")
                filler()
                time.sleep(2)
                save_game_data()
                play = ("menu")
                break

#======================================================= RANDOM ACTS =================================================

    

#======================================================== GAME END ===================================================


print("============Your Score============")
data()
