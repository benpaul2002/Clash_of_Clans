from colorama import Fore, Back, Style
from game_constants import BARBARIAN_HEALTH, ARCHER_HEALTH, BALLOON_HEALTH

class Troop:
    def __init__(self, row, col, map2, hp):
        self.current_pos = (row, col)
        self.map2 = map2
        self.hp = hp
        self.target = (-1, -1)
        self.min_distance_object = None
    
    def print(self, letter, hp):
        if(self.hp>0.5*hp):
            print(Fore.GREEN + letter, end='')
        elif(self.hp>0.2*hp):
            print(Fore.YELLOW + letter, end='')
        elif(self.hp>0):
            print(Fore.RED + letter, end='')
        else:
            print(Fore.GREEN + '.', end='')

class Barbarian(Troop):
    def __init__(self, row, col, map2, hp):
        super().__init__(row, col, map2, hp)
    def print(self):
        super().print('B', BARBARIAN_HEALTH)

class Archer(Troop):
    def __init__(self, row, col, map2, hp):
        super().__init__(row, col, map2, hp)
    def print(self):
        super().print('A', ARCHER_HEALTH)

class Balloon(Troop):
    def __init__(self, row, col, map2, hp):
        super().__init__(row, col, map2, hp)
    def print(self):
        super().print('O', BALLOON_HEALTH)
