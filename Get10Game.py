from tkinter import *
import tkinter.messagebox as messagebox
import sys
import random
"""La classe principale du jeu, qui est le contrôleur de l'ensemble du jeu."""

class game:
    def __init__(self, size):
        self.size = size
        self.matrice = self.generate_empty_game()
        self.coord = ()
        self.liste= []
        self.current_score = 0

    def setCoord(self, coord):
        self.coord = coord
        
    def setList(self, liste):
        self.liste = liste
        
    def generate_empty_game(self):
        return [[0] * size for i in range(size)]
    
    
    def aleatoire(self):
        for i in range(size):
            for j in range(size):
                if random.random() < 0.4:
                    self.matrice[i][j] = 1
                elif random.random() < 0.3:
                    self.matrice[i][j] = 2
                elif random.random() < 0.25:
                    self.matrice[i][j] = 3
                elif random.random() < 0.05:
                    self.matrice[i][j] = 4
        print(self.matrice)
    
    def existe_case_adj(self):  # parametres n ,  matrice a deux dimensions, i et j
        for i in range(size):
            for j in range(size):
                if not 0 <= i < size or not 0 <= j < size: return 'Error'
                if i + 1 < self.size:
                    if self.matrice[i + 1][j] == self.matrice[i][j]: return True
                if j + 1 < self.size:
                    if self.matrice[i][j + 1] == self.matrice[i][j]: return True
                if 0 <= j - 1:
                    if self.matrice[i][j - 1] == self.matrice[i][j]: return True
                if 0 <= i - 1:
                    if self.matrice[i - 1][j] == self.matrice[i][j]: return True
                return False

    def reste_coup(self):
        resultat = False  # on debut on a rien trouvé on sait pas si une case a une meme valeur adjacente
        for i in range(size):
            for j in range(size):
                if self.existe_case_adj():  # si la case a une case adjacente de la meme valeur
                    resultat = True  # le resultat change et devient vrai
        return resultat

    def propagation(self):   # fonction pour calculer toutes les cases adjacentes d'une cellule
        
        for self.coord in self.liste:
            i = self.coord[0]
            j = self.coord[1]
            number = self.matrice[i][j]
            if i > 0:
                if self.matrice[i-1][j] == number and (i-1, j) not in self.liste: #it also checks if the coordinates is in the list or not
                    self.liste.append((i-1,j))
            if i < (size-1):    
                if self.matrice[i+1][j] == number and (i+1, j) not in self.liste:
                    self.liste.append((i+1,j))
            if j > 0:    
                if self.matrice[i][j-1] == number and (i, j-1) not in self.liste:
                    self.liste.append((i,j-1))
            if j < (size-1):        
                if self.matrice[i][j+1] == number and (i, j+1) not in self.liste:
                    self.liste.append((i,j+1))
        return self.liste


    def modification(self) : # fonction incrementer et pour mettre un 0 sur toutes cases adjacentes qu'on a trouvé
        i,j= self.liste[0]
        #the value is here incremented by 1
        self.matrice[i][j] =+ 1

        #here all the values of the other coordinates in the self.liste are set to 0
        for coordinates in self.liste[1:]:
            i = coordinates[0]
            j = coordinates[1]
            self.matrice[i][j] = 0
        
        return self.matrice
            

    def gravity(self) :            # pour deplacer les cases vers le bas s'il ya des 0 et ajouter de nouvelles valeurs aleatoires
        for i in range(size):
            for j in range(size):
                if self.matrice[i][j] == 0 and i >= 1:
                    if i == 1:
                        self.matrice[i][j] = self.matrice[i - 1][j]
                        self.matrice[0][j] = 0
                    elif i == 2:
                        self.matrice[2][j] = self.matrice[i - 1][j]
                        self.matrice[1][j] = self.matrice[i - 2][j]
                        self.matrice[0][j] = 0
                    elif i == 3:
                        self.matrice[i][j] = self.matrice[i - 1][j]
                        self.matrice[2][j] = self.matrice[i - 2][j]
                        self.matrice[1][j] = self.matrice[i - 3][j]
                        self.matrice[0][j] = 0
                    elif i == 4:
                        self.matrice[i][j] = self.matrice[i - 1][j]
                        self.matrice[3][j] = self.matrice[i - 2][j]
                        self.matrice[2][j] = self.matrice[i - 3][j]
                        self.matrice[1][j] = self.matrice[i - 4][j]
                        self.matrice[0][j] = 0
                    elif i == 5:
                        self.matrice[i][j] = self.matrice[i - 1][j]
                        self.matrice[4][j] = self.matrice[i - 2][j]
                        self.matrice[3][j] = self.matrice[i - 3][j]
                        self.matrice[2][j] = self.matrice[i - 4][j]
                        self.matrice[1][j] = self.matrice[i - 5][j]
                        self.matrice[0][j] = 0
        self.current_score += self.matrice[i][j]
        for p in range(size):
            for m in range(size):
                if self.matrice[p][m] == 0:
                    self.matrice[p][m] = self.aleatoire(self) # du coup la derniere case en haut n'aura rien et on y met une valeur aleatoire
                    
    def found_10(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.matrice[i][j] >= 10:
                    return True
        return False


    def set_matrice(self, matrice):
        self.matrice = matrice

    def display(self):
        for n in self.matrice:
            for number in n:
                print(number, end=' ')
            print('\n')


""" La classe de vue GUI du jeu Get10 montrant via tkinter """

class GUI:                               
    SIZE = 500
    marge_gauche = SIZE / 5      # une marge de gauche pour que ca colle pas a la fenetre
    marge_haut = SIZE / 5  
    game_LEN = 4
    game_PADDING = 10
    CELL_PADDING = 5
    BACKGROUND_COLOR = '#f9f6f2'
    SCORE_FONT = "Helvetica", 32, "bold"
    CELL_BACKGROUND_COLOR_DICT = {
        '1': '#2ECC71',
        '2': '#2874A6',
        '3': '#F1C40F',
        '4': '#BA4A00',
        '5': '#117A65',
        '6': '#8E44AD',
        '7': '#DE3163',
        '8': '#A93226',
        '9': '#F7DC6F',
        '10': '#5D6D7E',
        'beyond': '#3c3a32'
    }
    CELL_COLOR_DICT = {
        '1': '#f9f6f2',
        '2': '#f9f6f2',
        '3': '#f9f6f2',
        '4': '#f9f6f2',
        '5': '#f9f6f2',
        '6': '#f9f6f2',
        '7': '#f9f6f2',
        '8': '#f9f6f2',
        '9': '#f9f6f2',
        '10': '#f9f6f2',
        'beyond': '#f9f6f2'
    }
    FONT = ('Verdana', 24, 'bold')
    MOUSE_CLICK_LEFT = ('<Button-1>')

    def __init__(self, game):
        self.game = game
        self.window = Tk()
        if sys.platform == 'win32':
            self.window.title('JustGet10')
            
        self.window.resizable(False, False)
        self.background = Frame(self.window, bg=GUI.BACKGROUND_COLOR)
        self.cell_labels = []
        for i in range(self.game.size):
            row_labels = []
            for j in range(self.game.size):
                label = Label(self.background, text='',
                                 justify=CENTER, font=GUI.FONT,
                                 width=4, height=2)
                label.grid(row=i, column=j, padx=5, pady=5)
                row_labels.append(label)
            self.cell_labels.append(row_labels)
        self.background.pack(side=TOP)
        self.start_matrice_num = self.game.size
        self.window.bind("<Button-1>" , self.Leftclick)
        self.add_start_matrice()
        self.paint()
        self.window.mainloop()
    
    
    def paint(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                    cell_text = str(self.game.matrice[i][j])
                    if self.game.matrice[i][j] > 10:
                        bg_color = GUI.CELL_BACKGROUND_COLOR_DICT.get('beyond')
                        fg_color = GUI.CELL_COLOR_DICT.get('beyond')
                    else:
                        bg_color = GUI.CELL_BACKGROUND_COLOR_DICT.get(cell_text)
                        fg_color = GUI.CELL_COLOR_DICT.get(cell_text)
                    self.cell_labels[i][j].configure(
                        text=cell_text,
                        bg=bg_color, fg=fg_color)
                    
    def add_start_matrice(self):
        for i in range(self.start_matrice_num):
            self.game.aleatoire()


    def Leftclick(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
        taillex = GUI.SIZE + (self.game.size * GUI.CELL_PADDING )  #calcule la longueur de la grille + sa marge gauche
        tailley = GUI.SIZE + (self.game.size *  GUI.CELL_PADDING)    #calcule la hauteur de la grille + sa marge haut
        if x >= 0 and x < taillex and y >= 0 and y < tailley :  #test pour connaitre si on a cliqué a l'interieur de la grille
            i = int((y - GUI.SIZE)/GUI.CELL_PADDING)            # on calcule a partir du y de la souris(qui est en pixel ) le i de la case selectionnée
            j = int((x - GUI.SIZE) / GUI.CELL_PADDING)  
            current = (i, j)                                 # c'est la case selectionée
            L = [current]
            print(L)
        self.game.propagation()                
        key_value = event.keysym
        print('{} Mouse Left Click Pressed'.format(key_value))
        self.click()
        print('Score: {}'.format(self.game.current_score))
        if  self.game.existe_case_adj():
            self.add_start_matrice
        self.paint()
        if self.game.found_10():
            return self.you_win()

    def click(self):
        if  self.game.existe_case_adj():
            self.game.liste=self.game.propagation()
            self.game.modification()    #appelle procedure modification pour incrementer et mettre les 0
            self.game.gravity()     #appelle procedure gravity  
            self.game.display()
            print(self.matrice)
            self.paint()
        elif not self.game.reste_coup():
            return self.game_over
    
    def you_win(self):
        if not self.won:
            self.won = True
            print('You Win!')
            if messagebox.askyesno('Get10Game', 'You Win!\n' 'Are you going to continue the Get10Game game?'):
                self.keep_playing = True

    def game_over(self):
        print('Game over!')
        messagebox.showinfo('Get10Game', 'Game over!')
        
if __name__ == '__main__':
    size = 6
    game = game(size)
    panel = GUI(game)
