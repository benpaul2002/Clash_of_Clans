from colorama import Fore, Back, Style
import time
from game_constants import HUT_HEALTH, TOWNHALL_HEALTH, CANON_HEALTH, WIZARD_HEALTH

class Building:
    def __init__(self, start_row, start_col, end_row, end_col, map2, hp):
        self.start_row = start_row
        self.start_col = start_col
        self.end_row = end_row
        self.end_col = end_col
        self.map2 = map2
        self.hp = hp
        coords = []
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                coord = (i,j)
                coords.append(coord)
        self.coords = coords

    def print(self, letter, hp, flash=0):
        i=0
        for row in self.map2:
            j=0
            for col in row:
                if(i>=self.start_row and i<=self.end_row and j>=self.start_col and j<=self.end_col):
                    if(flash==1):    
                        if(self.hp>0.5*hp):
                            self.map2[i][j] = Back.BLUE + Fore.GREEN + letter
                        elif(self.hp>0.2*hp):
                            self.map2[i][j] = Back.BLUE + Fore.YELLOW + letter
                        elif(self.hp>0):
                            self.map2[i][j] = Back.BLUE + Fore.RED + letter
                        else:
                            self.map2[i][j] = '.'
                    else:
                        if(self.hp>0.5*hp):
                            self.map2[i][j] = Fore.GREEN + letter
                        elif(self.hp>0.2*hp):
                            self.map2[i][j] = Fore.YELLOW + letter
                        elif(self.hp>0):
                            self.map2[i][j] = Fore.RED + letter
                        else:
                            self.map2[i][j] = '.'
                j+=1
            i+=1

class Hut(Building):
    def __init__(self, start_row, start_col, map2, hp):
        super().__init__(start_row, start_col, start_row, start_col, map2, hp)

    def print(self):
        super().print('H', HUT_HEALTH)

class TownHall(Building):
    def __init__(self, start_row, start_col, end_row, end_col, map2, hp):
        super().__init__(start_row, start_col, end_row, end_col, map2, hp)

    def print(self):
        super().print('T', TOWNHALL_HEALTH)

class Canon(Building):
    def __init__(self, start_row, start_col, map2, hp):
        super().__init__(start_row, start_col, start_row, start_col, map2, hp)
        self.prev_attack_time = time.time()
        self.flash = 0

    def print(self):
        super().print('C', CANON_HEALTH, self.flash)

class WizardTower(Building):
    def __init__(self, start_row, start_col, map2, hp):
        super().__init__(start_row, start_col, start_row, start_col, map2, hp)
        self.prev_attack_time = time.time()
        self.flash = 0

    def print(self):
        super().print('Z', WIZARD_HEALTH, self.flash)