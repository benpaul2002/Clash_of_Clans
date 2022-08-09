from building import Hut, TownHall, Canon, WizardTower
from wall import Wall
from king import King
from queen import Queen
from troop import Barbarian, Archer, Balloon
import time
from colorama import Fore, Back, Style
from game_constants import *

class Village:
    def __init__(self, rows, cols, char_flag):
        self.level = 1
        self.rows = rows
        self.cols = cols
        self.char_flag = char_flag
        self.next_village()

    def level_update(self):
        if(self.level==3):
            return
        self.level += 1
        self.next_village()
        
    def next_village(self):
        map = []
        for i in range(self.rows):
            row = ['.']*self.cols
            row.append('\n')
            map.append(row)
        self.map = map
        map2 = map
        self.map2 = map2

        spawn1 = (0, self.cols/2)
        spawn2 = (self.rows/2, 0)
        spawn3 = (self.rows-1, self.cols/2)
        self.spawn1 = spawn1
        self.spawn2 = spawn2
        self.spawn3 = spawn3

        self.townHall = TownHall(int(self.rows/2 - 2), int(self.cols/2 - 2), int(self.rows/2 + 2), int(self.cols/2 + 1), map2, TOWNHALL_HEALTH)

        huts = []
        hut1 = Hut(int(self.rows/2 - 6), int(self.cols/2 - 2), map2, HUT_HEALTH)
        hut2 = Hut(int(self.rows/2 - 4), int(self.cols/2 + 8), map2, HUT_HEALTH)
        hut3 = Hut(int(self.rows/2 + 6), int(self.cols/2 + 10), map2, HUT_HEALTH)
        hut4 = Hut(int(self.rows/2 + 4), int(self.cols/2 - 5), map2, HUT_HEALTH)
        hut5 = Hut(int(self.rows/2 - 3), int(self.cols/2 - 10), map2, HUT_HEALTH)
        huts.append(hut1)
        huts.append(hut2)
        huts.append(hut3)
        huts.append(hut4)
        huts.append(hut5)
        self.huts = huts

        walls = []
        start_row = 7
        start_col = 7
        end_row = self.rows-7
        end_col = self.cols-7
        i=0
        for row in self.map2:
            j=0
            for col in row:
                if((i==start_row or i==end_row) and j>=start_col and j<=end_col):
                    wall = Wall(i, j, self.map2, WALL_HEALTH)
                    walls.append(wall)
                elif((j==start_col or j==end_col) and i>=start_row and i<end_row):
                    wall = Wall(i, j, self.map2, WALL_HEALTH)
                    walls.append(wall)
                j+=1
            i+=1
        
        self.walls = walls

        canons=[]
        canon1 = Canon(int(self.rows/2), int(self.cols/2 - 8), map2, CANON_HEALTH)
        canon2 = Canon(int(self.rows/2), int(self.cols/2 + 6), map2, CANON_HEALTH)
        canon3 = Canon(int(3*self.rows/5), int(self.cols/2 - 14), map2, CANON_HEALTH)
        canon4 = Canon(int(3*self.rows/5), int(self.cols/2 + 12), map2, CANON_HEALTH)
        canons.append(canon1)
        canons.append(canon2)
        canons.append(canon3)
        canons.append(canon4)
        self.canons = canons[:self.level+1]

        if(self.char_flag==0):
            self.player = King(self.rows, self.cols, map2, KING_HEALTH)
        else:
            self.player = Queen(self.rows, self.cols, map2, QUEEN_HEALTH)

        barbarians = []
        self.barbarians = barbarians
        self.barbarian_count = 0

        archers = []
        self.archers = archers
        self.archer_count = 0

        balloons = []
        self.balloons = balloons
        self.balloon_count = 0

        wizards=[]
        wizard1 = WizardTower(int(self.rows/3), int(self.cols/2 - 8), map2, WIZARD_HEALTH)
        wizard2 = WizardTower(int(2*self.rows/3), int(self.cols/2 + 6), map2, WIZARD_HEALTH)
        wizard3 = WizardTower(int(self.rows/2), int(self.cols/2 - 14), map2, WIZARD_HEALTH)
        wizard4 = WizardTower(int(self.rows/2), int(self.cols/2 + 12), map2, WIZARD_HEALTH)
        wizards.append(wizard1)
        wizards.append(wizard2)
        wizards.append(wizard3)
        wizards.append(wizard4)
        self.wizards = wizards[:self.level+1]

    def printVillage(self, t):
        self.player.print_stats(t)

        self.townHall.print()
        for hut in self.huts:
            hut.print()
        for wall in self.walls:
            wall.print()
        for canon in self.canons:
            canon.print()
            if(canon.flash==1):
                canon.flash = 0
        for wizard in self.wizards:
            wizard.print()
            if(wizard.flash==1):
                wizard.flash = 0

        i=0
        for row in self.map2:
            j=0
            for col in row:
                if((i,j)==(self.player.current_pos)):
                    if(self.player.rage==1):
                        print(Back.GREEN + self.player.letter, end='' + Style.RESET_ALL)
                    elif(self.player.hp>100):
                        print(Fore.GREEN + self.player.letter, end='' + Style.RESET_ALL)
                    elif(self.player.hp>50):
                        print(Fore.YELLOW + self.player.letter, end='' + Style.RESET_ALL)
                    elif(self.player.hp>0):
                        print(Fore.RED + self.player.letter, end='' + Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + '.', end='' + Style.RESET_ALL)
                else:
                    flag = 0
                    for barbarian in self.barbarians:
                        if((i,j)==barbarian.current_pos):
                            barbarian.print()
                            flag+=1
                    for archer in self.archers:
                        if((i,j)==archer.current_pos):
                            archer.print()
                            flag+=1
                    for balloon in self.balloons:
                        if((i,j)==balloon.current_pos):
                            balloon.print()
                            flag+=1
                    if(flag==0):
                        print(Fore.GREEN + col, end='' + Style.RESET_ALL)
                j+=1
            i+=1
            print(Style.RESET_ALL, end='')

    def spawn_barbarian(self, spawn_point):
        if(self.barbarian_count>=BARBARIAN_LIMIT):
            return
        if(spawn_point==1):
            barbarian = Barbarian(self.spawn1[0], self.spawn1[1], self.map2, BARBARIAN_HEALTH)
        elif(spawn_point==2):
            barbarian = Barbarian(self.spawn2[0], self.spawn2[1], self.map2, BARBARIAN_HEALTH)
        elif(spawn_point==3):
            barbarian = Barbarian(self.spawn3[0], self.spawn3[1], self.map2, BARBARIAN_HEALTH)
        self.barbarians.append(barbarian)
        self.barbarian_count += 1
    
    def barbarian_move(self, barbarian, delx, dely):
        if(barbarian.hp<=0):
            return
        for wall in self.walls:
            if((barbarian.current_pos[0]+delx, barbarian.current_pos[1]+dely)==(wall.row, wall.col)):
                wall.hp -= BARBARIAN_DAMAGE
                if(wall.hp>0):
                    return
        barbarian.current_pos = (barbarian.current_pos[0]+delx, barbarian.current_pos[1]+dely)

    def barbarian_target_set(self, barbarian):
        if(barbarian.hp<=0):
            return

        i = barbarian.current_pos[0]
        j = barbarian.current_pos[1]

        min_delx = VILLAGE_ROWS+1
        min_dely = VILLAGE_COLS+1
        min_distance = abs(min_delx) + abs(min_dely)
        min_distance_object = None

        if(self.townHall.hp>0):
            min_delx = self.townHall.start_row - i
            min_dely = self.townHall.start_col - j - 1
            min_distance = abs(min_delx) + abs(min_dely)
            min_distance_object = self.townHall

        for canon in self.canons:
            if(canon.hp<=0):
                continue
            delx = canon.start_row - i
            dely = canon.start_col - j - 1
            distance = abs(delx) + abs(dely)
            if(distance<min_distance):
                min_delx = delx
                min_dely = dely
                min_distance = distance
                min_distance_object = canon

        for wizard in self.wizards:
            if(wizard.hp<=0):
                continue
            delx = wizard.start_row - i
            dely = wizard.start_col - j - 1
            distance = abs(delx) + abs(dely)
            if(distance<min_distance):
                min_delx = delx
                min_dely = dely
                min_distance = distance
                min_distance_object = wizard
                
        for hut in self.huts:
            if(hut.hp<=0):
                continue
            delx = hut.start_row - i
            dely = hut.start_col - j - 1
            distance = abs(delx) + abs(dely)
            if(distance<min_distance):
                min_delx = delx
                min_dely = dely
                min_distance = distance
                min_distance_object = hut

        barbarian.target = (int(min_delx), int(min_dely))    
        barbarian.min_distance_object = min_distance_object

    def spawn_archer(self, spawn_point):
        if(self.archer_count>=ARCHER_LIMIT):
            return
        if(spawn_point==1):
            archer = Archer(self.spawn1[0], self.spawn1[1], self.map2, ARCHER_HEALTH)
        elif(spawn_point==2):
            archer = Archer(self.spawn2[0], self.spawn2[1], self.map2, ARCHER_HEALTH)
        elif(spawn_point==3):
            archer = Archer(self.spawn3[0], self.spawn3[1], self.map2, ARCHER_HEALTH)
        self.archers.append(archer)
        self.archer_count += 1
    
    def archer_move(self, archer, delx, dely):
        if(archer.hp<=0):
            return
        for wall in self.walls:
            if((archer.current_pos[0]+1, archer.current_pos[1]+0)==(wall.row, wall.col)):
                wall.hp -= ARCHER_DAMAGE
                if(wall.hp>0):
                    return
            if((archer.current_pos[0]+0, archer.current_pos[1]+1)==(wall.row, wall.col)):
                wall.hp -= ARCHER_DAMAGE
                if(wall.hp>0):
                    return
            if((archer.current_pos[0]+2, archer.current_pos[1]+0)==(wall.row, wall.col)):
                wall.hp -= ARCHER_DAMAGE
                if(wall.hp>0):
                    return
            if((archer.current_pos[0]+0, archer.current_pos[1]+2)==(wall.row, wall.col)):
                wall.hp -= ARCHER_DAMAGE
                if(wall.hp>0):
                    return
            if((archer.current_pos[0]-1, archer.current_pos[1]+0)==(wall.row, wall.col)):
                wall.hp -= ARCHER_DAMAGE
                if(wall.hp>0):
                    return
            if((archer.current_pos[0]+0, archer.current_pos[1]-1)==(wall.row, wall.col)):
                wall.hp -= ARCHER_DAMAGE
                if(wall.hp>0):
                    return
            if((archer.current_pos[0]-2, archer.current_pos[1]+0)==(wall.row, wall.col)):
                wall.hp -= ARCHER_DAMAGE
                if(wall.hp>0):
                    return
            if((archer.current_pos[0]+0, archer.current_pos[1]-2)==(wall.row, wall.col)):
                wall.hp -= ARCHER_DAMAGE
                if(wall.hp>0):
                    return
        archer.current_pos = (archer.current_pos[0]+delx, archer.current_pos[1]+dely)

    def archer_target_set(self, archer):
        if(archer.hp<=0):
            return
        
        i = archer.current_pos[0]
        j = archer.current_pos[1]

        min_delx = VILLAGE_ROWS+1
        min_dely = VILLAGE_COLS+1
        min_distance = abs(min_delx) + abs(min_dely)
        min_distance_object = None

        if(self.townHall.hp>0):
            min_delx = self.townHall.start_row - i
            min_dely = self.townHall.start_col - j - 1
            min_distance = abs(min_delx) + abs(min_dely)
            min_distance_object = self.townHall

        for canon in self.canons:
            if(canon.hp<=0):
                continue
            delx = canon.start_row - i
            dely = canon.start_col - j - 1
            distance = abs(delx) + abs(dely)
            if(distance<min_distance):
                min_delx = delx
                min_dely = dely
                min_distance = distance
                min_distance_object = canon

        for wizard in self.wizards:
            if(wizard.hp<=0):
                continue
            delx = wizard.start_row - i
            dely = wizard.start_col - j - 1
            distance = abs(delx) + abs(dely)
            if(distance<min_distance):
                min_delx = delx
                min_dely = dely
                min_distance = distance
                min_distance_object = wizard
                
        for hut in self.huts:
            if(hut.hp<=0):
                continue
            delx = hut.start_row - i
            dely = hut.start_col - j - 1
            distance = abs(delx) + abs(dely)
            if(distance<min_distance):
                min_delx = delx
                min_dely = dely
                min_distance = distance
                min_distance_object = hut

        archer.target = (int(min_delx), int(min_dely))
        archer.min_distance_object = min_distance_object

    def spawn_balloon(self, spawn_point):
        if(self.balloon_count>=BALLOON_LIMIT):
            return
        if(spawn_point==1):
            balloon = Balloon(self.spawn1[0], self.spawn1[1], self.map2, BALLOON_HEALTH)
        elif(spawn_point==2):
            balloon = Balloon(self.spawn2[0], self.spawn2[1], self.map2, BALLOON_HEALTH)
        elif(spawn_point==3):
            balloon = Balloon(self.spawn3[0], self.spawn3[1], self.map2, BALLOON_HEALTH)
        self.balloons.append(balloon)
        self.balloon_count += 1

    def balloon_move(self, balloon, delx, dely):
        if(balloon.hp<=0):
            return
        balloon.current_pos = (balloon.current_pos[0]+delx, balloon.current_pos[1]+dely)

    def balloon_target_set(self, balloon):
        if(balloon.hp<=0):
            return
        
        i = balloon.current_pos[0]
        j = balloon.current_pos[1]

        min_delx = VILLAGE_ROWS+1
        min_dely = VILLAGE_COLS+1
        min_distance = abs(min_delx) + abs(min_dely)
        min_distance_object = None

        canon_flag = 0
        wizard_flag = 0

        for canon in self.canons:
            if(canon.hp<=0):
                continue
            delx = canon.start_row - i
            dely = canon.start_col - j - 1
            distance = abs(delx) + abs(dely)
            if(distance<min_distance):
                min_delx = delx
                min_dely = dely
                min_distance = distance
                min_distance_object = canon
                canon_flag = 1

        if(canon_flag==0):
            for wizard in self.wizards:
                if(wizard.hp<=0):
                    continue
                delx = wizard.start_row - i
                dely = wizard.start_col - j - 1
                distance = abs(delx) + abs(dely)
                if(distance<min_distance):
                    min_delx = delx
                    min_dely = dely
                    min_distance = distance
                    min_distance_object = wizard
                    wizard_flag = 1

        if(canon_flag==0 and wizard_flag==0 and self.townHall.hp>0):
            min_delx = self.townHall.start_row - i
            min_dely = self.townHall.start_col - j - 1
            min_distance = abs(min_delx) + abs(min_dely)
            min_distance_object = self.townHall
                
        if(canon_flag==0 and wizard_flag==0):
            for hut in self.huts:
                if(hut.hp<=0):
                    continue
                delx = hut.start_row - i
                dely = hut.start_col - j - 1
                distance = abs(delx) + abs(dely)
                if(distance<min_distance):
                    min_delx = delx
                    min_dely = dely
                    min_distance = distance
                    min_distance_object = hut

        balloon.target = (int(min_delx), int(min_dely))
        balloon.min_distance_object = min_distance_object

    def king_attack_helper(self, i, j):
        for wall in self.walls:
            if((i,j)==(wall.row, wall.col)):
                if(self.player.rage==1):
                    wall.hp -= 2*KING_DAMAGE
                else:
                    wall.hp -= KING_DAMAGE
                break
        for hut in self.huts:
            if((i,j)==(hut.start_row, hut.start_col)):
                if(self.player.rage==1):
                    hut.hp -= 2*KING_DAMAGE
                else:
                    hut.hp -= KING_DAMAGE
                break
        for canon in self.canons:
            if((i,j)==(canon.start_row, canon.start_col)):
                if(self.player.rage==1):
                    canon.hp -= 2*KING_DAMAGE
                else:
                    canon.hp -= KING_DAMAGE
                break
        for wizard in self.wizards:
            if((i,j)==(wizard.start_row, wizard.start_col)):
                if(self.player.rage==1):
                    wizard.hp -= 2*KING_DAMAGE
                else:
                    wizard.hp -= KING_DAMAGE
                break
        if(i>=self.townHall.start_row and i<=self.townHall.end_row and j>=self.townHall.start_col and j<=self.townHall.end_col):
            if(self.player.rage==1):
                self.townHall.hp -= 2*KING_DAMAGE
            else:
                self.townHall.hp -= KING_DAMAGE

    def king_attack(self):
        i=0
        for row in self.map2:
            j=0
            for col in row:
                if((i,j)==(self.player.current_pos[0]-1, self.player.current_pos[1]) and self.player.prev_inp=='w'):
                    self.king_attack_helper(i, j)
                    break

                if((i,j)==(self.player.current_pos[0]+1, self.player.current_pos[1]) and self.player.prev_inp=='s'):
                    self.king_attack_helper(i, j)
                    break

                if((i,j)==(self.player.current_pos[0], self.player.current_pos[1]-1) and self.player.prev_inp=='a'):
                    self.king_attack_helper(i, j)
                    break

                if((i,j)==(self.player.current_pos[0], self.player.current_pos[1]+1) and self.player.prev_inp=='d'):
                    self.king_attack_helper(i, j)
                    break

                j+=1
            i+=1

    def king_big_attack(self):
        cur_time = time.time()
        if(cur_time-self.player.prev_big_attack_time<5):
            return
        self.player.prev_big_attack_time = time.time()
        i=0
        townhall_flag = 0
        for row in self.map2:
            j=0
            for col in row:
                if(i>=self.player.current_pos[0]-3 and i<=self.player.current_pos[0]+3 and j>=self.player.current_pos[1]-3 and j<=self.player.current_pos[1]+3):
                    for wall in self.walls:
                        if((i,j)==(wall.row, wall.col)):
                            if(self.player.rage==1):
                                wall.hp -= 2*KING_DAMAGE
                            else:
                                wall.hp -= KING_DAMAGE

                    for hut in self.huts:
                        if((i,j)==(hut.start_row, hut.start_col)):
                            if(self.player.rage==1):
                                hut.hp -= 2*KING_DAMAGE
                            else:
                                hut.hp -= KING_DAMAGE
                            
                    for canon in self.canons:
                        if((i,j)==(canon.start_row, canon.start_col)):
                            if(self.player.rage==1):
                                canon.hp -= 2*KING_DAMAGE
                            else:
                                canon.hp -= KING_DAMAGE

                    for wizard in self.wizards:
                        if((i,j)==(wizard.start_row, wizard.start_col)):
                            if(self.player.rage==1):
                                wizard.hp -= 2*KING_DAMAGE
                            else:
                                wizard.hp -= KING_DAMAGE
                            
                    if(townhall_flag==0 and i>=self.townHall.start_row and i<self.townHall.end_row and j>=self.townHall.start_col and j<self.townHall.end_col):
                        if(self.player.rage==1):
                            self.townHall.hp -= 2*KING_DAMAGE
                        else:
                            self.townHall.hp -= KING_DAMAGE
                        townhall_flag = 1
                    

                j+=1
            i+=1

    def queen_attack_helper(self, i, j, attack_range):
        for wall in self.walls:
            if(abs(i-wall.row)<=attack_range and abs(j-wall.col)<=attack_range):
                wall.hp -= QUEEN_DAMAGE
        for hut in self.huts:
            if(abs(i-hut.start_row)<=attack_range and abs(j-hut.start_col)<=attack_range):
                hut.hp -= QUEEN_DAMAGE
        for canon in self.canons:
            if(abs(i-canon.start_row)<=attack_range and abs(j-canon.start_col)<=attack_range):
                canon.hp -= QUEEN_DAMAGE
        for wizard in self.wizards:
            if(abs(i-wizard.start_row)<=attack_range and abs(j-wizard.start_col)<=attack_range):
                wizard.hp -= QUEEN_DAMAGE
        if(abs(i-self.townHall.start_row)<=attack_range and abs(j-self.townHall.start_col)<=attack_range):
            self.townHall.hp -= QUEEN_DAMAGE
        elif(abs(i-self.townHall.end_row)<=attack_range and abs(j-self.townHall.end_col)<=attack_range):
            self.townHall.hp -= QUEEN_DAMAGE

    def queen_attack(self, tile_distance, attack_range):
        if(tile_distance==16):
            cur_time = time.time()
            if(cur_time-self.player.prev_big_attack_time<5):
                return
            self.player.prev_big_attack_time = time.time()
        i=0
        for row in self.map2:
            j=0
            for col in row:
                if((i,j)==(self.player.current_pos[0]-tile_distance, self.player.current_pos[1]) and self.player.prev_inp=='w'):
                    self.queen_attack_helper(i,j, attack_range)
                    break
                if((i,j)==(self.player.current_pos[0]+tile_distance, self.player.current_pos[1]) and self.player.prev_inp=='s'):
                    self.queen_attack_helper(i,j, attack_range)
                    break
                if((i,j)==(self.player.current_pos[0], self.player.current_pos[1]-tile_distance) and self.player.prev_inp=='a'):
                    self.queen_attack_helper(i,j, attack_range)
                    break
                if((i,j)==(self.player.current_pos[0], self.player.current_pos[1]+tile_distance) and self.player.prev_inp=='d'):
                    self.queen_attack_helper(i,j, attack_range)
                    break

                j+=1
            i+=1

    def canon_attack(self):
        flag = 0
        cur_time = time.time()
        for canon in self.canons:
            if(cur_time-canon.prev_attack_time<3 or canon.hp<=0):
                flag += 1
                continue
            canon.prev_attack_time = time.time()
            i=0
            for row in self.map2:
                j=0
                for col in row:
                    if(i>=canon.start_row-6 and i<=canon.start_row+6 and j>=canon.start_col-6 and j<=canon.start_col+6):
                        if((i,j)==(self.player.current_pos)):
                            self.player.hp -= CANON_DAMAGE
                            canon.flash = 1
                        else:
                            for barbarian in self.barbarians:
                                if(barbarian.hp<=0):
                                    continue
                                if((i,j)==(barbarian.current_pos)):
                                    barbarian.hp -= CANON_DAMAGE
                                    canon.flash = 1
                            for archer in self.archers:
                                if(archer.hp<=0):
                                    continue
                                if((i,j)==(archer.current_pos)):
                                    archer.hp -= CANON_DAMAGE
                                    canon.flash = 1

                    j+=1
                i+=1
        if(flag==2):
            return -1

    def wizard_attack_helper(self, i, j):
        if(abs(i-self.player.current_pos[0])<=3 and abs(j-self.player.current_pos[1])<=3):
            self.player.hp -= WIZARD_DAMAGE
        for barbarian in self.barbarians:
            if(barbarian.hp<=0):
                continue
            if(abs(i-barbarian.current_pos[0])<=3 and abs(j-barbarian.current_pos[1])<=3):
                barbarian.hp -= WIZARD_DAMAGE
        for archer in self.archers:
            if(archer.hp<=0):
                continue
            if(abs(i-archer.current_pos[0])<=3 and abs(j-archer.current_pos[1])<=3):
                archer.hp -= WIZARD_DAMAGE
        for balloon in self.balloons:
            if(balloon.hp<=0):
                continue
            if(abs(i-balloon.current_pos[0])<=3 and abs(j-balloon.current_pos[1])<=3):
                balloon.hp -= WIZARD_DAMAGE

    def wizard_attack(self):
        flag = 0
        cur_time = time.time()
        for wizard in self.wizards:
            if(cur_time-wizard.prev_attack_time<3 or wizard.hp<=0):
                flag += 1
                continue
            wizard.prev_attack_time = time.time()
            i=0
            for row in self.map2:
                j=0
                for col in row:
                    if(i>=wizard.start_row-6 and i<=wizard.start_row+6 and j>=wizard.start_col-6 and j<=wizard.start_col+6):
                        if((i,j)==(self.player.current_pos)):
                            self.wizard_attack_helper(i, j)
                            wizard.flash = 1
                        else:
                            for barbarian in self.barbarians:
                                if(barbarian.hp<=0):
                                    continue
                                if((i,j)==(barbarian.current_pos)):
                                    self.wizard_attack_helper(i, j)
                                    wizard.flash = 1
                            for archer in self.archers:
                                if(archer.hp<=0):
                                    continue
                                if((i,j)==(archer.current_pos)):
                                    self.wizard_attack_helper(i, j)
                                    wizard.flash = 1
                            for balloon in self.balloons:
                                if(balloon.hp<=0):
                                    continue
                                if((i,j)==(balloon.current_pos)):
                                    self.wizard_attack_helper(i, j)
                                    wizard.flash = 1

                    j+=1
                i+=1
        if(flag==2):
            return -1

    def game_end(self, t):
        if(self.player.hp<=0):
            self.printVillage(t)
            print("You lose!")
            return 1
        else:
            for hut in self.huts:
                if(hut.hp>0):
                    return -1
            for canon in self.canons:
                if(canon.hp>0):
                    return -1
            for wizard in self.wizards:
                if(wizard.hp>0):
                    return -1
            if(self.townHall.hp>0):
                return -1
            self.printVillage(t)
            print("Level passed!")
            if(self.level<3):
                self.level_update()
                self.next_village()
                return -1
            else:
                print("You win!")
                return 1
