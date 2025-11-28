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

item_locks = ["UNLOCKED"] * 5 + ["LOCKED"] * 30
age_locks = ["LOCKED"] * 6

number = -1
era = ["Bronze Age","Iron Age","Roman Age","Medievil Age","Electric Age","Modern Age"]

currentEra = ("Stone Age")

loop = 1

#===============================================  FUNCTIONS =====================================================
def filler():
    print ("")
    print ("===============================================")
    print ("")

def filler2():
    for i in range(100):
        print ("")

    

def stats():
    print ("=========== INFO ===========")
    print ("")
    print ("Your Health:    ",phealth)
    print ("")
    print ("Enemys Health:  ",ehealth)
    print ("")
    print ("============================")
    print ("")

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
    
def set_item_locks(indices, value="UNLOCKED"):
    for index in indices:
        item_locks[index] = value


def unlock_era(unlock_items, enemy_stats, age_index=None, bronze_unlock=False):
    global bronze
    if age_index is not None:
        age_locks[age_index] = "UNLOCKED"
    if bronze_unlock:
        bronze = 1
    set_item_locks(unlock_items)
    for stat, value in enemy_stats.items():
        globals()[stat] = value


state_file_pairs = [
    ("money", "money.dat"),
    ("exmoney", "exmoney.dat"),
    ("day", "day.dat"),
    ("happiness", "happiness.dat"),
    ("people", "people.dat"),
    ("maxpeople", "maxpeople.dat"),
    ("hpotion", "hpotion.dat"),
    ("bread", "bread.dat"),
    ("maximumPlayerdamage", "maximumPlayerdamage.dat"),
    ("minimumPlayerdamage", "minimumPlayerdamage.dat"),
    ("wfight", "wfight.dat"),
    ("lfight", "lfight.dat"),
    ("currentSword", "currentSword.dat"),
    ("name", "name.dat"),
    ("number", "number.dat"),
    ("currentEra", "currentEra.dat"),
]

item_lock_files = [f"itemlock{i}.dat" for i in range(1, 36)]
item_lock_save_map = [0, 1, 2, 3, 4, 5, 6, 7, 7] + list(range(9, 35))


def load_game_state():
    for var, filename in state_file_pairs:
        globals()[var] = pickle.load(open(filename, "rb"))
    for index, filename in enumerate(item_lock_files):
        item_locks[index] = pickle.load(open(filename, "rb"))


def save_game_state():
    for var, filename in state_file_pairs:
        pickle.dump(globals()[var], open(filename, "wb"))
    for index, filename in enumerate(item_lock_files):
        pickle.dump(item_locks[item_lock_save_map[index]], open(filename, "wb"))

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

                load_game_state()
                
                
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
            '''if cmd == ("tax"):
                if happiness < 1:
                    print ("Your people are not happy. They left your Kingdom and you soon became broke")
                    money = 0
                    break
                else:
                    multiplier3 = random.randint(1,5)
                    happiness -= multiplier3
                    money += random.randint(25,50)
                    log2 = ("You have taxed the people but they were not happy: -", multiplier3, "Happiness")
                    strength -= 1
                    log1 = ("Your Strength has gone down: ", strength, "Strength Left")
                    
            if cmd == ("Tax"):
                if happiness < 1:
                    print ("Your people are not happy. They left your Kingdom and you soon became broke")
                    money = 0
                    break
                else:
                    multiplier3 = random.randint(1,5)
                    happiness -= multiplier3
                    money += random.randint(25,50)
                    log2 = ("You have taxed the people but they were not happy: -", multiplier3, "Happiness")
                    strength -= 1
                    log2 = ("Your Strength has gone down: ", strength, "Strength Left")'''
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
            '''if cmd == ("expand"):
                if number <= 6:
                    if money > exmoney:
                        money = money - exmoney
                        filler()
                        multiplier2 += 1
                        maxpeople = maxpeople * multiplier2
                        exmoney = exmoney * 2
                        maxstrength = 4
                        number = number + 1
                        currentEra = era[number]
                        print ("You are now",currentEra,"and can now have up to", maxpeople, "people in", name, "Kingdom")
                        strength -= 1
                        log5 = ("Your Strength has gone down: ", strength, "Strength Left")
                        if currentEra == ("Bronze Age"):
                            if bronze == 0:
                                bronze = 1
                                age_locks[0] = ("UNLOCKED")
                                itemlock6 = ("UNLOCKED")
                                itemlock7 = ("UNLOCKED")
                                itemlock8 = ("UNLOCKED")
                                itemlock9 = ("UNLOCKED")
                                itemlock10 = ("UNLOCKED")
                                enemyHealthEASY = 200
                                minimumEnemydamageEASY = 5
                                maximumEnemydamageEASY = 10
                                enemyHealthMEDIUM = 300
                                minimumEnemydamageMEDIUM = 7
                                maximumEnemydamageMEDIUM = 15
                                enemyHealthHARD = 400
                                minimumEnemydamageHARD = 15
                                maximumEnemydamageHARD = 25
                                minimumEnemycoinsHARD = 300
                                maximumEnemycoinsHARD = 1200
                                minimumEnemycoinsMEDIUM = 200
                                maximumEnemycoinsMEDIUM = 700
                                minimumEnemycoinsEASY = 100
                                maximumEnemycoinsEASY = 500
                        if currentEra == ("Iron Age"):
                            age_locks[1] = ("UNLOCKED")
                            itemlock11 = ("UNLOCKED")
                            itemlock12 = ("UNLOCKED")
                            itemlock13 = ("UNLOCKED")
                            itemlock14 = ("UNLOCKED")
                            itemlock15 = ("UNLOCKED")
                            enemyHealthEASY = 300
                            minimumEnemydamageEASY = 7
                            maximumEnemydamageEASY = 15
                            enemyHealthMEDIUM = 400
                            minimumEnemydamageMEDIUM = 12
                            maximumEnemydamageMEDIUM = 18
                            enemyHealthHARD = 600
                            minimumEnemydamageHARD = 15
                            maximumEnemydamageHARD = 30
                            minimumEnemycoinsHARD = 600
                            maximumEnemycoinsHARD = 1700
                            minimumEnemycoinsMEDIUM = 500
                            maximumEnemycoinsMEDIUM = 900
                            minimumEnemycoinsEASY = 300
                            maximumEnemycoinsEASY = 800
                        if currentEra == ("Roman Age"):
                            age_locks[2] = ("UNLOCKED")
                            itemlock16 = ("UNLOCKED")
                            itemlock17 = ("UNLOCKED")
                            itemlock18 = ("UNLOCKED")
                            itemlock19 = ("UNLOCKED")
                            itemlock20 = ("UNLOCKED")
                            minimumEnemydamageEASY = 12
                            maximumEnemydamageEASY = 18
                            minimumEnemydamageMEDIUM = 15
                            maximumEnemydamageMEDIUM = 25
                            minimumEnemydamageHARD = 20
                            maximumEnemydamageHARD = 40
                            minimumEnemycoinsHARD = 1200
                            maximumEnemycoinsHARD = 2000
                            minimumEnemycoinsMEDIUM = 800
                            maximumEnemycoinsMEDIUM = 1100
                            minimumEnemycoinsEASY = 600
                            maximumEnemycoinsEASY = 1000
                        if currentEra == ("Medievil Age"):
                            age_locks[3] = ("UNLOCKED")
                            itemlock21 = ("UNLOCKED")
                            itemlock22 = ("UNLOCKED")
                            itemlock23 = ("UNLOCKED")
                            itemlock24 = ("UNLOCKED")
                            itemlock25 = ("UNLOCKED")
                            minimumEnemydamageEASY = 15
                            maximumEnemydamageEASY = 25
                            minimumEnemydamageMEDIUM = 20
                            maximumEnemydamageMEDIUM = 30
                            minimumEnemydamageHARD = 25
                            maximumEnemydamageHARD = 45
                            minimumEnemycoinsHARD = 2000
                            maximumEnemycoinsHARD = 4000
                            minimumEnemycoinsMEDIUM = 1500
                            maximumEnemycoinsMEDIUM = 2000
                            minimumEnemycoinsEASY = 1000
                            maximumEnemycoinsEASY = 1400
                        if currentEra == ("Electric Age"):
                            age_locks[4] = ("UNLOCKED")
                            itemlock26 = ("UNLOCKED")
                            itemlock27 = ("UNLOCKED")
                            itemlock28 = ("UNLOCKED")
                            itemlock29 = ("UNLOCKED")
                            itemlock30 = ("UNLOCKED")
                            minimumEnemydamageEASY = 20
                            maximumEnemydamageEASY = 30
                            minimumEnemydamageMEDIUM = 25
                            maximumEnemydamageMEDIUM = 37
                            minimumEnemydamageHARD = 30
                            maximumEnemydamageHARD = 55
                            minimumEnemycoinsHARD = 8000
                            maximumEnemycoinsHARD = 10000
                            minimumEnemycoinsMEDIUM = 4500
                            maximumEnemycoinsMEDIUM = 7000
                            minimumEnemycoinsEASY = 2000
                            maximumEnemycoinsEASY = 3000
                        if currentEra == ("Modern Age"):
                            age_locks[5] = ("UNLOCKED")
                            itemlock31 = ("UNLOCKED")
                            itemlock32 = ("UNLOCKED")
                            itemlock33 = ("UNLOCKED")
                            itemlock34 = ("UNLOCKED")
                            itemlock35 = ("UNLOCKED")
                            minimumEnemydamageEASY = 25
                            maximumEnemydamageEASY = 37
                            minimumEnemydamageMEDIUM = 30
                            maximumEnemydamageMEDIUM = 45
                            minimumEnemydamageHARD = 35
                            maximumEnemydamageHARD = 60
                            minimumEnemycoinsHARD = 20000
                            maximumEnemycoinsHARD = 50000
                            minimumEnemycoinsMEDIUM = 10000
                            maximumEnemycoinsMEDIUM = 15000
                            minimumEnemycoinsEASY = 5000
                            maximumEnemycoinsEASY = 9000
                    elif money < exmoney:
                        amount = exmoney - money
                        print ("You do not have the required amount of Coins. You need", amount, "Coins to expand")
                        time.sleep(2)
                if number > 6:
                    filler()
                    print ("You are already at the top Age")
                    filler()
                    time.sleep(2)'''
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
                        "Bronze Age": {
                            "unlock_items": [5, 6, 7, 8, 9],
                            "enemy_stats": {"enemyHealthEASY": 200, "minimumEnemydamageEASY": 5, "maximumEnemydamageEASY": 10, "enemyHealthMEDIUM": 300, "minimumEnemydamageMEDIUM": 7, "maximumEnemydamageMEDIUM": 15, "enemyHealthHARD": 400, "minimumEnemydamageHARD": 15, "maximumEnemydamageHARD": 25, "minimumEnemycoinsHARD": 300, "maximumEnemycoinsHARD": 1200, "minimumEnemycoinsMEDIUM": 200, "maximumEnemycoinsMEDIUM": 700, "minimumEnemycoinsEASY": 100, "maximumEnemycoinsEASY": 500},
                            "age_index": 0,
                            "bronze_unlock": True,
                        },
                        "Iron Age": {
                            "unlock_items": [10, 11, 12, 13, 14],
                            "enemy_stats": {"enemyHealthEASY": 300, "minimumEnemydamageEASY": 7, "maximumEnemydamageEASY": 15, "enemyHealthMEDIUM": 400, "minimumEnemydamageMEDIUM": 12, "maximumEnemydamageMEDIUM": 18, "enemyHealthHARD": 600, "minimumEnemydamageHARD": 15, "maximumEnemydamageHARD": 30, "minimumEnemycoinsHARD": 600, "maximumEnemycoinsHARD": 1700, "minimumEnemycoinsMEDIUM": 500, "maximumEnemycoinsMEDIUM": 900, "minimumEnemycoinsEASY": 300, "maximumEnemycoinsEASY": 800},
                            "age_index": 1,
                        },
                        "Roman Age": {
                            "unlock_items": [15, 16, 17, 18, 19],
                            "enemy_stats": {"minimumEnemydamageEASY": 12, "maximumEnemydamageEASY": 18, "minimumEnemydamageMEDIUM": 15, "maximumEnemydamageMEDIUM": 25, "minimumEnemydamageHARD": 20, "maximumEnemydamageHARD": 40, "minimumEnemycoinsHARD": 1200, "maximumEnemycoinsHARD": 2000, "minimumEnemycoinsMEDIUM": 800, "maximumEnemycoinsMEDIUM": 1100, "minimumEnemycoinsEASY": 600, "maximumEnemycoinsEASY": 1000},
                            "age_index": 2,
                        },
                        "Medievil Age": {
                            "unlock_items": [20, 21, 22, 23, 24],
                            "enemy_stats": {"minimumEnemydamageEASY": 15, "maximumEnemydamageEASY": 25, "minimumEnemydamageMEDIUM": 20, "maximumEnemydamageMEDIUM": 30, "minimumEnemydamageHARD": 25, "maximumEnemydamageHARD": 45, "minimumEnemycoinsHARD": 2000, "maximumEnemycoinsHARD": 4000, "minimumEnemycoinsMEDIUM": 1500, "maximumEnemycoinsMEDIUM": 2000, "minimumEnemycoinsEASY": 1000, "maximumEnemycoinsEASY": 1400},
                            "age_index": 3,
                        },
                        "Electric Age": {
                            "unlock_items": [25, 26, 27, 28, 29],
                            "enemy_stats": {"minimumEnemydamageEASY": 20, "maximumEnemydamageEASY": 30, "minimumEnemydamageMEDIUM": 25, "maximumEnemydamageMEDIUM": 37, "minimumEnemydamageHARD": 30, "maximumEnemydamageHARD": 55, "minimumEnemycoinsHARD": 8000, "maximumEnemycoinsHARD": 10000, "minimumEnemycoinsMEDIUM": 4500, "maximumEnemycoinsMEDIUM": 7000, "minimumEnemycoinsEASY": 2000, "maximumEnemycoinsEASY": 3000},
                            "age_index": 4,
                        },
                        "Modern Age": {
                            "unlock_items": [30, 31, 32, 33, 34],
                            "enemy_stats": {"minimumEnemydamageEASY": 25, "maximumEnemydamageEASY": 37, "minimumEnemydamageMEDIUM": 30, "maximumEnemydamageMEDIUM": 45, "minimumEnemydamageHARD": 35, "maximumEnemydamageHARD": 60, "minimumEnemycoinsHARD": 20000, "maximumEnemycoinsHARD": 50000, "minimumEnemycoinsMEDIUM": 10000, "maximumEnemycoinsMEDIUM": 15000, "minimumEnemycoinsEASY": 5000, "maximumEnemycoinsEASY": 9000},
                            "age_index": 5,
                        },
                    }
                    if currentEra in unlock_data:
                        unlock_era(**unlock_data[currentEra])
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
                        filler()
                        print ("============= Items =============")
                        print ("")
                        print ("1: Health Potions (500 Coins)    ")
                        print ("")
                        print ("======== Type the number ========")
                        print ("")
                        item = input("Number: ")
                        if item == ("1"):
                            price = 500
                            filler()
                            amount = input("Quantity: ")
                            amount = int(amount)
                            price = price * amount
                            if money < price:
                                print ("You do not have enough Coins to purchase this item")
                                filler()
                            if money >= price:
                                money = money - price
                                print ("You have successfully purchased",amount,"Health Potions!")
                                hpotion = hpotion + amount
                                filler()
                        if item == ("exit"):
                            print ("You have closed the shop")

                    if spage == ("2"):
                        filler()
                        print ("")
                        print ("================ Items ================")
                        print ("                                      |")
                        print ("1: Bread (20 Coins)                   |")
                        print ("                                      |")
                        print ("=======================================")
                        item = input("Number: ")
                        if item == ("1"):
                            price = 20
                            filler()
                            amount = input("Quantity: ")
                            amount = int(amount)
                            price = price * amount
                            if money < price:
                                print ("You do not have enough Coins to purchase this item")
                                filler()
                            if money >= price:
                                money = money - price
                                print ("You have successfully purchased",amount,"Bread!")
                                bread = bread + amount
                                filler()
#======================================================================================================
                    if spage == ("3"):
                        filler()
                        print ("================ Stone Age ================")
                        print ("       Name                      Price         Purchasable")
                        print ("")
                        print ("1: Pebble                    (1000 Coins)    (",item_locks[0],")")
                        print ("2: Stone                     (5000 Coins)    (",item_locks[1],")")
                        print ("3: Rock                      (7500 Coins)    (",item_locks[2],")")
                        print ("4: Chissled Stone           (12,000 Coins)   (",item_locks[3],")")
                        print ("5: Sharpened Rock           (16,000 Coins)   (",item_locks[4],")")
                        print ("")
                        print ("===============  Bronze Age   ================","(",age_locks[0],")")
                        if age_locks[0] == ("UNLOCKED"):
                            print ("")
                            print ("6: Socketed Axe             (30,000 Coins)   (",item_locks[5],")")
                            print ("7: Dagger                   (45,000 Coins)   (",item_locks[6],")")
                            print ("8: Sickle Sword             (60,000 Coins)   (",item_locks[7],")")
                            print ("9: Reinforced Axe           (90,000 Coins)   (",item_locks[8],")")
                            print ("10: Dead Oak Bow            (120,000 Coins)  (",item_locks[9],")")
                        print ("")
                        print ("===============   Iron Age    ================","(",age_locks[1],")")
                        if age_locks[1] == ("UNLOCKED"):
                            print ("")
                            print ("11: Iron Spear              (165,000 Coins)   (",item_locks[10],")")
                            print ("12: Steel Sword             (200,000 Coins)   (",item_locks[11],")")
                            print ("13: Lance                   (220,000 Coins)   (",item_locks[12],")")
                            print ("14: Axe                     (235,000 Coins)   (",item_locks[13],")")
                            print ("15: Bow                     (260,000 Coins)   (",item_locks[14],")")
                        print ("")
                        print ("===============  Romans Age   ================","(",age_locks[2],")")
                        if age_locks[2] == ("UNLOCKED"):
                            print ("")
                            print ("16: Pugio                   (350,000 Coins)   (",item_locks[15],")")
                            print ("17: Gladius                 (385,000 Coins)   (",item_locks[16],")")
                            print ("18: Spatha                  (400,000 Coins)   (",item_locks[17],")")
                            print ("19: Javelin                 (435,000 Coins)   (",item_locks[18],")")
                            print ("20: Falx                    (495,000 Coins)   (",item_locks[19],")")
                        print ("")
                        print ("==============   Medievil Age  ================","(",age_locks[3],")")
                        if age_locks[3] == ("UNLOCKED"):
                            print ("")
                            print ("21: Lance                   (515,000 Coins)   (",item_locks[20],")")
                            print ("22: Mace                    (545,000 Coins)   (",item_locks[21],")")
                            print ("23: Crossbow                (600,000 Coins)   (",item_locks[22],")")
                            print ("24: Tribuchet               (630,000 Coins)   (",item_locks[23],")")
                            print ("25: Longbow                 (675,000 Coins)   (",item_locks[24],")")
                        print ("")
                        print ("=============== Electric Age  ================","(",age_locks[4],")")
                        if age_locks[4] == ("UNLOCKED"):
                            print ("")
                            print ("26: Fire Lance              (735,000 Coins)   (",item_locks[25],")")
                            print ("27: Proto-gun               (795,000 Coins)   (",item_locks[26],")")
                            print ("28: Gattling Gun            (850,000 Coins)   (",item_locks[27],")")
                            print ("29: Flintlock               (900,000 Coins)   (",item_locks[28],")")
                            print ("30: Revolver                (975,000 Coins)   (",item_locks[29],")")
                        print ("")
                        print ("===============  Modern Age   ================","(",age_locks[5],")")
                        if age_locks[5] == ("UNLOCKED"):
                            print ("")
                            print ("31: Glock                  (1,045,000 Coins)   (",item_locks[30],")")
                            print ("32: Uzi                    (1,100,000 Coins)   (",item_locks[31],")")
                            print ("33: Maxim Gun              (1,150,000 Coins)   (",item_locks[32],")")
                            print ("34: AK-47                  (1,200,000 Coins)   (",item_locks[33],")")
                            print ("35: M1 Garand              (1,300,000 Coins)   (",item_locks[34],")")
                        print ("")
                        print ("============================================")
#================================================= STONE ERA =====================================================
                        item = input("Number: ")
                        if item == ("1"):
                            if item_locks[0] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            elif item_locks[0] == ("UNLOCKED"):
                                price = 1000
                                filler()
                                print ("========== Pebble ==========")
                                print ("                           |")
                                print ("+ 2 Damage                |")
                                print ("                           |")
                                print ("============================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Pebble!")
                                        minimumPlayerdamage = 5 + 2
                                        maximumPlayerdamage = 15 + 2
                                        filler()
                                        currentSword = ("Pebble (+2 Damage)")
                                        item_locks[0] = ("LOCKED")

                        if item == ("2"):
                            if item_locks[1] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            if item_locks[1] == ("UNLOCKED"):
                                price = 5000
                                filler()
                                print ("============ Stone =============")
                                print ("                               |")
                                print ("+ 5 Damage                     |")
                                print ("                               |")
                                print ("================================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Stone!")
                                        minimumPlayerdamage = 5 + 5
                                        maximumPlayerdamage = 15 + 5
                                        filler()
                                        currentSword = ("Stone (+5 Damage)")
                                        item_locks[0] = ("LOCKED")
                                        item_locks[1] = ("LOCKED")

                        if item == ("3"):
                            if item_locks[2] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            if item_locks[2] == ("UNLOCKED"):
                                price = 7500
                                filler()
                                print ("=========== Rock ============")
                                print ("                            |")
                                print ("+ 7 Damage                  |")
                                print ("                            |")
                                print ("=============================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Rock!")
                                        minimumPlayerdamage = 5 + 7
                                        maximumPlayerdamage = 15 + 7
                                        filler()
                                        currentSword = ("Rock (+7 Damage)")
                                        item_locks[0] = ("LOCKED")
                                        item_locks[1] = ("LOCKED")
                                        item_locks[2] = ("LOCKED")

                        if item == ("4"):
                            if item_locks[2] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            if item_locks[2] == ("UNLOCKED"):
                                price = 12000
                                filler()
                                print ("=========== Chissled Stone ============")
                                print ("                                      |")
                                print ("+ 12 Damage                           |")
                                print ("                                      |")
                                print ("=======================================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Chissled Stone!")
                                        minimumPlayerdamage = 5 + 12
                                        maximumPlayerdamage = 15 + 12
                                        filler()
                                        currentSword = ("Chissled Stone (+12 Damage)")
                                        item_locks[0] = ("LOCKED")
                                        item_locks[1] = ("LOCKED")
                                        item_locks[2] = ("LOCKED")
                                        item_locks[3] = ("LOCKED")

                        if item == ("5"):
                            if item_locks[2] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            if item_locks[2] == ("UNLOCKED"):
                                price = 16000
                                filler()
                                print ("=========== Sharpened Rock ============")
                                print ("                                      |")
                                print ("+ 15 Damage                           |")
                                print ("                                      |")
                                print ("=======================================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Sharpened Rock!")
                                        minimumPlayerdamage = 5 + 15
                                        maximumPlayerdamage = 15 + 15
                                        filler()
                                        currentSword = ("Sharpened Rock (+15 Damage)")
                                        item_locks[0] = ("LOCKED")
                                        item_locks[1] = ("LOCKED")
                                        item_locks[2] = ("LOCKED")
                                        item_locks[3] = ("LOCKED")
                                        item_locks[4] = ("LOCKED")

#===================================================== BRONZE ERA ===================================================
                       
                        if item == ("6"):
                            if item_locks[5] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            elif item_locks[5] == ("UNLOCKED"):
                                price = 30000
                                filler()
                                print ("========== Socketed Axe ==========")
                                print ("                                 |")
                                print ("+ 17 Damage                      |")
                                print ("                                 |")
                                print ("==================================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Socketed Axe!")
                                        minimumPlayerdamage = 5 + 17
                                        maximumPlayerdamage = 15 + 17
                                        filler()
                                        currentSword = ("Socketed Axe (+17 Damage)")
                                        item_locks[5] = ("LOCKED")

                        if item == ("7"):
                            if item_locks[6] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            if item_locks[6] == ("UNLOCKED"):
                                price = 45000
                                filler()
                                print ("============ Dagger =============")
                                print ("                                |")
                                print ("+ 20 Damage                     |")
                                print ("                                |")
                                print ("=================================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Dagger!")
                                        minimumPlayerdamage = 5 + 20
                                        maximumPlayerdamage = 15 + 20
                                        filler()
                                        currentSword = ("Dagger (+20 Damage)")
                                        item_locks[5] = ("LOCKED")
                                        item_locks[6] = ("LOCKED")

                        if item == ("8"):
                            if item_locks[7] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            if item_locks[7] == ("UNLOCKED"):
                                price = 60000
                                filler()
                                print ("=========== Sickle Sword ============")
                                print ("                                    |")
                                print ("+ 24 Damage                         |")
                                print ("                                    |")
                                print ("=====================================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Sickle Sword!")
                                        minimumPlayerdamage = 5 + 24
                                        maximumPlayerdamage = 15 + 24
                                        filler()
                                        currentSword = ("Sickle Sword (+24 Damage)")
                                        item_locks[5] = ("LOCKED")
                                        item_locks[6] = ("LOCKED")
                                        item_locks[7] = ("LOCKED")

                        if item == ("9"):
                            if item_locks[8] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            if item_locks[8] == ("UNLOCKED"):
                                price = 90000
                                filler()
                                print ("=========== Reinforced Axe ============")
                                print ("                                      |")
                                print ("+ 27 Damage                           |")
                                print ("                                      |")
                                print ("=======================================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Reinforced Axe!")
                                        minimumPlayerdamage = 5 + 27
                                        maximumPlayerdamage = 15 + 27
                                        filler()
                                        currentSword = ("Reinforced Axe (+27 Damage)")
                                        item_locks[5] = ("LOCKED")
                                        item_locks[6] = ("LOCKED")
                                        item_locks[7] = ("LOCKED")
                                        item_locks[8] = ("LOCKED")

                        if item == ("10"):
                            if item_locks[9] == ("LOCKED"):
                                print ("")
                                print ("You have already purchased this item")
                                print ("")
                            if item_locks[9] == ("UNLOCKED"):
                                price = 120000
                                filler()
                                print ("=========== Dead Oak Bow ==============")
                                print ("                                      |")
                                print ("+ 30 Damage                           |")
                                print ("                                      |")
                                print ("=======================================")
                                print ("")
                                print ("Yes/No")
                                print ("")
                                amount = input("Confirm: ")
                                if amount == ("yes"):
                                    if money < price:
                                        print ("You do not have enough Coins to purchase this item")
                                        filler()
                                    if money >= price:
                                        money = money - price
                                        print ("")
                                        print ("You have successfully purchased 1 Dead Oak Bow!")
                                        minimumPlayerdamage = 5 + 30
                                        maximumPlayerdamage = 15 + 30
                                        filler()
                                        currentSword = ("Dead Oak Bow (+30 Damage)")
                                        item_locks[5] = ("LOCKED")
                                        item_locks[6] = ("LOCKED")
                                        item_locks[7] = ("LOCKED")
                                        item_locks[8] = ("LOCKED")
                                        item_locks[9] = ("LOCKED")
                        
#===================================================== IRON ERA ===================================================

                    if item == ("11"):
                        if item_locks[10] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[10] == ("UNLOCKED"):
                            price = 165000
                            filler()
                            print ("============ Iron Spear  ==============")
                            print ("                                      |")
                            print ("+ 34 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Iron Spear!")
                                    minimumPlayerdamage = 5 + 34
                                    maximumPlayerdamage = 15 + 34
                                    filler()
                                    currentSword = ("Iron Spear (+34 Damage)")
                                    item_locks[10] = ("LOCKED")

                    if item == ("12"):
                        if item_locks[11] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[11] == ("UNLOCKED"):
                            price = 200000
                            filler()
                            print ("============ Steel Sword ==============")
                            print ("                                      |")
                            print ("+ 38 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Steel Sword!")
                                    minimumPlayerdamage = 5 + 38
                                    maximumPlayerdamage = 15 + 38
                                    filler()
                                    currentSword = ("Steel Sword (+38 Damage)")
                                    item_locks[10] = ("LOCKED")
                                    item_locks[11] = ("LOCKED")

                    if item == ("13"):
                        if item_locks[12] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[12] == ("UNLOCKED"):
                            price = 220000
                            filler()
                            print ("=============   Lance   ===============")
                            print ("                                      |")
                            print ("+ 42 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Lance!")
                                    minimumPlayerdamage = 5 + 42
                                    maximumPlayerdamage = 15 + 42
                                    filler()
                                    currentSword = ("Lance (+42 Damage)")
                                    item_locks[10] = ("LOCKED")
                                    item_locks[11] = ("LOCKED")
                                    item_locks[12] = ("LOCKED")

                    if item == ("14"):
                        if item_locks[13] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[13] == ("UNLOCKED"):
                            price = 235000
                            filler()
                            print ("==============   Axe   ================")
                            print ("                                      |")
                            print ("+ 46 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Axe!")
                                    minimumPlayerdamage = 5 + 46
                                    maximumPlayerdamage = 15 + 46
                                    filler()
                                    currentSword = ("Axe (+46 Damage)")
                                    item_locks[10] = ("LOCKED")
                                    item_locks[11] = ("LOCKED")
                                    item_locks[12] = ("LOCKED")
                                    item_locks[13] = ("LOCKED")

                    if item == ("15"):
                        if item_locks[14] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[14] == ("UNLOCKED"):
                            price = 260000
                            filler()
                            print ("==============   Bow   ================")
                            print ("                                      |")
                            print ("+ 50 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Bow!")
                                    minimumPlayerdamage = 5 + 50
                                    maximumPlayerdamage = 15 + 50
                                    filler()
                                    currentSword = ("Bow (+50 Damage)")
                                    item_locks[10] = ("LOCKED")
                                    item_locks[11] = ("LOCKED")
                                    item_locks[12] = ("LOCKED")
                                    item_locks[13] = ("LOCKED")
                                    item_locks[14] = ("LOCKED")

#===================================================== ROMAN ERA ===================================================

                    if item == ("16"):
                        if item_locks[15] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[15] == ("UNLOCKED"):
                            price = 350000
                            filler()
                            print ("==============  Pugio  ================")
                            print ("                                      |")
                            print ("+ 54 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Pugio!")
                                    minimumPlayerdamage = 5 + 54
                                    maximumPlayerdamage = 15 + 54
                                    filler()
                                    currentSword = ("Pugio (+54 Damage)")
                                    item_locks[15] = ("LOCKED")

                    if item == ("17"):
                        if item_locks[16] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[16] == ("UNLOCKED"):
                            price = 385000
                            filler()
                            print ("=============  Gladius  ===============")
                            print ("                                      |")
                            print ("+ 58 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Gladius!")
                                    minimumPlayerdamage = 5 + 58
                                    maximumPlayerdamage = 15 + 58
                                    filler()
                                    currentSword = ("Gladius (+58 Damage)")
                                    item_locks[15] = ("LOCKED")
                                    item_locks[16] = ("LOCKED")

                    if item == ("18"):
                        if item_locks[17] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[17] == ("UNLOCKED"):
                            price = 400000
                            filler()
                            print ("=============   Spatha  ===============")
                            print ("                                      |")
                            print ("+ 62 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Spatha!")
                                    minimumPlayerdamage = 5 + 62
                                    maximumPlayerdamage = 15 + 62
                                    filler()
                                    currentSword = ("Spatha (+62 Damage)")
                                    item_locks[15] = ("LOCKED")
                                    item_locks[16] = ("LOCKED")
                                    item_locks[17] = ("LOCKED")

                    if item == ("19"):
                        if item_locks[18] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[18] == ("UNLOCKED"):
                            price = 435000
                            filler()
                            print ("=============  Javelin  ===============")
                            print ("                                      |")
                            print ("+ 66 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Javelin!")
                                    minimumPlayerdamage = 5 + 66
                                    maximumPlayerdamage = 15 + 66
                                    filler()
                                    currentSword = ("Javelin (+66 Damage)")
                                    item_locks[15] = ("LOCKED")
                                    item_locks[16] = ("LOCKED")
                                    item_locks[17] = ("LOCKED")
                                    item_locks[18] = ("LOCKED")

                    if item == ("20"):
                        if item_locks[19] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[19] == ("UNLOCKED"):
                            price = 495000
                            filler()
                            print ("==============   Falx  ================")
                            print ("                                      |")
                            print ("+ 70 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Falx!")
                                    minimumPlayerdamage = 5 + 70
                                    maximumPlayerdamage = 15 + 70
                                    filler()
                                    currentSword = ("Falx (+70 Damage)")
                                    item_locks[15] = ("LOCKED")
                                    item_locks[16] = ("LOCKED")
                                    item_locks[17] = ("LOCKED")
                                    item_locks[18] = ("LOCKED")
                                    item_locks[19] = ("LOCKED")

# ==================================================== MEDIEVIL AGE ===================================================

                    if item == ("21"):
                        if item_locks[20] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[20] == ("UNLOCKED"):
                            price = 515000
                            filler()
                            print ("================ Lance ================")
                            print ("                                      |")
                            print ("+ 74 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Lance!")
                                    minimumPlayerdamage = 5 + 74
                                    maximumPlayerdamage = 15 + 74
                                    filler()
                                    currentSword = ("Lance (+74 Damage)")
                                    item_locks[20] = ("LOCKED")

                    if item == ("22"):
                        if item_locks[21] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[21] == ("UNLOCKED"):
                            price = 545000
                            filler()
                            print ("================  Mace ================")
                            print ("                                      |")
                            print ("+ 78 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Mace!")
                                    minimumPlayerdamage = 5 + 78
                                    maximumPlayerdamage = 15 + 78
                                    filler()
                                    currentSword = ("Mace (+78 Damage)")
                                    item_locks[20] = ("LOCKED")
                                    item_locks[21] = ("LOCKED")

                    if item == ("23"):
                        if item_locks[22] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[22] == ("UNLOCKED"):
                            price = 600000
                            filler()
                            print ("=============== Crossbow ==============")
                            print ("                                      |")
                            print ("+ 82 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Crossbow!")
                                    minimumPlayerdamage = 5 + 82
                                    maximumPlayerdamage = 15 + 82
                                    filler()
                                    currentSword = ("Crossbow (+82 Damage)")
                                    item_locks[20] = ("LOCKED")
                                    item_locks[21] = ("LOCKED")
                                    item_locks[22] = ("LOCKED")

                    if item == ("24"):
                        if item_locks[23] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[23] == ("UNLOCKED"):
                            price = 630000
                            filler()
                            print ("==============  Tribuchet =============")
                            print ("                                      |")
                            print ("+ 84 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Tribuchet!")
                                    minimumPlayerdamage = 5 + 84
                                    maximumPlayerdamage = 15 + 84
                                    filler()
                                    currentSword = ("Tribuchet (+84 Damage)")
                                    item_locks[20] = ("LOCKED")
                                    item_locks[21] = ("LOCKED")
                                    item_locks[22] = ("LOCKED")
                                    item_locks[23] = ("LOCKED")

                    if item == ("25"):
                        if item_locks[24] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[24] == ("UNLOCKED"):
                            price = 675000
                            filler()
                            print ("===============  Longbow ==============")
                            print ("                                      |")
                            print ("+ 86 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Longbow!")
                                    minimumPlayerdamage = 5 + 86
                                    maximumPlayerdamage = 15 + 86
                                    filler()
                                    currentSword = ("Longbow (+86 Damage)")
                                    item_locks[20] = ("LOCKED")
                                    item_locks[21] = ("LOCKED")
                                    item_locks[22] = ("LOCKED")
                                    item_locks[23] = ("LOCKED")
                                    item_locks[24] = ("LOCKED")

# ========================================================= ELECTRIC AGE ===================================================

                    if item == ("26"):
                        if item_locks[25] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[25] == ("UNLOCKED"):
                            price = 735000
                            filler()
                            print ("==============  Fire Lance ============")
                            print ("                                      |")
                            print ("+ 88 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Fire Lance!")
                                    minimumPlayerdamage = 5 + 88
                                    maximumPlayerdamage = 15 + 88
                                    filler()
                                    currentSword = ("Fire Lance (+88 Damage)")
                                    item_locks[25] = ("LOCKED")

                    if item == ("27"):
                        if item_locks[26] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[26] == ("UNLOCKED"):
                            price = 795000
                            filler()
                            print ("==============  Proto-gun =============")
                            print ("                                      |")
                            print ("+ 90 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Proto-gun!")
                                    minimumPlayerdamage = 5 + 90
                                    maximumPlayerdamage = 15 + 90
                                    filler()
                                    currentSword = ("Proto-gun (+90 Damage)")
                                    item_locks[25] = ("LOCKED")
                                    item_locks[26] = ("LOCKED")

                    if item == ("28"):
                        if item_locks[27] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[27] == ("UNLOCKED"):
                            price = 850000
                            filler()
                            print ("============= Gattling Gun ============")
                            print ("                                      |")
                            print ("+ 92 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Gattling Gun!")
                                    minimumPlayerdamage = 5 + 92
                                    maximumPlayerdamage = 15 + 92
                                    filler()
                                    currentSword = ("Gattling Gun (+92 Damage)")
                                    item_locks[25] = ("LOCKED")
                                    item_locks[26] = ("LOCKED")
                                    item_locks[27] = ("LOCKED")

                    if item == ("29"):
                        if item_locks[28] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[28] == ("UNLOCKED"):
                            price = 900000
                            filler()
                            print ("============== Flintlock ==============")
                            print ("                                      |")
                            print ("+ 94 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Flintlock!")
                                    minimumPlayerdamage = 5 + 94
                                    maximumPlayerdamage = 15 + 94
                                    filler()
                                    currentSword = ("Flintlock (+94 Damage)")
                                    item_locks[25] = ("LOCKED")
                                    item_locks[26] = ("LOCKED")
                                    item_locks[27] = ("LOCKED")
                                    item_locks[28] = ("LOCKED")

                    if item == ("30"):
                        if item_locks[29] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[29] == ("UNLOCKED"):
                            price = 975000
                            filler()
                            print ("==============  Revolver ==============")
                            print ("                                      |")
                            print ("+ 96 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Revolver!")
                                    minimumPlayerdamage = 5 + 96
                                    maximumPlayerdamage = 15 + 96
                                    filler()
                                    currentSword = ("Revolver (+96 Damage)")
                                    item_locks[25] = ("LOCKED")
                                    item_locks[26] = ("LOCKED")
                                    item_locks[27] = ("LOCKED")
                                    item_locks[28] = ("LOCKED")
                                    item_locks[29] = ("LOCKED")

                    if item == ("31"):
                        if item_locks[30] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[30] == ("UNLOCKED"):
                            price = 1045000
                            filler()
                            print ("===============  Glock  ===============")
                            print ("                                      |")
                            print ("+ 98 Damage                           |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Glock!")
                                    minimumPlayerdamage = 5 + 98
                                    maximumPlayerdamage = 15 + 98
                                    filler()
                                    currentSword = ("Glock (+98 Damage)")
                                    item_locks[30] = ("LOCKED")

                    if item == ("32"):
                        if item_locks[31] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[31] == ("UNLOCKED"):
                            price = 1100000
                            filler()
                            print ("===============   Uzi   ===============")
                            print ("                                      |")
                            print ("+ 100 Damage                          |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Uzi!")
                                    minimumPlayerdamage = 5 + 100
                                    maximumPlayerdamage = 15 + 100
                                    filler()
                                    currentSword = ("Uzi (+100 Damage)")
                                    item_locks[30] = ("LOCKED")
                                    item_locks[31] = ("LOCKED")

                    if item == ("33"):
                        if item_locks[32] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[32] == ("UNLOCKED"):
                            price = 1150000
                            filler()
                            print ("============== Maxim Gun ==============")
                            print ("                                      |")
                            print ("+ 102 Damage                          |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 Maxim Gun!")
                                    minimumPlayerdamage = 5 + 102
                                    maximumPlayerdamage = 15 + 102
                                    filler()
                                    currentSword = ("Maxin Gun (+102 Damage)")
                                    item_locks[30] = ("LOCKED")
                                    item_locks[31] = ("LOCKED")
                                    item_locks[32] = ("LOCKED")

                    if item == ("34"):
                        if item_locks[33] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[33] == ("UNLOCKED"):
                            price = 1200000
                            filler()
                            print ("===============  AK-47  ===============")
                            print ("                                      |")
                            print ("+ 104 Damage                          |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 AK-47!")
                                    minimumPlayerdamage = 5 + 104
                                    maximumPlayerdamage = 15 + 104
                                    filler()
                                    currentSword = ("AK-47 (+104 Damage)")
                                    item_locks[30] = ("LOCKED")
                                    item_locks[31] = ("LOCKED")
                                    item_locks[32] = ("LOCKED")
                                    item_locks[33] = ("LOCKED")

                    if item == ("35"):
                        if item_locks[34] == ("LOCKED"):
                            print ("")
                            print ("You have already purchased this item")
                            print ("")
                        if item_locks[34] == ("UNLOCKED"):
                            price = 1300000
                            filler()
                            print ("============== M1 Garand ==============")
                            print ("                                      |")
                            print ("+ 106 Damage                          |")
                            print ("                                      |")
                            print ("=======================================")
                            print ("")
                            print ("Yes/No")
                            print ("")
                            amount = input("Confirm: ")
                            if amount == ("yes"):
                                if money < price:
                                    print ("You do not have enough Coins to purchase this item")
                                    filler()
                                if money >= price:
                                    money = money - price
                                    print ("")
                                    print ("You have successfully purchased 1 M1 Garand!")
                                    minimumPlayerdamage = 5 + 106
                                    maximumPlayerdamage = 15 + 106
                                    filler()
                                    currentSword = ("M1 Garand (+106 Damage)")
                                    item_locks[30] = ("LOCKED")
                                    item_locks[31] = ("LOCKED")
                                    item_locks[32] = ("LOCKED")
                                    item_locks[33] = ("LOCKED")
                                    item_locks[34] = ("LOCKED")
                                    
                    if spage == ("exit"):
                            print ("You have closed the shop")
                            break

                    else:
                        print ("Please try again.")

    #=================================================== PEOPLE ========================================================
            
                        
    #================================================== EXTRA CMDS ======================================================

            if cmd == ("stats"):
                filler()
                data()

            if cmd == ("inv"):
                filler()
                inv()
                

    #================================================== FIGHTING ========================================================
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
                                print ("You did", pdamage, "damage but the enemy did", edamage, "damage to you")
                            if enemy == 2:
                                eblock = random.randint(5,15)#========= ONLY CHANGE THE NUMBERS ============
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
                                    print ("The enemy attacked! The enemy did",edamage, "damage")
                                if edamage < 1:
                                    edamage = edamage - pblock
                                    phealth = phealth + edamage
                                    print ("The enemy attacked! The enemy did",edamage, "damage")
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
                                print ("You do not have any health potions to use! The enemy did", edamage,"damage to you!")

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
                                edamage = random.randint(minimumEnemydamageMEDIUM,maximumEnemydamageMEDIUM)#========= ONLY CHANGE THE NUMBERS ============
                                phealth = phealth - edamage
                                print ("You did", pdamage, "damage but the enemy did", edamage, "damage to you")
                            if enemy == 2:
                                eblock = random.randint(10,20)#========= ONLY CHANGE THE NUMBERS ============
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
                                edamage = random.randint(minimumEnemydamageMEDIUM,maximumEnemydamageMEDIUM)#========= ONLY CHANGE THE NUMBERS ============
                                if edamage >= 0:
                                    edamage = edamage - pblock
                                    phealth = phealth - edamage
                                    print ("The enemy attacked! The enemy did",edamage, "damage")
                                if edamage < 1:
                                    edamage = edamage - pblock
                                    phealth = phealth + edamage
                                    print ("The enemy attacked! The enemy did",edamage, "damage")
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
                                edamage = random.randint(minimumEnemydamageMEDIUM,maximumEnemydamageMEDIUM)#========= ONLY CHANGE THE NUMBERS ============
                                phealth = phealth - edamage
                                print ("You do not have any health potions to use! The enemy did", edamage,"damage to you!")

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
                                edamage = random.randint(minimumEnemydamageHARD,maximumEnemydamageHARD)#========= ONLY CHANGE THE NUMBERS ============
                                phealth = phealth - edamage
                                print ("You did", pdamage, "damage but the enemy did", edamage, "damage to you")
                            if enemy == 2:
                                eblock = random.randint(15,25)#========= ONLY CHANGE THE NUMBERS ============
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
                                edamage = random.randint(minimumEnemydamageHARD,maximumEnemydamageHARD)#========= ONLY CHANGE THE NUMBERS ============
                                if edamage >= 0:
                                    edamage = edamage - pblock
                                    phealth = phealth - edamage
                                    print ("The enemy attacked! The enemy did",edamage, "damage")
                                if edamage < 1:
                                    edamage = edamage - pblock
                                    phealth = phealth + edamage
                                    print ("The enemy attacked! The enemy did",edamage, "damage")
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
                                edamage = random.randint(minimumEnemydamageHARD,maximumEnemydamageHARD)#========= ONLY CHANGE THE NUMBERS ============
                                phealth = phealth - edamage
                                print ("You do not have any health potions to use! The enemy did", edamage,"damage to you!")
                    
        
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
            save_game_state()

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
                save_game_state()
                play = ("menu")
                break

#======================================================= RANDOM ACTS =================================================

    

#======================================================== GAME END ===================================================


print("============Your Score============")
data()
