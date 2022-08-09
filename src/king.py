from colorama import Fore, Back, Style
import time
from game_constants import KING_HEALTH

class King:
    def __init__(self, rows, cols, map2, hp):
        self.current_pos = (0, int(cols/2))
        self.rows = rows
        self.cols = cols
        self.map2 = map2
        self.hp = hp
        self.prev_big_attack_time = time.time()
        self.prev_inp = None
        self.rage = 0
        self.prev_rage_time = 0
        self.prev_heal_time = 0
        self.letter = 'K'

    def move(self, inp):
        if(self.hp<=0):
            return

        if(inp=='w' and self.current_pos[0]!=0 and self.map2[self.current_pos[0]-1][self.current_pos[1]]=='.'):
            if(self.rage==1 and self.current_pos[0]!=1 and self.map2[self.current_pos[0]-2][self.current_pos[1]]=='.'):
                self.current_pos = (self.current_pos[0]-2, self.current_pos[1])
            else:
                self.current_pos = (self.current_pos[0]-1, self.current_pos[1])

        elif(inp=='s' and self.current_pos[0]!=self.rows-1 and self.map2[self.current_pos[0]+1][self.current_pos[1]]=='.'):
            if(self.rage==1 and self.current_pos[0]!=self.rows-2 and self.map2[self.current_pos[0]+2][self.current_pos[1]]=='.'):
                self.current_pos = (self.current_pos[0]+2, self.current_pos[1])
            else:
                self.current_pos = (self.current_pos[0]+1, self.current_pos[1])

        elif(inp=='a' and self.current_pos[1]!=0 and self.map2[self.current_pos[0]][self.current_pos[1]-1]=='.'):
            if(self.rage==1 and self.current_pos[1]!=1 and self.map2[self.current_pos[0]][self.current_pos[1]-2]=='.'):
                self.current_pos = (self.current_pos[0], self.current_pos[1]-2)
            else:
                self.current_pos = (self.current_pos[0], self.current_pos[1]-1)

        elif(inp=='d' and self.current_pos[1]!=self.cols-1 and self.map2[self.current_pos[0]][self.current_pos[1]+1]=='.'):
            if(self.rage==1 and self.current_pos[1]!=self.cols-2 and self.map2[self.current_pos[0]][self.current_pos[1]+2]=='.'):
                self.current_pos = (self.current_pos[0], self.current_pos[1]+2)
            else:
                self.current_pos = (self.current_pos[0], self.current_pos[1]+1)

    def print_stats(self, t):
        print("\nKing HP: " + str(self.hp) + "\t\t\t0 ", end='')
        if(self.hp>0.5*KING_HEALTH):
            print("|" + Back.GREEN, end='')
        elif(self.hp>0.2*KING_HEALTH):
            print("|" + Back.YELLOW, end='')
        elif(self.hp>=0):
            print("|" + Back.RED, end='')
        for i in range(int(self.hp/10)):
            print(" ", end='')
        print(Style.RESET_ALL, end='')
        for i in range(int((KING_HEALTH-self.hp)/10)):
            print(" ", end='')
        print("| " + str(KING_HEALTH))

        if(self.rage==1):
            print("Rage Spell Activated!")
        elif(t-self.prev_rage_time>=100):
            print("Rage Spell ready!")
        else:
            print("Rage cooldown: " + str(100-t+self.prev_rage_time))

        if(t-self.prev_heal_time>=100):
            print("Heal Spell ready!")
        else:
            print("Heal cooldown: " + str(100-t+self.prev_heal_time))

        if(time.time()-self.prev_big_attack_time>5):
            print("Leviathan Axe Ready!")
        else:
            print("Leviathan Axe cooldown: " + str(int(5-time.time()+self.prev_big_attack_time)))
