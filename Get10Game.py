import tkinter as tk
import tkinter.messagebox as messagebox
import sys
import random
"""La classe principale du jeu, qui est le contrôleur de l'ensemble du jeu."""

class game:
    def __init__(self, size):
        self.size = size
        self.cells = self.generate_empty_game()
        self.current_score = 0

    def generate_empty_game(self):
        return [[0] * self.size for i in range(self.size)]
    
    def aleatoire(self):
        for i in range(self.size):
            for j in range(self.size):
                if random.random() < 0.6:
                    self.cells[i][j] = 1
                elif random.random() < 0.45:
                    self.cells[i][j] = 2
                elif random.random() < 0.2:
                    self.cells[i][j] = 3
                elif random.random() < 0.1:
                    self.cells[i][j] = 4
    
    def existe_case_adj(self):  # parametres n ,  cells a deux dimensions, i et j
        for i in range(self.size):
            for j in range(self.size):
                if i <= 0:                          # on donne des conditions pour exclure le test sur les cases qui depassent la grille ou deborden
                    if j <= 0:
                        return self.cells[i + 1][j] == self.cells[i][j] or self.cells[i][j + 1] == self.cells[i][j]
                    elif j >= self.size  - 1:
                        return self.cells[i + 1][j] == self.cells[i][j] or self.cells[i][j - 1] == self.cells[i][j]
                    else:
                        return self.cells[i + 1][j] == self.cells[i][j] or self.cells[i][j - 1] == self.cells[i][j] or self.cells[i][j + 1] == self.cells[i][j]
                elif i >= self.size - 1:
                    if j <= 0:
                        return self.cells[i - 1][j] == self.cells[i][j] or self.cells[i][j + 1] == self.cells[i][j]
                    elif j >= self.size  - 1:
                        return self.cells[i - 1][j] == self.cells[i][j] or self.cells[i][j - 1] == self.cells[i][j]
                    else:
                        return self.cells[i - 1][j] == self.cells[i][j] or self.cells[i][j - 1] == self.cells[i][j] or self.cells[i][j + 1] == self.cells[i][j]
                else:
                    if j <= 0:
                        return self.cells[i - 1][j] == self.cells[i][j] or self.cells[i + 1][j] == self.cells[i][j] or self.cells[i][j + 1] == self.cells[i][j]
                    elif j >= self.size  - 1:
                        return self.cells[i - 1][j] == self.cells[i][j] or self.cells[i + 1][j] == self.cells[i][j] or self.cells[i][j - 1] == self.cells[i][j]
                    else:
                        return self.cells[i - 1][j] == self.cells[i][j] or self.cells[i + 1][j] == self.cells[i][j] or self.cells[i][j - 1] == self.cells[i][j] or \
                        self.cells[i][j + 1] == self.cells[i][j]    

    def reste_coup(self):
        resultat = False  # on debut on a rien trouvé on sait pas si une case a une meme valeur adjacente
        for i in range(self.size):
            for j in range(self.size):
                if self.existe_case_adj():  # si la case a une case adjacente de la meme valeur
                    resultat = True  # le resultat change et devient vrai
        return resultat

    def propagation(self ,liste_tuple, tuple):   # fonction pour calculer toutes les cases adjacentes d'une cellule
        tuple=[[],[]]
        i = tuple[0]  #recupere le i du tuple
        j = tuple[1] #recupere le j du tuple
        if self.existe_case_adj() :
            if i <= 0:                     # on donne des conditions pour exclure le test sur les cases qui depassent la grille ou debordent
                if j <= 0:

                    if self.cells[i + 1][j] == self.cells[i][j] :  # si la valeur de la cellule(case) est egale a la cellule selectionnée (tuple)
                        if (i + 1, j) not in liste_tuple :   # si cette cellule n'est pas dans la liste liste_tuple (L plus tard)
                            liste_tuple.append((i + 1, j))   # on ajoute la cellule
                            self.propagation(self ,liste_tuple, (i + 1, j)) # et la on excute fonction propagation sur la cellule
                                                                            # qu'on vient de trouver (c'est la recusivité)
                    if self.cells[i][j + 1] == self.cells[i][j] :   # meme principe que le bloc precedent et sur tous les autres cases
                        if (i, j + 1) not in liste_tuple :
                            liste_tuple.append((i, j + 1))
                            self.propagation(self ,liste_tuple, (i + 1, j))

                elif j >= self.size - 1 :

                    if self.cells[i + 1][j] == self.cells[i][j] :
                        if (i + 1, j) not in liste_tuple :
                            liste_tuple.append((i + 1, j))
                            self.propagation(self, liste_tuple, (i + 1, j))
                    if self.cells[i][j - 1] == self.cells[i][j] :
                        if (i, j - 1) not in liste_tuple :
                            liste_tuple.append((i, j - 1))
                            self.propagation(self, liste_tuple, (i, j - 1))

                else:

                    if self.cells[i + 1][j] == self.cells[i][j] :
                        if (i + 1, j) not in liste_tuple :
                            liste_tuple.append((i + 1, j))
                            self.propagation(self, liste_tuple, (i + 1, j),)
                    if self.cells[i][j - 1] == self.cells[i][j] :
                        if (i, j - 1) not in liste_tuple :
                            liste_tuple.append((i, j - 1))
                            self.propagation(self, liste_tuple, (i, j - 1))
                    if self.cells[i][j + 1] == self.cells[i][j] :
                        if (i, j + 1) not in liste_tuple :
                            liste_tuple.append((i, j + 1))
                            self.propagation(self, liste_tuple, (i, j + 1))

            elif i >= self.size - 1:
                if j <= 0:

                    if self.cells[i - 1][j] == self.cells[i][j] :
                        if (i - 1, j) not in liste_tuple:
                            liste_tuple.append((i - 1, j))
                            self.propagation(self, liste_tuple, (i - 1, j))
                    if self.cells[i][j + 1] == self.cells[i][j] :
                        if (i, j + 1) not in liste_tuple :
                            liste_tuple.append((i, j + 1))
                            self.propagation(self, liste_tuple, (i, j + 1))

                elif j >= self.size - 1 :

                    if self.cells[i - 1][j] == self.cells[i][j] :
                        if (i - 1, j) not in liste_tuple :
                            liste_tuple.append((i - 1, j))
                            self.propagation(self,liste_tuple, (i - 1, j))
                    if self.cells[i][j - 1] == self.cells[i][j] :
                        if (i, j - 1) not in liste_tuple :
                            liste_tuple.append((i, j - 1))
                            self.propagation(self ,liste_tuple, (i, j - 1))

                else :
                    if self.cells[i - 1][j] == self.cells[i][j] :
                        if (i - 1, j) not in liste_tuple :
                            liste_tuple.append((i - 1, j))
                            self.propagation(self, liste_tuple, (i - 1, j))
                    if self.cells[i][j - 1] == self.cells[i][j] :
                        if (i, j - 1) not in liste_tuple :
                            liste_tuple.append((i, j - 1))
                            self.propagation(self, liste_tuple, (i, j - 1))
                    if self.cells[i][j + 1] == self.cells[i][j] :
                        if (i, j + 1) not in liste_tuple :
                            liste_tuple.append((i, j + 1))
                            self.propagation(self, liste_tuple, (i, j + 1))

            else :
                if j <= 0:

                    if self.cells[i - 1][j] == self.cells[i][j] :
                        if (i - 1, j) not in liste_tuple :
                            liste_tuple.append((i - 1, j))
                            self.propagation(self, liste_tuple, (i - 1, j))
                    if self.cells[i + 1][j] == self.cells[i][j] :
                        if (i + 1, j) not in liste_tuple :
                            liste_tuple.append((i + 1, j))
                            self.propagation(self, liste_tuple, (i + 1, j))
                    if self.cells[i][j + 1] == self.cells[i][j] :
                        if (i, j + 1) not in liste_tuple :
                            liste_tuple.append((i, j + 1))
                            self.propagation(self, liste_tuple, (i, j + 1))

                elif j >= self.size - 1:

                    if self.cells[i - 1][j] == self.cells[i][j] :
                        if (i - 1, j) not in liste_tuple :
                            liste_tuple.append((i - 1, j))
                            self.propagation(self, liste_tuple, (i - 1, j))
                    if self.cells[i + 1][j] == self.cells[i][j] :
                        if (i + 1, j) not in liste_tuple :
                            liste_tuple.append((i + 1, j))
                            self.propagation(self, liste_tuple, (i + 1, j))
                    if self.cells[i][j - 1] == self.cells[i][j] :
                        if (i, j - 1) not in liste_tuple :
                            liste_tuple.append((i, j - 1))
                            self.propagation(self, liste_tuple, (i, j - 1))
                else:

                    if self.cells[i - 1][j] == self.cells[i][j]:
                        if (i - 1, j) not in liste_tuple:
                            liste_tuple.append((i - 1, j))
                            self.propagation(self, liste_tuple, (i - 1, j))
                    if self.cells[i + 1][j] == self.cells[i][j]:
                        if (i + 1, j) not in liste_tuple:
                            liste_tuple.append((i + 1, j))
                            self.propagation(self, liste_tuple, (i + 1, j))
                    if self.cells[i][j - 1] == self.cells[i][j]:
                        if (i, j - 1) not in liste_tuple:
                            liste_tuple.append((i, j - 1))
                            self.propagation(self, liste_tuple, (i, j - 1))
                    if self.cells[i][j + 1] == self.cells[i][j]:
                        if (i, j + 1) not in liste_tuple:
                            liste_tuple.append((i, j + 1))
                            self.propagation(self, liste_tuple, (i, j + 1))


    def modification(self , liste_tuple) : # fonction incrementer et pour mettre un 0 sur toutes cases adjacentes qu'on a trouvé
        x = liste_tuple[0][0]                   # recupere l'abcisse du premier tuple de la liste liste_tuple qui va correspondre a la case selectionné
        y = liste_tuple[0][1]                   # recupere l'ordonnée du premier tuple de la liste liste_tuple qui va correspondre a la case selection
        self.cells[x][y] += 1                      # incremente la case correspondante dans la grille qui est la case selectionnée
        for coordonnées in liste_tuple[ 1 : ] : # pour tous les autres elements de liste_tuple sauf le premier
            x = coordonnées[0]                  # recupere leur abscisse
            y = coordonnées[1]                  # recupere leur ordonnée
            self.cells[x][y] = 0                   # met un 0 a la case correspondante dans la grille

    def gravity(self) :            # pour deplacer les cases vers le bas s'il ya des 0 et ajouter de nouvelles valeurs aleatoires
        for i in range(self.size) :
            for j in range(self.size) :
                if self.cells[i][j] == 0 :
                    for element in reversed(range(i)) : # on parcours les i d'une case dont la valeur = 0 dans le sens inverse
                        self.cells[element+1][j] = self.cells[element][j] #on affecte sa valeur a une case en bas pour le faire descendre
                    self.cells[0][j] = self.aleatoire(self) # du coup la derniere case en haut n'aura rien et on y met une valeur aleatoire
                    
    def found_10(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.cells[i][j] >= 10:
                    return True
        return False


    def set_cells(self, cells):
        self.cells = cells

    def display(self):
        for i in range(self.size):
            cells = ""  # initialiser cells qui s'ecrase a chaque nouveau i
        for j in range(self.size):
            cells = cells + str(cells[i][
                                        j]) + " "  # faire la somme des des elements de la cells game[i] avec des espaces entre eux , str() permet de transformer un nombre en caractere
        print("*    ", cells, "     *") 


""" La classe de vue GUI du jeu Get10 montrant via tkinter """

class GUI:
    SIZE = 500
    marge_gauche = SIZE / 5      # une marge de gauche pour que ca colle pas a la fenetre
    marge_haut = SIZE / 5  
    game_LEN = 4
    game_PADDING = 10
    CELL_PADDING = 10
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
        self.root = tk.Tk()
        if sys.platform == 'win32':
            self.root.title('JustGet10')
            
        self.root.resizable(False, False)
        self.background = tk.Frame(self.root, bg=GUI.BACKGROUND_COLOR)
        self.cell_labels = []
        for i in range(self.game.size):
            row_labels = []
            for j in range(self.game.size):
                label = tk.Label(self.background, text='',
                                 justify=tk.CENTER, font=GUI.FONT,
                                 width=4, height=2)
                label.grid(row=i, column=j, padx=5, pady=5)
                row_labels.append(label)
            self.cell_labels.append(row_labels)
        self.background.pack(side=tk.TOP)
        self.start_cells_num = self.game.size
        self.root.bind("<Button-1>" , self.Leftclick)
        self.add_start_cells()
        self.paint()
        self.root.mainloop()
    
    
    def paint(self):
        for i in range(self.game.size):
            for j in range(self.game.size):
                    cell_text = str(self.game.cells[i][j])
                    if self.game.cells[i][j] > 10:
                        bg_color = GUI.CELL_BACKGROUND_COLOR_DICT.get('beyond')
                        fg_color = GUI.CELL_COLOR_DICT.get('beyond')
                    else:
                        bg_color = GUI.CELL_BACKGROUND_COLOR_DICT.get(cell_text)
                        fg_color = GUI.CELL_COLOR_DICT.get(cell_text)
                    self.cell_labels[i][j].configure(
                        text=cell_text,
                        bg=bg_color, fg=fg_color)
                    
    def add_start_cells(self):
        for i in range(self.start_cells_num):
            self.game.aleatoire()


    def Leftclick(self, event):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
        x = self.root.winfo_pointerx() - self.root.winfo_rootx()
        y = self.root.winfo_pointery() - self.root.winfo_rooty()
        taillex = self.marge_gauche + (self.game.size * GUI.CELL_PADDING)  #calcule la longueur de la grille + sa marge gauche
        tailley = self.marge_haut + (self.game.size* GUI.CELL_PADDING)    #calcule la hauteur de la grille + sa marge haut
        if x >= 0 and x < taillex and y >= 0 and y < tailley :  #test pour connaitre si on a cliqué a l'interieur de la grille
            i = int((y - self.marge_gauche)/GUI.CELL_PADDING)            # on calcule a partir du y de la souris(qui est en pixel ) le i de la case selectionnée
            j = int((x - self.marge_gauche) / GUI.CELL_PADDING)  
            current = (i, j)                                 # c'est la case selectionée
            L = [current]
            print(L)
        self.game.propagation(self ,tuple)                
        key_value = event.keysym
        print('{} Mouse Left Click Pressed'.format(key_value))
        if key_value in GUI.MOUSE_CLICK_LEFT:
            self.click()
        else:
            pass
        self.paint()
        print('Score: {}'.format(self.game.current_score))
        if self.game.found_10():
            return self.you_win()

    def click(self):
        if  self.game.existe_case_adj():
            self.game.modification()    #appelle procedure modification pour incrementer et mettre les 0
            self.game.gravity()     #appelle procedure gravity  
            self.game.display()  
    
    def you_win(self):
        if not self.won:
            self.won = True
            print('You Win!')
            if messagebox.askyesno('Get10Game', 'You Win!\n'
                                       'Are you going to continue the Get10Game game?'):
                self.keep_playing = True

    def game_over(self):
        print('Game over!')
        messagebox.showinfo('Get10Game', 'Oops!\n'
                                    'Game over!')
        
if __name__ == '__main__':
    size = 5
    game = game(size)
    panel = GUI(game)