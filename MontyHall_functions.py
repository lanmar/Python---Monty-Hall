# coding: utf-8

import numpy as np

def monty_hall(strategie, nb_tour):
    '''Simule une partie du jeu Monty Hall.
    
    Cette fonction simule le choix de la porte par le participant, 
    l'élimination d'une mauvaise porte par le présentateur, et le 
    choix final. 
    
    Args:
        strategie (Strategie): La stratégie du joueur, 0 pour GARDER et 1 pour CHANGER
        nb_tours (int): Nombre de tours     
        
    Returns:
        gain (tableau numpy): tableau Numpy des gains du joueur
    '''
    
    # nombre de porte dans le jeu
    nb_porte = 3
    
    # Construction de la matrice aléatoire des choix par tour. 
    #1 ligne = 1 tour
    premier_choix = np.random.randint(0, nb_porte, nb_tour)
    #print(premier_choix)
    
    # tableau des bonnes portes
    bonnes_portes = np.random.randint(0, nb_porte, nb_tour)
    #print(bonnes_portes)    
    
    # On compare le premier_choix du joueur et le tableau des bonnes portes et selon la stratégie :
    # 0-GARDER =  si la porte choisie est égale à la bonne porte, le joueur a gagné
    # 1-CHANGER = si la porte choisie est égale à la bonne porte, le joueur a perdu puisqu'il a décidé de 
    #             changer son choix. En revanche, si la porte choisie n'était pas la bonne porte, il gagne puisque
    #             en changeant il va tomber sur la bonne porte (le présentateur retirant systématiquement une
    #             mauvaise porte)
    
    gains = []
    if strategie == 'GARDER':
        gains = premier_choix == bonnes_portes
    elif strategie == 'CHANGER':
        # Quand je change je prend la bonne porte  si mon premier choix était faux
        gains = premier_choix != bonnes_portes
    else:
        raise ValueError("Stratégie non reconnue!")
    #print(gains)
    total_gains = sum(gains)
    #print(total_gains)
    return total_gains
  

def play(strategie, nb_tours) :
    '''Simule une partie du jeu Monty Hall.
    
    Cette fonction simule le choix de la porte par le participant, 
    l'élimination d'une mauvaise porte par le présentateur, et le 
    choix final. Elle renvoie les résultats de plusieurs parties sous 
    forme d'un tableau.
    
    Args:
        strategie : La stratégie du joueur ("CHANGER" ou "GARDER")
        nb_tours : le nombre de parties qui sont jouées
        
    Returns:
        array: pour chaque tour 1 si le joueur a gagné et 0 s'il a perdu
    '''
    
    gains = np.arange(0,nb_tours)
    i = 0
    
    while i < nb_tours :
           
        portes = [0, 1, 2]

        bonne_porte = np.random.randint(3, size=1)

        # Choix du joueur
        premier_choix = np.random.randint(3, size=1)

        # Il nous reste deux portes
        portes.remove(premier_choix)

        # Le présentateur élimine une porte
        porte_eliminee = np.random.randint(2, size=1)[0]
        if premier_choix == bonne_porte:
            portes.remove(portes[porte_eliminee])
        else:
            portes = [bonne_porte]    

        deuxieme_choix = 0
        # Le deuxieme choix depend de la strategie
        if strategie == "CHANGER":
            deuxieme_choix = portes[0]
        elif strategie == "GARDER" :
            deuxieme_choix = premier_choix
        else:
            raise ValueError("Stratégie non reconnue!")

        gains[i] = 1 if deuxieme_choix == bonne_porte  else 0
        i = i +1

    return gains