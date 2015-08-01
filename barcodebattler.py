#Barcode Battler

#Import modules
from sys import argv
import zbar, random, pygame, time

#Variable
global player, HP,enemyHP, enemy_name, weapon, equip, code

#Functions
def scanner():
    global code
    proc = zbar.Processor()
    proc.parse_config('enable')
    device = '/dev/video1'
    if len(argv) > 1:
        device = argv[1]
    proc.init(device)
    proc.visible = True
    proc.process_one()
    proc.visible = False
    for symbol in proc.results:
        code = symbol.data

#Choose player, this is handled via QR codes on cards.
def player():
        global code,player,HP
        if code == "Andrew":
                print("Andrew is your warrior")
                HP = random.randint(10,100)
                player = "Andrew"
                print(player+" has "+str(HP)+" HP")
        elif code == "Ben":
                print("Ben is your warrior")
                HP = random.randint(10,100)
                player = "Ben"
                print(player+" has "+str(HP)+" HP")
        elif code == "Graham":
                print("Graham is your warrior")
                HP = random.randint(10,100)
                player = "Graham"
                print(player+" has "+str(HP)+" HP")
        elif code == "Mike":
                print("Mike is your warrior")
                HP = random.randint(10,100)
                player = "Mike"
                print(player+" has "+str(HP)+" HP")

        else:
                print("Player not recognised, please scan one of the cards to continue")
                


#Generate an enemy.
def enemy():
        global enemy_name
        global enemyHP
        enemy_names = ["Windows10","Killersaur","MegaDave","OpenSourcerer"]
        enemy_name = random.choice(enemy_names)
        enemyHP = random.randint(10,100)
        print("Your enemy is "+enemy_name)
        print("They have "+str(enemyHP)+" HP")
              

#Equip player with a weapon
def weapon():
        global code
        global weapon
        scanner()
        print(code)
        value = int(code) / 13000000000000 / random.randint(0,5)
        print(value)
        if value > 0 and value < 5:
                print("You have a basic wooden sword")
                weapon = ("wooden_sword")
        elif value > 5 and value < 11:
                print("You have a steel sword")
                weapon = ("steel_sword")
        elif value == 0:
                print("You have no sword...you will have to use your fists of fury!")
                weapon = ("fists")
        else:
                print("You have an enchanted sword of mega power")
                weapon = ("enchanted_sword")

def equip():
        global code
        global equip
        scanner()
        print(code)
        value = int(code) / 13000000000 / random.randint(0,5)
        #print(value)
        if value > 0 and value < 5:
                print("You have a basic wooden shield")
                equip = ("wood_shield")
        elif value > 5 and value < 11:
                print("You have an iron shield")
                equip = ("iron_shield")
        elif value == 0:
                print("You have no shield...that sucks")
                equip = ("nothing")
        else:
                print("You have a mirrored shield that can reflect half damage to your attacker")
                equip = ("mirror_shield")

def player_attack():
        global enemy_name
        global enemyHP
        chance = ["attack","miss"]
        chance = random.choice(chance)
        #print(chance)
        if chance != "miss":
                damage = random.randint(0,10)
                print("DAMAGE:",damage)
                enemyHP = enemyHP - damage
                print("You cause "+str(damage)+" damage to "+(enemy_name)+" they now have "+str(enemyHP)+" HP")
        elif HP < 1:
                print("YOU'RE DEAD")
                game_over()
                
        else:
                print("Player misses the opponent")
        
                
def enemy_attack():
        global player
        global HP      
        chance = ["attack","miss"]
        chance = random.choice(chance)
        if chance != "miss":
                damage = random.randint(0,10)
                print("DAMAGE:",damage)
                time.sleep(2)
                HP = HP - damage
                print("Your enemy causes "+str(damage)+" damage to "+(player)+" they now have "+str(HP)+" HP")
        elif enemyHP < 1:
                print("ENEMY DEAD")
                game_over()
        else:
                print("Opponent misses the player")

def game_over():
        print("GAME OVER")

#T E S T I N G
scanner()
#print(code)
player()
enemy()
time.sleep(5)
weapon()
time.sleep(5)
equip()
while True:
        if HP <= 0 or enemyHP <= 0:
                print("G A M E  O V E R")
                if HP < 1:
                        print("Your enemy has won!")
                else:
                        print("You have vanquished your enemy")
                break
                #player_attack()
                #time.sleep(1)
                #enemy_attack()
        else:
                player_attack()
                time.sleep(1)
                enemy_attack()                
