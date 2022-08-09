from os.path import exists
import sys
sys.path.insert(0, './src')
from input import input_to, Get
from village import Village
import time
from game_constants import *

t=0

f_exist = exists("./replays/moves.txt")
if(not f_exist):
    print("No replays available!")
    exit()

f = open("./replays/moves.txt", "r")
time_line = f.readline().strip()
char_flag = int(f.readline().strip())

v1 = Village(VILLAGE_ROWS, VILLAGE_COLS, char_flag)
v1.printVillage(t)
print("\n\n")

flag=0

queen_big_attack_flag = 0

while(1):
    t+=1
    if(flag==0):
        time_line = f.readline().strip()
        if(time_line==""):
            if(v1.game_end(t)==1):
                break
            else:
                print("Huh?")
                break

    inps = input_to(Get)        # This is here so as to prevent replay from instantly taking input
    if(t!=int(time_line)):
        flag = 1
        continue
    flag = 0
    
    inp = f.readline().strip()
    if(inp==""):
        inp = ' '
    if(inp=='q'):
        break
    if(v1.game_end(t)==1):
        break

    if(queen_big_attack_flag==1):
        queen_big_attack_flag = 0
        v1.queen_attack(16, 9)

    if(v1.player.rage==1 and t-v1.player.prev_rage_time>=100):
        v1.player.rage = 0
        v1.player.prev_rage_time = t
        v1.printVillage(t)
        print("\n\n")

    if(inp=='w' or inp=='s' or inp=='a' or inp=='d'):
        v1.player.move(inp)
        v1.player.prev_inp = inp
        v1.printVillage(t)
        print("\n\n")
    elif(inp==' '):
        if(char_flag==0):
            v1.king_attack()
        elif(char_flag==1):
            v1.queen_attack(8, 5)
        v1.printVillage(t)
        print("\n\n")
    elif(inp=='b'):
        if(char_flag==0):
            v1.king_big_attack()
        elif(char_flag==1):
            queen_big_attack_flag = 1
        v1.printVillage(t)
        print("\n\n")
    elif(inp=='r' and char_flag==0):
        if(t-v1.player.prev_rage_time>=100):
            v1.player.rage = 1
            v1.player.prev_rage_time = t
            v1.printVillage(t)
            print("\n\n")
    elif(inp=='h' and char_flag==0):
        if(t-v1.player.prev_heal_time>=100):
            v1.player.hp = int(v1.player.hp*1.5)
            if(v1.player.hp>KING_HEALTH):
                v1.player.hp = KING_HEALTH
            for barbarian in v1.barbarians:
                barbarian.hp = int(barbarian.hp*1.5)
                if(barbarian.hp>BARBARIAN_HEALTH):
                    barbarian.hp = BARBARIAN_HEALTH
            v1.player.prev_heal_time = t
            v1.printVillage(t)
            print("\n\n")
    elif(inp=='1' or inp=='2' or inp=='3'):
        v1.spawn_barbarian(int(inp))
        v1.printVillage(t)
        print("\n\n")
    elif(inp=='4' or inp=='5' or inp=='6'):
        v1.spawn_archer(int(inp)-3)
        v1.printVillage(t)
        print("\n\n")
    elif(inp=='7' or inp=='8' or inp=='9'):
        v1.spawn_balloon(int(inp)-6)
        v1.printVillage(t)
        print("\n\n")
    elif(inp=='k'):
        for i in range(20):
            v1.player.hp -= 10
            v1.printVillage(t)
            print("\n\n")
            time.sleep(1)
    if(inp=='u'):
        v1.printVillage(t)
        print("\n\n")
    v1.canon_attack()
    v1.wizard_attack()
    
    i=0
    lim=2
    if(v1.player.rage==0):
        lim=1
    for i in range(lim):
        for barbarian in v1.barbarians:
            if(barbarian.hp<=0):
                continue
            if(barbarian.min_distance_object==None):
                v1.barbarian_target_set(barbarian)
            if(barbarian.target != (-1, -1)):
                v1.barbarian_target_set(barbarian)
                if(barbarian.target[0]>0):
                    v1.barbarian_move(barbarian, 1,0)
                    barbarian.target = (barbarian.target[0]-1, barbarian.target[1])
                elif(barbarian.target[0]<0):
                    v1.barbarian_move(barbarian, -1,0)
                    barbarian.target = (barbarian.target[0]+1, barbarian.target[1])
                elif(barbarian.target[1]>0):
                    v1.barbarian_move(barbarian, 0,1)
                    barbarian.target = (barbarian.target[0], barbarian.target[1]-1)
                elif(barbarian.target[1]<0):
                    v1.barbarian_move(barbarian, 0,-1)
                    barbarian.target = (barbarian.target[0], barbarian.target[1]+1)
                if(barbarian.target==(0,0)):
                    barbarian.target = (-1, -1)
                v1.printVillage(t)
            
            elif(barbarian.min_distance_object != None):
                barbarian.min_distance_object.hp -= BARBARIAN_DAMAGE
                if(barbarian.min_distance_object.hp<=0):
                    barbarian.min_distance_object = None
                    v1.barbarian_target_set(barbarian)

        for archer in v1.archers:
            if(archer.hp<=0):
                continue
            if(archer.min_distance_object==None):
                v1.archer_target_set(archer)
            if(archer.target != (-1, -1)):
                v1.archer_target_set(archer)
                if(archer.target[0]>8):
                    v1.archer_move(archer, 2,0)
                    archer.target = (archer.target[0]-2, archer.target[1])
                elif(archer.target[0]<-8):
                    v1.archer_move(archer, -2,0)
                    archer.target = (archer.target[0]+2, archer.target[1])
                elif(archer.target[1]>8):
                    v1.archer_move(archer, 0,2)
                    archer.target = (archer.target[0], archer.target[1]-2)
                elif(archer.target[1]<-8):
                    v1.archer_move(archer, 0,-2)
                    archer.target = (archer.target[0], archer.target[1]+2)
                if(archer.target<=(8,8) and archer.target>=(-8,-8)):
                    archer.target = (-1, -1)
                v1.printVillage(t)
            
            elif(archer.min_distance_object != None):
                archer.min_distance_object.hp -= ARCHER_DAMAGE
                if(archer.min_distance_object.hp<=0):
                    archer.min_distance_object = None
                    v1.archer_target_set(archer)
        
        for balloon in v1.balloons:
            if(balloon.hp<=0):
                continue
            if(balloon.min_distance_object==None):
                v1.balloon_target_set(balloon)
            if(balloon.target != (-1, -1)):
                v1.balloon_target_set(balloon)
                if(balloon.target[0]>0):
                    v1.balloon_move(balloon, 1,0)
                    balloon.target = (balloon.target[0]-1, balloon.target[1])
                elif(balloon.target[0]<0):
                    v1.balloon_move(balloon, -1,0)
                    balloon.target = (balloon.target[0]+1, balloon.target[1])
                elif(balloon.target[1]>0):
                    v1.balloon_move(balloon, 0,1)
                    balloon.target = (balloon.target[0], balloon.target[1]-1)
                elif(balloon.target[1]<0):
                    v1.balloon_move(balloon, 0,-1)
                    balloon.target = (balloon.target[0], balloon.target[1]+1)
                if(balloon.target==(0,0)):
                    balloon.target = (-1, -1)
                v1.printVillage(t)
            
            elif(balloon.min_distance_object != None):
                balloon.min_distance_object.hp -= BALLOON_DAMAGE
                if(balloon.min_distance_object.hp<=0):
                    balloon.min_distance_object = None
                    v1.balloon_target_set(balloon)

