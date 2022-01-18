from tkinter import *
import tkinter.messagebox as messagebox
import random
"""La classe principale du jeu, qui est le contrôleur de l'ensemble du jeu."""

def aleatoire(proba) :                 #une fonction parce qu'il retourne quelque chose
    nb = random.random()
    if(nb < proba[0]):
        return 4
    elif(proba[0] < nb < proba[1]):
        return 3
    elif(proba[1] < nb < proba[2]):
        return 2
    else:
        return 1


def newBoard(n, proba) :                                      
    if(0 < proba[0] < proba[1] < proba[2] < 1):
        plateau = [[0 for i in range(n)] for j in range(n)] 
        for i in range(n):
            for j in range(n):
                plateau[i][j] = aleatoire(proba)
    return plateau




class game:
    def __init__(self, size):
        self.size = size
        self.plateau = newBoard(n , proba)
        print(self.plateau)
        self.coord = []
        self.liste= [0]*size
        self.current_score = self.score()

    def set_plateau(self, plateau):
        self.plateau = plateau
    
                 
    def existe_case_adj(self):  # parametres n ,  plateau a deux dimensions, i et j
        for i in range(size):
            for j in range(size):
                if not 0 <= i < size or not 0 <= j < size: return 'Error'
                if i + 1 < self.size:
                    if self.plateau[i + 1][j] == self.plateau[i][j]: return True
                if j + 1 < self.size:
                    if self.plateau[i][j + 1] == self.plateau[i][j]: return True
                if 0 <= j - 1:
                    if self.plateau[i][j - 1] == self.plateau[i][j]: return True
                if 0 <= i - 1:
                    if self.plateau[i - 1][j] == self.plateau[i][j]: return True
                return False

    def reste_coup(self):
        resultat = False  # on debut on a rien trouvé on sait pas si une case a une meme valeur adjacente
        for i in range(size):
            for j in range(size):
                if self.existe_case_adj():  # si la case a une case adjacente de la meme valeur
                    resultat = True  # le resultat change et devient vrai
        return resultat

    def propagation(self):   # fonction pour calculer toutes les cases adjacentes d'une cellule
        if self.existe_case_adj():
            for self.coord in self.liste:
                i = self.liste[0]
                j = self.liste[1]
                if i > 0:
                    if self.plateau[i-1][j] == self.plateau[i][j] and (i-1, j) not in self.liste: #it also checks if the coordinates is in the list or not
                        self.liste.append((i-1,j))
                if i < (size-1):    
                    if self.plateau[i+1][j] == self.plateau[i][j] and (i+1, j) not in self.liste:
                        self.liste.append((i+1,j))
                if j > 0:    
                    if self.plateau[i][j-1] == self.plateau[i][j] and (i, j-1) not in self.liste:
                        self.liste.append((i,j-1))
                if j < (size-1):        
                    if self.plateau[i][j+1] == self.plateau[i][j] and (i, j+1) not in self.liste:
                        self.liste.append((i,j+1))
            return self.liste
        


    def update(self) : # fonction incrementer et pour mettre un 0 sur toutes cases adjacentes qu'on a trouvé
        print(self.liste)
        i= self.liste[0]
        j= self.liste[1]
        #valeur incrementer par 1
        self.plateau[i][j]=+1
        #ici toutes les valeurs des autres coordonnées dans la liste self.sont mises à 0
        for i in range(1, len(self.liste)):
            
            self.plateau[self.liste[0]][self.liste[1]] = 0
        
        return self.plateau
            

    def down(self) :            # pour deplacer les cases vers le bas s'il ya des 0 et ajouter de nouvelles valeurs aleatoires
        
        for i in range(size):
            for j in range(size):
                if self.plateau[i][j] == 0 and i >= 1:
                    if i == 1:
                        self.plateau[i][j] = self.plateau[i - 1][j]
                        self.plateau[0][j] = 0
                    elif i == 2:
                        self.plateau[2][j] = self.plateau[i - 1][j]
                        self.plateau[1][j] = self.plateau[i - 2][j]
                        self.plateau[0][j] = 0
                    elif i == 3:
                        self.plateau[i][j] = self.plateau[i - 1][j]
                        self.plateau[2][j] = self.plateau[i - 2][j]
                        self.plateau[1][j] = self.plateau[i - 3][j]
                        self.plateau[0][j] = 0
                    elif i == 4:
                        self.plateau[i][j] = self.plateau[i - 1][j]
                        self.plateau[3][j] = self.plateau[i - 2][j]
                        self.plateau[2][j] = self.plateau[i - 3][j]
                        self.plateau[1][j] = self.plateau[i - 4][j]
                        self.plateau[0][j] = 0
                    elif i == 5:
                        self.plateau[i][j] = self.plateau[i - 1][j]
                        self.plateau[4][j] = self.plateau[i - 2][j]
                        self.plateau[3][j] = self.plateau[i - 3][j]
                        self.plateau[2][j] = self.plateau[i - 4][j]
                        self.plateau[1][j] = self.plateau[i - 5][j]
                        self.plateau[0][j] = 0
        for p in range(size):
            for m in range(size):
                if self.plateau[p][m] == 0:
                    self.plateau[p][m] = aleatoire(proba) # du coup la derniere case en haut n'aura rien et on y met une valeur aleatoire
        return self.plateau
                    
    def found_10(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.plateau[i][j] >= 10:
                    return True
        return False

    def score(self):
        for i in range (size):
            for j in range(size):
                self.current_score =+ self.plateau[i][j]
                return self.current_score

    def display(self):
        for n in self.plateau:
            for number in n:
                print(number, end=' ')
            print('\n')


""" La classe de vue GUI du jeu Get10 montrant via tkinter """

class GUI:                               
    SIZE = 500
    CELL_PADDING = 1
    BACKGROUND_COLOR = '#f9f6f2'
    SCORE_FONT = "Helvetica", 32, "bold"
    Couleur1 = {
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
    Couleur2 = {
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
        self.window.title('Just Get 10')
        self.window.resizable(False, False)
        self.background = Frame(self.window, bg=GUI.BACKGROUND_COLOR)
        
        self.case = []
        for i in range(self.game.size):
            ligne = []
            for j in range(self.game.size):
                label = Label(self.background, text='',
                                 justify=CENTER, font=GUI.FONT,
                                 width=4, height=2)
                label.grid(row=i, column=j,padx=1, pady=1)
                ligne.append(label)
            self.case.append(ligne)
        self.background.pack(side=TOP)
        self.start_plateau_num = self.game.size
        self.window.bind("<Button-1>" , self.Leftclick)
        self.paint()
        self.window.mainloop()
    
    
    def paint(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                    cell_text = str(self.game.plateau[i][j])
                    bg_color = GUI.Couleur1.get(cell_text)
                    fg_color = GUI.Couleur2.get(cell_text)
                    self.case[i][j].configure(
                        text=cell_text,
                        bg=bg_color, fg=fg_color)
        



    def Leftclick(self, event):
        for i in range(self.game.size):
            for j in range(self.game.size):
                self.case=self.game.plateau[i][j]
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
        taillex = (self.game.size * GUI.CELL_PADDING )  #calcule la longueur de la grille 
        tailley = (self.game.size *  GUI.CELL_PADDING)    #calcule la hauteur de la grille 
        if x >= 0 and x < taillex and y >= 0 and y < tailley :  #test pour connaitre si on a cliqué a l'interieur de la grille
            i = int(y / self.game.size)            # on calcule a partir du y le i de la case selectionnée
            j = int(x  / self.game.size)  
            current = (i, j)                                 # c'est la case selectionée
            L = [current]
            print(L)
        
        L = self.click()
                 
        key_value = event.keysym
        print('{} Mouse Left Click Pressed'.format(key_value))
        
        print('Score: {}'.format(self.game.current_score))
        
        if self.game.found_10():
            return self.you_win()

    def click(self):
        while self.game.reste_coup() == True :
            self.game.propagation() # apelle fonction propagation pour calculer toutes les cases adjacentes d'une cellule
            self.game.update()    #appelle procedure update pour incrementer et mettre les 0
            self.game.down()     #appelle procedure down
            self.game.display() #display
            self.window.update()
            print(self.game.plateau)
        else:
            return self.game_over
    
    def you_win(self):
        if not self.won:
            self.won = True
            print('You Win!')
            if messagebox.askyesno('Get10Game', 'You Win!\n' 'Are you going to continue the Get10Game ?'):
                self.keep_playing = True

    def game_over(self):
        print('Game over!')
        messagebox.showinfo('Get10Game', 'Game over!')
        
if __name__ == '__main__':
    proba = (0.05, 0.25, 0.3, 0.4)
    n=6
    size = 6
    game = game(size)
    panel = GUI(game)
