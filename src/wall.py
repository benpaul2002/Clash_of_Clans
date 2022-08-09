from tkinter import W
from colorama import Fore, Back, Style
from game_constants import WALL_HEALTH

class Wall:
    def __init__(self, row, col, map2, hp):
        self.row = row
        self.col = col
        self.hp = hp
        self.map2 = map2
    
    def print(self):
        i=0
        for row in self.map2:
            j=0
            for col in row:
                if(i==self.row and j==self.col):
                    if(self.hp>0.5*WALL_HEALTH):
                        self.map2[i][j] = Fore.GREEN + 'W'
                    elif(self.hp>0.2*WALL_HEALTH):
                        self.map2[i][j] = Fore.YELLOW + 'W'
                    elif(self.hp>0):
                        self.map2[i][j] = Fore.RED + 'W'
                    else:
                        self.map2[i][j] = '.'
                    break
                j+=1
            i+=1