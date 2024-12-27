# Noms : Eva Delarue et Kenny Ly

from tkinter import *
from PIL import ImageTk, Image
import pygame
import random
import time
from datetime import datetime

# Variables globales:
table_nombre_choisi = None
prenom = None
nom = None
gratinee = None
serveur = random.choice(["Eva", "Kenny", "Marine", "Kevin"])
padding_y = 51
liste_achats = []
servir_bouton_activation = False
prix = {"soupe" : 15.50, "croquettes" : 12.00, "poisson" : 28.00, "steak" : 35.00, "café" : 4.50, "quart de gateau" : 7.50}

# Étape 1 : la réservation
def etape_1():
    '''Entre les données du client et effectue une réservation'''
    global prenom
    global nom

    boucle = True
    while boucle:
        noms = input("Quel était le prénom et nom pour la réservation? ")    # Demande les informations dans la console
        liste_noms = noms.split()

        # Traitement d'erreurs
        if len(liste_noms) == 2:
            if liste_noms[0].isalpha() == True and liste_noms[1].isalpha() == True:
                boucle = False

    prenom = liste_noms[0]      # Sauvegarde des informations dans 2 variables globales
    nom = liste_noms[1]

# Étape 2 : la confirmation
def etape_2():
    '''Confirme la réservation avec le prénom et nom du client, ainsi que lui assigne une table aléatoire.'''
    global table_nombre_choisi

    pygame.init()

    ECRAN = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Confirmation de la réservation")

    ECRAN.fill("light grey")
    police = pygame.font.SysFont("Calibri", 20)  # Police de tous les textes de l'étape
    police_epaisse = pygame.font.SysFont("Calibri", 25, bold=True)  # Police des titres de l'étape

    coordonnees_bouton_valider = pygame.Rect(65,335,100,30)    # Création du bouton VALIDER
    bouton_valider_surface = pygame.Surface((coordonnees_bouton_valider.width, coordonnees_bouton_valider.height))

    coordonnees_bouton_sassoir = pygame.Rect(290, 390, 120, 30)     # Création du bouton S'ASSOIR
    bouton_sassoir_surface = pygame.Surface((coordonnees_bouton_sassoir.width, coordonnees_bouton_sassoir.height))

    # Tous les textes affichés sur l'écran
    texte_bouton_valider = police.render("VALIDER", 0, (0,0,0))
    texte_bouton_sassoir = police.render("S'ASSOIR", 0, (0,0,0))
    texte_prenom = police.render("PRÉNOM", 0, (0,0,0))
    texte_nom = police.render("NOM", 0, (0,0,0))
    texte_gauche_ligne_1 = police_epaisse.render("CONFIRMATION", 0, (0,0,0))
    texte_gauche_ligne_2 = police_epaisse.render("INFOS CLIENT", 0, (0,0,0))
    texte_droite = police_epaisse.render("TABLES DISPONIBLES", 0, (0,0,0))

    # Création des 9 tables, avec leur coordonnées, leur numéro affiché, et leur affichage
    table1 = pygame.Rect(230, 120, 60, 60)
    texte1 = police_epaisse.render("1", 0, (255, 255, 255))
    coord1 = (254, 140)
    pygame.draw.rect(ECRAN, (140, 140, 140), table1)
    ECRAN.blit(texte1, coord1)

    table2 = pygame.Rect(320, 120, 60, 60)
    texte2 = police_epaisse.render("2", 0, (255, 255, 255))
    coord2 = (344, 140)
    pygame.draw.rect(ECRAN, (140, 140, 140), table2)
    ECRAN.blit(texte2, coord2)

    table3 = pygame.Rect(410, 120, 60, 60)
    texte3 = police_epaisse.render("3", 0, (255, 255, 255))
    coord3 = (434, 140)
    pygame.draw.rect(ECRAN, (140, 140, 140), table3)
    ECRAN.blit(texte3, coord3)

    table4 = pygame.Rect(230, 210, 60, 60)
    texte4 = police_epaisse.render("4", 0, (255, 255, 255))
    coord4 = (254, 230)
    pygame.draw.rect(ECRAN, (140, 140, 140), table4)
    ECRAN.blit(texte4, coord4)

    table5 = pygame.Rect(320, 210, 60, 60)
    texte5 = police_epaisse.render("5", 0, (255, 255, 255))
    coord5 = (344, 230)
    pygame.draw.rect(ECRAN, (140, 140, 140), table5)
    ECRAN.blit(texte5, coord5)

    table6 = pygame.Rect(410, 210, 60, 60)
    texte6 = police_epaisse.render("6", 0, (255, 255, 255))
    coord6 = (434, 230)
    pygame.draw.rect(ECRAN, (140, 140, 140), table6)
    ECRAN.blit(texte6, coord6)

    table7 = pygame.Rect(230, 300, 60, 60)
    texte7 = police_epaisse.render("7", 0, (255, 255, 255))
    pygame.draw.rect(ECRAN, (140, 140, 140), table7)
    coord7 = (254, 320)
    ECRAN.blit(texte7, coord7)

    table8 = pygame.Rect(320, 300, 60, 60)
    texte8 = police_epaisse.render("8", 0, (255, 255, 255))
    pygame.draw.rect(ECRAN, (140, 140, 140), table8)
    coord8 = (344, 320)
    ECRAN.blit(texte8, coord8)

    table9 = pygame.Rect(410, 300, 60, 60)
    texte9 = police_epaisse.render("9", 0, (255, 255, 255))
    pygame.draw.rect(ECRAN, (140, 140, 140), table9)
    coord9 = (434, 320)
    ECRAN.blit(texte9, coord9)

    entree_prenom = ""      # Texte des champs d'entrée
    entree_nom = ""

    active_prenom = False     # Zones de champs d'entrée/de boutons non actives au départ
    active_nom = False
    active_valider = False

    LANCEMENT = True

    def affiche_table():
        '''Fonction qui change la couleur de la table choisie aléatoirement en vert.'''
        global table_nombre_choisi

        # Dictionnaire des numéros associés aux rectangles ainsi qu'aux coordonnées de chaque table respective
        dictio_tables = {"1": (table1, coord1), "2": (table2, coord2), "3": (table3, coord3), "4": (table4, coord4),
                         "5": (table5, coord5), "6": (table6, coord6), "7": (table7, coord7), "8": (table8, coord8),
                         "9": (table9, coord9)}

        table_nombre_choisi = random.choice(list(dictio_tables.keys()))    # Choix aléatoire d'une table
        table_coord_choisie = dictio_tables[table_nombre_choisi][0]     # Coordonnées du numéro associé à la table choisie
        nouveau_texte = police_epaisse.render(table_nombre_choisi, 0, (0,0,0))   # Numéro apparaissant au-dessus du vert
        pygame.draw.rect(ECRAN, (154, 249, 148), table_coord_choisie)    # Affichage de la table en vert
        ECRAN.blit(nouveau_texte, dictio_tables[table_nombre_choisi][1])     # Affichage du numéro en noir




    while LANCEMENT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LANCEMENT = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # Si la souris est cliquée
                if coordonnees_champ_prenom.collidepoint(event.pos):  # Si le clic est dans la zone de texte du prénom
                    active_prenom = True
                    active_nom = False     # On désactive la zone de texte du nom
                elif coordonnees_champ_nom.collidepoint(event.pos):   # Si le clic est dans la zone de texte du nom
                    active_nom = True
                    active_prenom = False  # On désactive la zone de texte du prénom
                else:    # Si le clic est dans aucune des zones de texte
                    active_prenom = False
                    active_nom = False

                if coordonnees_bouton_valider.collidepoint(event.pos):  # Si on clique sur le bouton VALIDER
                    if entree_prenom == prenom and entree_nom == nom:   # Si les informations entrées sont les bonnes
                        affiche_table() # Lancement de la fonction qui affiche la table au hasard
                        active_valider = True   # Le clic est gardé en mémoire et permet d'activer S'ASSOIR

                if coordonnees_bouton_sassoir.collidepoint(event.pos):  # Si on clique sur le bouton S'ASSOIR
                    if active_valider == True:    # Si on a d'abord cliqué sur le bouton VALIDER

                        LANCEMENT = False # Fermeture de la fenêtre

            if event.type == pygame.KEYDOWN:  # Lorsque le clavier est utilisé
                if active_prenom == True:  # Si on a cliqué sur le champ de texte du prénom
                    if surface_texte_prenom.get_width() <= 100:  # On limite la largeur du texte à 110 pixels.
                        if event.key == pygame.K_BACKSPACE:  # Si la touche BACKSPACE est utilisée
                            entree_prenom = entree_prenom[0:-1]  # Le dernier caractère de l'entrée est effacé
                        else:
                            entree_prenom += event.unicode  # On ajoute le nouveau caractère au texte actuel

                    if surface_texte_prenom.get_width() >= 100:  # Si le texte fait plus de 110 pixels
                        if event.key == pygame.K_BACKSPACE:  # Seulement la touche BACKSPACE est efficace
                            entree_prenom = entree_prenom[0:-1]

                if active_nom == True:  # Si on a cliqué sur le champ de texte du nom
                    if surface_texte_nom.get_width() <= 100:  # On limite la largeur du texte à 110 pixels.
                        if event.key == pygame.K_BACKSPACE:  # Si la touche BACKSPACE est utilisée
                            entree_nom = entree_nom[0:-1]  # Le dernier caractère de l'entrée est effacé
                        else:
                            entree_nom += event.unicode  # On ajoute le nouveau caractère au texte actuel

                    if surface_texte_nom.get_width() >= 100:  # Si le texte fait plus de 110 pixels
                        if event.key == pygame.K_BACKSPACE:  # Seulement la touche BACKSPACE est efficace
                            entree_nom = entree_nom[0:-1]

        surface_texte_prenom = police.render(entree_prenom, 0, (0, 0, 0))  # Rendering de la surface de texte du prénom
        surface_texte_nom = police.render(entree_nom, 0, (0,0,0)) # Rendering de la surface de texte du nom

        ECRAN.blit(texte_gauche_ligne_1, (35, 115))
        ECRAN.blit(texte_gauche_ligne_2, (45, 140))
        ECRAN.blit(texte_droite, (243, 80))

        coordonnees_champ_prenom = pygame.Rect(55, 205, 120, 30)  # Coordonnées du champ d'entrée du prénom
        ECRAN.blit(texte_prenom, (55, 180))
        pygame.draw.rect(ECRAN, "white", coordonnees_champ_prenom)  # Affichage du champ d'entrée

        coordonnees_champ_nom = pygame.Rect(55, 275, 120, 30)
        ECRAN.blit(texte_nom, (55, 252))
        pygame.draw.rect(ECRAN, "white", coordonnees_champ_nom)

        ECRAN.blit(bouton_valider_surface, coordonnees_bouton_valider)  # Affichage du fond du bouton
        bouton_valider_surface.fill("grey")

        ECRAN.blit(bouton_sassoir_surface, coordonnees_bouton_sassoir)
        bouton_sassoir_surface.fill("grey")


        ECRAN.blit(surface_texte_prenom, (coordonnees_champ_prenom.x + 5, coordonnees_champ_prenom.y + 6))

        ECRAN.blit(surface_texte_nom,(coordonnees_champ_nom.x + 5, coordonnees_champ_nom.y + 6))

        ECRAN.blit(texte_bouton_valider, (82, 341))
        ECRAN.blit(texte_bouton_sassoir, (315, 397))

        pygame.display.update()

    pygame.quit()

# Étape 3 : la présentation du menu
def etape_3():
    '''Présente le menu du restaurant'''
    fenetre = Tk()  # création d’une fenêtre de type Tkinter
    fenetre.title("Menu")  # affiche le titre de la fenêtre

    fenetre.geometry("500x500")  # méthode pour la taille de la fenêtre Tkinter
    fenetre.minsize(500, 500)  # méthode pour baliser la réduction de taille la fenêtre
    fenetre.maxsize(500, 500)  # méthode pour baliser l’agrandissement de taille la fenêtre

    # Entrées
    entrees_annonce = Label(fenetre, text="Entrées au choix", font=("Courier", 18, "bold", "underline"))    # Titre entrée
    entrees_annonce.pack(pady=(50, 0))
    entree_1 = Label(fenetre, text="#1 Soupe à l’oignon non gratinée, gratinée (extra 2$), 15.50$",
                     font=("Calibri", 12))      # Choix d'entrée numéro 1
    entree_1.pack()
    entree_2 = Label(fenetre, text="#2 Croquettes de thon, 12.00$", font=("Calibri", 12))   # Choix d'entrée numéro 2
    entree_2.pack()

    # Repas
    repas_annonce = Label(fenetre, text="Repas au choix", font=("Courier", 18, "bold", "underline"))    # Titre repas
    repas_annonce.pack(pady=(20, 0))
    repas_1 = Label(fenetre, text="#1 Poisson avec des pommes de terre, 28.00$", font=("Calibri", 12)) # Choix de repas numéro 1
    repas_1.pack()
    repas_2 = Label(fenetre, text="#2 Steak avec des légumes du jardin, 35.00$", font=("Calibri", 12)) # Choix de repas numéro 2
    repas_2.pack()

    # Desserts
    dessert_annonce = Label(fenetre, text="Desserts au choix", font=("Courier", 18, "bold", "underline"))   # Titre dessert
    dessert_annonce.pack(pady=(20, 0))
    dessert_1 = Label(fenetre, text="#1 Café, 4.50$", font=("Calibri", 12))     # Choix de dessert numéro 1
    dessert_1.pack()
    dessert_2 = Label(fenetre, text="#2 Un quart de gâteau au fromage, 7.50$", font=("Calibri", 12))    # Choix de dessert numéro 2
    dessert_2.pack()

    # Bouton pour fermer la fenêtre et passer à la prochaine étape
    def close_window():
        fenetre.destroy()   # Ferme la fenêtre

    commander_bouton = Button(fenetre, text="COMMANDER", font=("Calibri", 18), command=close_window)
    commander_bouton.pack(pady=40)

    fenetre.mainloop()  # gestionnaire de la boucle de Tkinter

# Étape 4 : la prise de la commande
def etape_4():
    '''Un serveur prend en note ce que le client commande'''
    global serveur
    global padding_y
    global liste_achats
    global servir_bouton_activation

    fenetre = Tk()  # création d’une fenêtre de type Tkinter
    fenetre.title("Menu")  # affiche le titre de la fenêtre

    fenetre.geometry("500x500")  # méthode pour la taille de la fenêtre Tkinter
    fenetre.minsize(500, 500)  # méthode pour baliser la réduction de taille la fenêtre
    fenetre.maxsize(500, 500)  # méthode pour baliser l’agrandissement de taille la fenêtre


    '''Côté Gauche'''
    # Vérification de validité
    def check_valid(liste_reponse_valide, champ_text, button):
        '''Fonction qui vérifie la validité du texte qui est entré. Elle prend une liste des réponses valides, le texte entré dans
        le champ de texte et le bouton cliqué.'''
        global padding_y
        global liste_achats
        global servir_bouton_activation

        if champ_text.get() in liste_reponse_valide:
            bloc_note_texte = Label(fenetre, text="Vous avez commandé : " + champ_text.get(), font=("Calibri", 10))    # Écrit les paroles du serveur
            bloc_note_texte.place(relx=0.55, y=padding_y)   # Place ce que le serveur dit à la droite
            liste_achats.append(champ_text.get())      # Ajoute l'option que le client choisi dans une liste
            padding_y += 18     # Incrémente sur l'axe des y pour que les lignes soient bien espacées.

            button.destroy()    # Supprimation du bouton utilisé pour éviter des doubles commandes

            if champ_text.get() == "croquettes":
                # Si l'entrée choisi sont des croquettes, on va supprimer l'option pour le gratinée
                gratin_confirm.destroy()    # Supprimation du bouton gratinée
                entree_text_gratin.destroy()    # Supprimation du champ de texte pour le gratinée
                label_gratin.destroy()      # Supprimation du texte qui présente le gratinée

            if len(liste_achats) == 4:
                '''Si le client a terminé de commander (on ignore la possibilité d'un client qui commande du gratinée
                avant de commander une croquette pour l'instant. On va gérer ce cas dans l'étape 5)'''
                padding_y += 18     # Incrémente sur l'axe des y pour que les lignes soient bien espacées
                conclusion_texte = Label(fenetre, text="Merci, ça ne sera pas long!", font=("Calibri", 10))     # Texte qui conclut la commande
                conclusion_texte.place(relx=0.55, y=padding_y)  # Place le texte de conclusion
                servir_bouton_activation = True     # Activation du bouton 'SERVIR' pour passer à la prochaine étape

            elif len(liste_achats) == 3 and "croquettes" in liste_achats and "gratinée" not in liste_achats and "non gratinée"\
                    not in liste_achats:
                '''Si le client a terminé de commander tous les items'''
                padding_y += 18  # Incrémente sur l'axe des y pour que les lignes soient bien espacées
                conclusion_texte = Label(fenetre, text="Merci, ça ne sera pas long!", font=("Calibri", 10))  # Texte qui conclut la commande
                conclusion_texte.place(relx=0.55, y=padding_y)  # Place le texte de conclusion
                servir_bouton_activation = True  # Activation du bouton 'SERVIR' pour passer à la prochaine étape

        else:
            bloc_note_texte = Label(fenetre, text="Choix invalide", font=("Calibri", 10))   # Texte d'avertissement si le client rentre un choix invalide
            bloc_note_texte.place(relx=0.55, y=padding_y)   # Placement de l'avertissement


    # Entrées
    label_entree = Label(fenetre, text="Entrée #1 (soupe) ou #2 (croquettes) ?", font=("Calibri", 10, "underline"))     # Texte au dessus du champ d'entrée
    label_entree.place(relx=0.25, y=30, anchor=CENTER)

    entree_text_entree = Entry(fenetre, font=("Calibri", 10))
    entree_text_entree.place(relx=0.25, y=50, anchor=CENTER)

    entree_confirm = Button(fenetre, text="Confirmer", font=("Calibri", 10),
                            command= lambda: check_valid(["soupe", "croquettes"], entree_text_entree, entree_confirm))
    entree_confirm.place(relx=0.25, y=75, anchor=CENTER)


    # Gratinée
    label_gratin = Label(fenetre, text="Si entrée #1, gratinée ou non gratinée ?", font=("Calibri", 10, "underline"))     # Texte au dessus du champ d'entrée 'entrée'
    label_gratin.place(relx=0.25, y=110, anchor=CENTER)

    entree_text_gratin = Entry(fenetre, font=("Calibri", 10))   # Champ d'entrée pour les entrées
    entree_text_gratin.place(relx=0.25, y=130, anchor=CENTER)

    gratin_confirm = Button(fenetre, text="Confirmer", font=("Calibri", 10),
                           command=lambda: check_valid(["gratinée", "non gratinée"], entree_text_gratin, gratin_confirm))       # Bouton de confirmation pour les entrées
    gratin_confirm.place(relx=0.25, y=155, anchor=CENTER)


    # Repas
    label_repas = Label(fenetre, text="Repas #1 (poisson) ou #2 (steak) ?", font=("Calibri", 10, "underline"))     # Texte au dessus du champ d'entrée 'repas'
    label_repas.place(relx=0.25, y=210, anchor=CENTER)

    entree_text_repas = Entry(fenetre, font=("Calibri", 10))    # Champ d'entrée pour les repas
    entree_text_repas.place(relx=0.25, y=230, anchor=CENTER)

    repas_confirm = Button(fenetre, text="Confirmer", font=("Calibri", 10),
                           command=lambda: check_valid(["poisson", "steak"], entree_text_repas, repas_confirm))     # Bouton de confirmation pour les repas
    repas_confirm.place(relx=0.25, y=255, anchor=CENTER)


    # Dessert
    label_dessert = Label(fenetre, text="Dessert #1 (café) ou #2 (quart de gateau) ?", font=("Calibri", 10, "underline"))   # Texte au dessus du champ d'entrée 'dessert'
    label_dessert.place(relx=0.25, y=280, anchor=CENTER)

    entree_text_dessert = Entry(fenetre, font=("Calibri", 10))      # Champ d'entrée pour les desserts
    entree_text_dessert.place(relx=0.25, y=300, anchor=CENTER)

    dessert_confirm = Button(fenetre, text="Confirmer", font=("Calibri", 10),
                             command=lambda: check_valid(["café", "quart de gateau"], entree_text_dessert, dessert_confirm))    # Bouton de confirmation pour les desserts
    dessert_confirm.place(relx=0.25, y=325, anchor=CENTER)



    '''Côté droit'''
    introduction = Label(fenetre, text="Bonjour, je m'appelle {} et je serai ".format(serveur), font=("Calibri", 10))   # Présentation du serveur
    introduction2 = Label(fenetre, text="votre serveur aujourd'hui.", font=("Calibri", 10))
    introduction.place(relx=0.55, y=15)
    introduction2.place(relx=0.55, y=33)

    # Ligne séparatrice
    mon_canevas = Canvas(width=3, height=450)
    mon_canevas.pack()
    mon_canevas.create_line(3, 0, 3, 450, fill="black", width=3, dash=True) # Dessin d'une ligne qui sépare la commande et la conversation

    # Bouton pour fermer la fenêtre
    def close_window():
        if servir_bouton_activation == True:    # Le bouton ne fonctionne que si la commande est complète
            fenetre.destroy()
    servir_bouton = Button(fenetre, text="SERVIR", font=("Calibri", 18), command=close_window)
    servir_bouton.pack(side="bottom")

    fenetre.mainloop()  # gestionnaire de la boucle de Tkinter

# Étape 5 : mangez!
def etape_5():
    global liste_achats

    # Si le client a entré la soupe comme gratinée et qu'il a commandé une soupe
    if "gratinée" in liste_achats and "soupe" in liste_achats:
        liste_achats.remove("gratinée")
        gratinee = True

    # Si le client a entré la soupe comme gratinée et qu'il n'a pas commandé de soupe
    if "gratinée" in liste_achats and "soupe" not in liste_achats:
        liste_achats.remove("gratinée")
        gratinee = False

    # Si le client a entré la soupe comme non gratinée (peu importe s'il en a commandé une ou non)
    if "non gratinée" in liste_achats:
        liste_achats.remove("non gratinée")
        gratinee = False

    increment = -1
    pygame.init()

    ECRAN = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Présentation des plats")
    ECRAN.fill((255, 255, 255))  # Couleur de l'arrière-plan en blanc

    def soupe():      # Fonction qui dessine la soupe (gratinée/non gratinée)
        ECRAN.fill((255, 255, 255))
        background = pygame.Surface(ECRAN.get_size())  # Creation d'une surface couvrant l'entierté de l'ECRAN
        background.fill("#954723")      # Remplit le background au complet du brun de la soupe

        for i in range(600):    # On dessine 600 oignons de tailles variées d'une certaine couleur
            pygame.draw.arc(background, "#9C5E3C", (random.randint(0, 500), random.randint(0, 500),
                                                    random.randint(35, 75), random.randint(35, 75)),
                            random.randint(0, 6),
                            random.randint(0, 6), width=random.randint(3, 6))

        for i in range(300):    # On en dessine 300 par-dessus d'une couleur plus claire
            pygame.draw.arc(background, "#C4814E", (random.randint(0, 500), random.randint(0, 500),
                                                    random.randint(35, 75), random.randint(35, 75)),
                            random.randint(0, 6),
                            random.randint(0, 6), width=random.randint(3, 6))

        if gratinee == True:    # Si la soupe est gratinée
            background.fill("#EDC958")    # Remplit le background au complet d'un jaune pour le fromage gratiné

            for i in range(1000):    # On dessine 1000 cercles de tailles variées d'une certaine couleur
                pygame.draw.circle(background, "#F5AC5B", (random.randint(0, 500), random.randint(0, 500)),
                                   random.randint(5, 15), width=0)
            for i in range(100):     # On dessine 100 oignons pour ajouter du potentiel relief sous le fromage
                pygame.draw.arc(background, "#C4814E", (random.randint(0, 500), random.randint(0, 500),
                                                        random.randint(35, 75), random.randint(35, 75)),
                                random.randint(0, 6),
                                random.randint(0, 6), width=random.randint(3, 6))

            for i in range(700):    # On dessine 700 cercles d'une couleur plus claire pour donner un effet de relief
                pygame.draw.circle(background, "#F4D177", (random.randint(0, 500), random.randint(0, 500)),
                                   random.randint(5, 15), width=0)

            for i in range(500):    # On en dessine 500 encore plus clair
                pygame.draw.circle(background, "#F9DA9B", (random.randint(0, 500), random.randint(0, 500)),
                                   random.randint(5, 15), width=0)

            for i in range(400):    # On répète le processus
                pygame.draw.circle(background, "#FADD9C", (random.randint(0, 500), random.randint(0, 500)),
                                   random.randint(5, 15), width=0)

            for i in range(300):    # On répète le processus
                pygame.draw.circle(background, "#FADEAC", (random.randint(0, 500), random.randint(0, 500)),
                                   random.randint(5, 15), width=0)

            for i in range(200):    # On répète le processus
                pygame.draw.circle(background, "#FEE4C2", (random.randint(0, 500), random.randint(0, 500)),
                                   random.randint(5, 15), width=0)


        # On dessine les cercles qui représentent le bol
        pygame.draw.circle(background, "light grey", (250, 250), 150, 20)
        pygame.draw.circle(background, "#EDEEF2", (250, 250), 150, 5)

        '''PLUGIN NUMÉRO 1: Masque utilisant la transparence pour encadrer la soupe d'onion dans le bol'''
        size = background.get_size()    # Trouve la taille du background

        # Surface ALPHA (qui prend en compte la transparence) de couleur (0,0,0,0) où le dernier zéro représente
        # une opacité de 0 (donc complètement transparent) qui couvre l'entierete de l'ECRAN
        cropped_background = pygame.Surface(size, pygame.SRCALPHA)

        # Trace une ellipse complètement blanche (r, g, b, d'opacité maximale) sur la surface ALPHA. Représente l'intérieur du bol
        pygame.draw.ellipse(cropped_background, (255, 255, 255, 255), (100, 100, 300, 300))

        # Dessine la surface ALPHA sur la surface background avec le special flag qu'on choisi toujours le r, g, b et
        # alpha (opacité) le plus bas dans un pixel donné. Donc, quand on est à l'extérieur de l'ellipse, c'est du noir
        # complètement transparent. Quand on est à l'intérieur de l'ellipse, c'est la couleur de la soupe complètement opaque.
        cropped_background.blit(background, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

        ECRAN.blit(cropped_background, (0, 0))  # Place la soupe encadré par le bol sur l'écran

    def croquettes():     # Fonction qui dessine les croquettes
        ECRAN.fill((255, 255, 255))

        # Dessin de l'assiette
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 170, 40)
        pygame.draw.circle(ECRAN, "light grey", (250, 250), 150, 5)
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 130, 0)

        # Dessin des croquettes
        pygame.draw.circle(ECRAN, "#EAA763", (272, 275), 35, 0)
        pygame.draw.circle(ECRAN, "#EAA763", (315, 222), 35, 0)
        pygame.draw.circle(ECRAN, "#EAA763", (237, 218), 35, 0)
        pygame.draw.circle(ECRAN, "#EAA763", (205, 285), 35, 0)
        pygame.draw.circle(ECRAN, "#EAA763", (267, 342), 35, 0)
        pygame.draw.circle(ECRAN, "#EAA763", (337, 295), 35, 0)

        # Dessin du citron
        pygame.draw.arc(ECRAN, "#FCDD59", (115, 190, 70, 70), 1.57, 4.71, 40)
        pygame.draw.circle(ECRAN, "#FCDD59", (120, 225), 10, 0)
        pygame.draw.ellipse(ECRAN, "#FAFAEE", (135, 190, 30, 70), 0)
        pygame.draw.ellipse(ECRAN, "#FCE4B5", (140, 195, 20, 60), 0)
        pygame.draw.line(ECRAN, "#FAFAEE", (149, 190), (149, 260), 1)
        pygame.draw.line(ECRAN, "#FAFAEE", (135, 225), (165, 225), 1)
        pygame.draw.line(ECRAN, "#FAFAEE", (142, 207), (157, 242), 1)
        pygame.draw.line(ECRAN, "#FAFAEE", (142, 242), (157, 207), 1)

        # Dessin des sauces
        pygame.draw.circle(ECRAN, "#CCD7F0", (275, 145), 37, 0)
        pygame.draw.circle(ECRAN, "#FCEBD2", (275, 145), 30, 0)
        pygame.draw.circle(ECRAN, "#CCD7F0", (190, 155), 37, 0)
        pygame.draw.circle(ECRAN, "#8C2E24", (190, 155), 30, 0)

    def poisson():     # Fonction qui dessine le poisson
        ECRAN.fill((255, 255, 255))

        # Dessin de l'assiette
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 170, 40)
        pygame.draw.circle(ECRAN, "light grey", (250, 250), 150, 5)
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 130, 0)


        # Dessin de la sauce sous le poisson et du poisson
        pygame.draw.circle(ECRAN, "#FCEBD2", (270, 270), 105, 0)
        pygame.draw.polygon(ECRAN, "#C39476", ((285, 183), (340, 195), (333, 223), (320, 248), (305, 273),
                                               (300, 288), (295, 298), (290, 303), (281, 318), (270, 335), (263, 349),
                                               (255, 358), (246, 359), (240, 361), (237, 359), (232, 359), (227, 354),
                                               (220, 348), (210, 342), (198, 336), (203, 320)))
        pygame.draw.polygon(ECRAN, "#4F4538", ((285, 183), (340, 195), (340, 200), (250, 355), (200, 323), (200, 320)),0)
        pygame.draw.polygon(ECRAN, "#635B50", ((285, 183), (340, 195), (250, 350), (200, 320)), 0)

        # Dessin du citron
        pygame.draw.arc(ECRAN, "#FCDD59", (125, 275, 70, 70), 1.57, 4.71, 40)
        pygame.draw.circle(ECRAN, "#FCDD59", (130, 310), 10, 0)
        pygame.draw.ellipse(ECRAN, "#FAFAEE", (145, 275, 30, 70), 0)
        pygame.draw.ellipse(ECRAN, "#FCE4B5", (150, 280, 20, 60), 0)
        pygame.draw.line(ECRAN, "#FAFAEE", (159, 275), (159, 345), 1)
        pygame.draw.line(ECRAN, "#FAFAEE", (145, 310), (175, 310), 1)
        pygame.draw.line(ECRAN, "#FAFAEE", (152, 292), (167, 327), 1)
        pygame.draw.line(ECRAN, "#FAFAEE", (152, 327), (167, 292), 1)

        # Dessin de toutes les pommes de terre (commentaires donnent l'orientation de chaque pomme de terre)

        # Vertical vers la gauche
        pygame.draw.arc(ECRAN, "#A67822", (140, 155, 40, 40), 1.57, 4.71, 40)
        pygame.draw.arc(ECRAN, "#A67822", (140, 155, 40, 40), 1.56, 4.70, 50)
        pygame.draw.ellipse(ECRAN, "#D9B44A", (153, 155, 15, 40), 0)

        pygame.draw.arc(ECRAN, "#BB861C", (210, 185, 40, 40), 1.57, 4.71, 40)
        pygame.draw.arc(ECRAN, "#BB861C", (210, 185, 40, 40), 1.58, 4.70, 50)
        pygame.draw.ellipse(ECRAN, "#DDAE42", (223, 185, 15, 40), 0)

        pygame.draw.arc(ECRAN, "#BC8A45", (190, 225, 40, 40), 1.57, 4.71, 40)
        pygame.draw.arc(ECRAN, "#BC8A45", (190, 225, 40, 40), 1.58, 4.70, 50)
        pygame.draw.ellipse(ECRAN, "#DDAE42", (203, 225, 15, 40), 0)

        pygame.draw.arc(ECRAN, "#BC8A45", (110, 235, 40, 40), 1.57, 4.71, 40)
        pygame.draw.arc(ECRAN, "#BC8A45", (110, 235, 40, 40), 1.58, 4.70, 50)
        pygame.draw.ellipse(ECRAN, "#DDAE42", (123, 235, 15, 40), 0)

        # Horizontal vers le bas
        pygame.draw.arc(ECRAN, "#BC8A35", (170, 125, 40, 40), 0, 3.14, 40)
        pygame.draw.arc(ECRAN, "#BC8A35", (170, 125, 40, 40), 0.01, 3.13, 50)
        pygame.draw.ellipse(ECRAN, "#DEBE73", (170, 138, 40, 15), 0)

        pygame.draw.arc(ECRAN, "#996342", (195, 175, 40, 40), 0, 3.14, 40)
        pygame.draw.arc(ECRAN, "#996342", (195, 175, 40, 40), 0.01, 3.13, 50)
        pygame.draw.ellipse(ECRAN, "#B87F49", (195, 188, 40, 15), 0)

        pygame.draw.arc(ECRAN, "#8C5B37", (125, 215, 40, 40), 0, 3.14, 40)
        pygame.draw.arc(ECRAN, "#8C5B37", (125, 215, 40, 40), 0.01, 3.13, 50)
        pygame.draw.ellipse(ECRAN, "#BF8B4F", (125, 228, 40, 15), 0)

        pygame.draw.arc(ECRAN, "#BC8A45", (120, 185, 40, 40), 0, 3.14, 40)
        pygame.draw.arc(ECRAN, "#BC8A45", (120, 185, 40, 40), 0.01, 3.13, 50)
        pygame.draw.ellipse(ECRAN, "#DCB677", (120, 198, 40, 15), 0)

        # Vertical vers la droite
        pygame.draw.arc(ECRAN, "#BC8A45", (140, 215, 40, 40), 4.71, 1.57, 40)
        pygame.draw.arc(ECRAN, "#BC8A45", (140, 215, 40, 40), 4.72, 1.56, 50)
        pygame.draw.ellipse(ECRAN, "#DCB677", (153, 215, 15, 40), 0)

        pygame.draw.arc(ECRAN, "#8C5B37", (170, 160, 40, 40), 4.71, 1.57, 40)
        pygame.draw.arc(ECRAN, "#8C5B37", (170, 160, 40, 40), 4.72, 1.56, 50)
        pygame.draw.ellipse(ECRAN, "#BF8B4F", (183, 160, 15, 40), 0)

        pygame.draw.arc(ECRAN, "#BB861C", (200, 120, 40, 40), 4.71, 1.57, 40)
        pygame.draw.arc(ECRAN, "#BB861C", (200, 120, 40, 40), 4.72, 1.56, 50)
        pygame.draw.ellipse(ECRAN, "#DEBE73", (213, 120, 15, 40), 0)

        pygame.draw.arc(ECRAN, "#BB861C", (230, 160, 40, 40), 4.71, 1.57, 40)
        pygame.draw.arc(ECRAN, "#BB861C", (230, 160, 40, 40), 4.72, 1.56, 50)
        pygame.draw.ellipse(ECRAN, "#DEBE73", (243, 160, 15, 40), 0)

        # Horizontal vers le haut
        pygame.draw.arc(ECRAN, "#BB861C", (230, 125, 40, 40), 3.14, 0, 40)
        pygame.draw.arc(ECRAN, "#BB861C", (230, 125, 40, 40), 3.15, 6.27, 50)
        pygame.draw.ellipse(ECRAN, "#DEBE73", (230, 138, 40, 15), 0)

        pygame.draw.arc(ECRAN, "#8C5B37", (200, 205, 40, 40), 3.14, 0, 40)
        pygame.draw.arc(ECRAN, "#8C5B37", (200, 205, 40, 40), 3.15, 6.27, 50)
        pygame.draw.ellipse(ECRAN, "#DDAE42", (200, 218, 40, 15), 0)

        pygame.draw.arc(ECRAN, "#A67822", (165, 185, 40, 40), 3.14, 0, 40)
        pygame.draw.arc(ECRAN, "#A67822", (165, 185, 40, 40), 3.15, 6.27, 50)
        pygame.draw.ellipse(ECRAN, "#D9B44A", (165, 198, 40, 15), 0)

        pygame.draw.arc(ECRAN, "#A67822", (150, 155, 40, 40), 3.14, 0, 40)
        pygame.draw.arc(ECRAN, "#A67822", (150, 155, 40, 40), 3.15, 6.27, 50)
        pygame.draw.ellipse(ECRAN, "#D9B44A", (150, 168, 40, 15), 0)

    def steak():   # Fonction qui dessine le steak
        ECRAN.fill((255, 255, 255))  # Couleur de l'arrière-plan en blanc

        # Dessin de l'assiette
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 170, 40)
        pygame.draw.circle(ECRAN, "light grey", (250, 250), 150, 5)
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 130, 0)

        def salad(x, y):     # Fonction qui dessine la salade
            pygame.draw.polygon(ECRAN, "#7AB536", (
                (x - 10, y + 20), (x + 10, y + 20), (x + 20, y + 10), (x + 20, y - 10), (x + 10, y - 20),
                (x - 10, y - 20), (x - 20, y - 10),
                (x - 20, y + 10)))

        def carrot(x, y):    # Fonction qui dessine les carrotes
            pygame.draw.polygon(ECRAN, "#DE722B", (
                (x - 5, y + 10), (x + 5, y + 10), (x + 10, y + 5), (x + 10, y - 5), (x + 5, y - 10), (x - 5, y - 10),
                (x - 10, y - 5),
                (x - 10, y + 5)))

        def tomato(x, y):     # Fonction qui dessine les tomates
            pygame.draw.circle(ECRAN, "#E5231B", (x, y), 10, 0)

        def broccoli(x, y):    # Fonction qui dessine les broccolis
            # Tige du broccoli
            pygame.draw.rect(ECRAN, "#7AC43E", (x + 17, y + 25, 17, 30))

            # Feuilles du broccoli
            pygame.draw.circle(ECRAN, "#055D4F", (x + 9, y + 25), 15)
            pygame.draw.circle(ECRAN, "#055D4F", (x + 41, y + 25), 15)
            pygame.draw.circle(ECRAN, "#055D4F", (x + 25, y + 10), 15)
            pygame.draw.circle(ECRAN, "#055D4F", (x + 15, y + 15), 15)
            pygame.draw.circle(ECRAN, "#055D4F", (x + 35, y + 15), 15)

        # Dessin de la salade
        salad(275, 225)
        salad(300, 225)
        salad(280, 180)
        salad(305, 200)
        salad(325, 225)
        salad(290, 250)
        salad(300, 225)
        salad(350, 200)
        salad(340, 180)
        salad(360, 200)
        salad(325, 225)
        salad(285, 250)
        salad(315, 335)
        salad(320, 160)
        salad(280, 280)
        salad(305, 305)
        salad(370, 250)
        salad(290, 150)
        salad(300, 325)
        salad(350, 300)
        salad(340, 275)
        salad(360, 300)
        salad(325, 325)
        salad(350, 250)

        # Dessin des carottes
        carrot(252, 215)
        carrot(289, 220)
        carrot(283, 188)
        carrot(257, 242)
        carrot(315, 204)
        carrot(277, 250)
        carrot(281, 237)
        carrot(342, 237)
        carrot(325, 180)
        carrot(358, 175)
        carrot(333, 240)
        carrot(280, 280)
        carrot(252, 315)
        carrot(289, 340)
        carrot(283, 300)
        carrot(257, 342)
        carrot(315, 304)
        carrot(370, 300)
        carrot(281, 337)
        carrot(342, 337)
        carrot(325, 280)
        carrot(300, 140)
        carrot(280, 125)
        carrot(315, 345)

        # Dessin des tomates
        tomato(300, 176)
        tomato(300, 250)
        tomato(285, 188)
        tomato(257, 240)
        tomato(301, 280)
        tomato(294, 270)
        tomato(270, 237)
        tomato(345, 266)
        tomato(300, 182)
        tomato(370, 250)
        tomato(333, 170)
        tomato(260, 194)
        tomato(350, 200)
        tomato(300, 215)
        tomato(310, 286)
        tomato(300, 330)
        tomato(285, 298)
        tomato(257, 340)
        tomato(301, 150)
        tomato(270, 337)
        tomato(345, 330)
        tomato(300, 130)
        tomato(370, 235)
        tomato(333, 270)
        tomato(260, 294)
        tomato(350, 300)
        tomato(300, 315)

        # Dessin des brocolis
        broccoli(135, 160)
        broccoli(115, 190)
        broccoli(175, 125)
        broccoli(220, 110)
        broccoli(215, 150)
        broccoli(190, 170)
        broccoli(165, 200)
        broccoli(185, 205)

        # Dessin des onions
        pygame.draw.arc(ECRAN, "#8B006B", [275, 175, 50, 50], 0, 3.14, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [300, 200, 50, 50], 2, 4.50, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [320, 225, 50, 50], 4, 6.28, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [250, 215, 50, 50], 3, 6, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [330, 180, 50, 50], 0, 5, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [280, 150, 50, 50], 1, 4.9, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [300, 215, 50, 50], 4.9, 1, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [275, 275, 50, 50], 0, 3.14, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [300, 300, 50, 50], 2, 4.50, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [280, 315, 50, 50], 4, 6.28, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [250, 315, 50, 50], 3, 6, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [330, 280, 50, 50], 0, 5, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [280, 250, 50, 50], 1, 4.9, 5)
        pygame.draw.arc(ECRAN, "#8B006B", [300, 315, 50, 50], 4.9, 1, 5)

        # Dessin du steak
        pygame.draw.polygon(ECRAN, "#805135", (
            (135, 245), (125, 280), (190, 320), (250, 340), (285, 335), (290, 320), (290, 340), (285, 355),
            (250, 360), (190, 340), (125, 300), (120, 280)))
        pygame.draw.polygon(ECRAN, "#5C3318", (
            (290, 320), (250, 275), (235, 245), (225, 235), (200, 235), (190, 245), (165, 235), (135, 244),
            (125, 280), (135, 290), (190, 330), (250, 350), (282, 345)))
        pygame.draw.polygon(ECRAN, "#C39457", (
            (220, 235), (200, 235), (190, 245), (165, 235), (135, 244), (170, 240), (185, 250), (200, 270),
            (230, 290), (210, 270), (200, 250), (210, 238)))

    def cafe():    # Fonction qui dessine le café
        ECRAN.fill((255, 255, 255))

        # Dessin de l'assiette
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 110, 40)
        pygame.draw.circle(ECRAN, "light grey", (250, 250), 90, 5)
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 70, 0)

        # Dessin de la tasse
        pygame.draw.circle(ECRAN, "#BCBCBC", (250, 250), 60, 0)
        pygame.draw.line(ECRAN, "#B5B5B5", (309, 250), (350, 250), 20)
        pygame.draw.circle(ECRAN, "#D29E55", (250, 250), 50, 0)


        # Dessin du "latte art"
        pygame.draw.line(ECRAN, "white", (250, 220), (250, 290), 5)
        pygame.draw.arc(ECRAN, "white", (215, 215, 70, 70), 2.59, 0.55, 5)
        pygame.draw.arc(ECRAN, "white", (225, 215, 50, 60), 2.44, 0.7, 4)
        pygame.draw.arc(ECRAN, "white", (235, 215, 30, 50), 2.29, 0.85, 3)
        pygame.draw.arc(ECRAN, "white", (243, 220, 15, 35), 2.5, 4.71, 3)
        pygame.draw.arc(ECRAN, "white", (243, 220, 15, 35), 4.71, 6.92, 3)
        pygame.draw.line(ECRAN, "white", (245, 210), (250, 220), 5)
        pygame.draw.line(ECRAN, "white", (255, 210), (250, 220), 5)

    def gateau():     # Fonction qui dessine le quart de gateau
        ECRAN.fill((255, 255, 255))

        # Dessin de l'assiette
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 110, 40)
        pygame.draw.circle(ECRAN, "light grey", (250, 250), 90, 5)
        pygame.draw.circle(ECRAN, "#EDEDED", (250, 250), 70, 0)

        # Dessin du gateau
        pygame.draw.arc(ECRAN, "#AF642D", (151, 205, 200, 200), 0.79, 2.35, 200)
        pygame.draw.arc(ECRAN, "#FDEFD2", (150, 205, 200, 200), 0.79, 2.35, 200)
        pygame.draw.arc(ECRAN, "#AF642D", (150, 205, 200, 200), 0.79, 2.35, 5)

        # Dessin des bleuets
        pygame.draw.circle(ECRAN, "#405574", (280, 295), 8, 0)
        pygame.draw.circle(ECRAN, "#405574", (295, 305), 8, 0)
        pygame.draw.circle(ECRAN, "#405574", (297, 287), 8, 0)
        pygame.draw.circle(ECRAN, "#3A2641", (282, 295), 3, 0)
        pygame.draw.circle(ECRAN, "#3A2641", (295, 303), 3, 0)
        pygame.draw.circle(ECRAN, "#3A2641", (295, 287), 3, 0)

    # Bouton MANGER pour passer au prochain plat
    police = pygame.font.SysFont("Arial", 20)  # Police de tous les textes
    texte_bouton = police.render("MANGER", 0, (0, 0, 0))  # Rendering du texte du bouton
    coordonnees_bouton = pygame.Rect((200, 450, 100, 40))  # Coordonnées du bouton
    bouton_surface = pygame.Surface((coordonnees_bouton.width, coordonnees_bouton.height))  # Surface du bouton

    '''PLUGIN NUMÉRO 2: EFFET SONORE POUR MANGER (partie 1)'''
    eating_sfx = pygame.mixer.Sound("Minecraft Eating.mp3")

    LANCEMENT = True

    while LANCEMENT:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LANCEMENT = False

            if event.type == pygame.MOUSEBUTTONDOWN:  # Si la souris est cliquée
                if coordonnees_bouton.collidepoint(event.pos):  # Si le clic est sur le bouton
                    if increment != -1:
                        '''PLUGIN EFFET SONORE POUR MANGER (partie 2)'''
                        eating_sfx.play()

                    increment += 1
                    for i in range(len(liste_achats)):
                        if increment == len(liste_achats):
                            '''PLUGIN TIME POUR FAIRE UN DÉLAI DANS LE TEMPS'''
                            time.sleep(0.5)  # Petit delai juste pour que le plat joue le son avant de fermer la fenêtre
                            LANCEMENT = False

                        else:
                            if liste_achats[increment] == "soupe":
                                soupe()

                            elif liste_achats[increment] == "croquettes":
                                croquettes()

                            if liste_achats[increment] == "poisson":
                                poisson()

                            elif liste_achats[increment] == "steak":
                                steak()

                            if liste_achats[increment] == "café":
                                cafe()

                            elif liste_achats[increment] == "quart de gateau":
                                gateau()

        ECRAN.blit(bouton_surface, coordonnees_bouton)  # Affichage du fond du bouton
        bouton_surface.fill("grey")
        ECRAN.blit(texte_bouton, (213, 458))

        pygame.display.flip()

    pygame.quit()

# Étape 6 : Impression du reçu
def etape_6():
    global table_nombre_choisi
    global serveur
    global liste_achats
    global gratinee
    global prix

    fenetre = Tk()  # création d’une fenêtre de type Tkinter
    fenetre.title("Facture")  # affiche le titre de la fenêtre


    fenetre.geometry("500x500")
    fenetre.minsize(500, 500)  # méthode pour baliser la réduction de taille la fenêtre
    fenetre.maxsize(500, 500)  # méthode pour baliser l’agrandissement de taille la fenêtre

    mon_canevas = Canvas(width=260, height=500, bg='white')  # Création d'un canevas pour le papier imprimante
    mon_canevas.pack(side=LEFT)

    police = ("Arial", 15, "bold")   # Polices de caractères
    police_petite = ("Arial", 12)


    increment=0
    sous_total = 0

    for item in liste_achats: # Pour chaque item acheté
        increment += 25    # On augmente la coordonnée en y

        # Le texte du plat change selon l'itération de la boucle
        texte_plat = mon_canevas.create_text(30, 70+increment, text=item.upper(), anchor=NW, font=police_petite)

        # La quantité de chaque plat est calculée selon le nombre de fois où le plat apparaît
        nombre = mon_canevas.create_text(10,70+increment, text=str(liste_achats.count(item)), anchor=NW, font=police_petite)

        # On ajoute le coût de chaque plat au sous-total
        cout = prix[item]
        sous_total += cout

        # Si la soupe est gratinée, on ajoute un supplément de 2$
        if gratinee == True and item == "soupe":
             cout += 2

        # On change le coût en string pour pouvoir compter ses caractères
        cout = str(cout)

        # Selon le nombre de caractères, on ajoute des décimales
        if len(cout) == 2:
            cout += ".00$"

        elif len(cout) == 3 or len(cout) == 4:
            cout += "0$"

        elif len(cout) == 5:
            cout += "$"

        # On affiche le texte du montant à droite de chaque plat
        texte_montant = mon_canevas.create_text(250,70+increment, text=str(cout), anchor= NE, font=police_petite)

    # Calculs de la TVQ, TPS et du total
    TVQ = round(sous_total * 0.09975, 2)
    TPS = round((sous_total) * 0.05, 2)
    total = round(sous_total + TPS + TVQ, 2)

    # Changement du sous-total, de la TPS, de la TVQ et du total en string
    sous_total = str(sous_total)
    total = str(total) + "$"
    TPS = str(TPS)
    TVQ = str(TVQ)

    # On ajoute des décimales selon le nombre de caractères
    if len(sous_total) == 2:
        sous_total += ".00$"

    elif len(sous_total) == 3 or len(sous_total) == 4:
        sous_total += "0$"

    elif len(sous_total) == 5:
        sous_total += "$"

    # On ajoute le signe de $ aux taxes
    TPS = TPS + "$"
    TVQ = TVQ + "$"


    # Affichage de tous les textes de la facture
    texte_table = mon_canevas.create_text(130, 50, text=f"Table n° {table_nombre_choisi}", font=police)

    texte_montant_sous_total = mon_canevas.create_text(250, 200, text=sous_total , anchor=E, font=police_petite)

    texte_sous_total = mon_canevas.create_text(30, 200, text="SOUS-TOTAL", anchor=W, font=police_petite)

    texte_TPS = mon_canevas.create_text(30, 225, text="TPS", anchor=W, font=police_petite)

    texte_montant_TPS = mon_canevas.create_text(250,225, text=str(TPS), anchor=E, font=police_petite)

    texte_TVQ = mon_canevas.create_text(30, 250,text="TVQ", anchor=W, font=police_petite)

    texte_montant_TVQ = mon_canevas.create_text(250,250, text=str(TVQ), anchor=E, font=police_petite)

    texte_total = mon_canevas.create_text(20,285, text="TOTAL", anchor=W, font=police)

    texte_montant_total = mon_canevas.create_text(250,285, text=str(total), anchor=E, font=police)

    lignes_egals = mon_canevas.create_text(3,313, text="============================", anchor=W, font=police_petite)

    '''PLUGIN NUMÉRO 3 : AFFICHE L'HEURE EXACTE À LAQUELLE LE PROGRAMME EST LANCÉ'''
    temps = (datetime.now())    # Prend la date et l'heure actuelle de l'ordinateur
    temps_actuel = temps.strftime("%H:%M")    # Conserve seulement l'heure et les minutes
    texte_temps = mon_canevas.create_text(40,345, text="HEURE : " + str(temps_actuel), anchor=W, font=police_petite)

    texte_additionnel_1 = mon_canevas.create_text(40,370, text="TPS : 000000000 RT0001", anchor=W, font=police_petite)

    texte_additionnel_2 = mon_canevas.create_text(40,395, text="TVQ : 0000000000 TQ0001", anchor=W, font=police_petite)

    texte_serveur = mon_canevas.create_text(130,425, text="VOUS AVEZ ÉTÉ SERVI", anchor=N, font=police_petite)

    nom_serveur = mon_canevas.create_text(130,455, text=f"PAR : {serveur}", anchor=N, font=police_petite)

    # Affichage de l'image du terminal
    canvas = Canvas(width=240, height=500, bg="black")
    canvas.pack(side=RIGHT)
    image_terminal = ImageTk.PhotoImage(Image.open("terminal.png").resize((240, 500)))
    canvas.create_image(0, 0, image=image_terminal, anchor=NW)


    '''PLUGIN NUMÉRO 4: Simulation de l'impression d'un reçu'''
    def imprimer_papier():
        '''Fonction qui déplace le rectangle blanc'''
        mon_canevas.move(papier, 0, 5)  # Déplace le papier par 5 pixel

        fenetre.after(25,
                      imprimer_papier)  # Rafraîchit la fenêtre à chaque 25 milisecondes et déplace le papier par récursion


    papier = mon_canevas.create_rectangle(0, 0, 260, 500, fill='white',
                                          width=0)  # Dessin du rectangle pour représenter le papier

    imprimer_papier()  # Déplace automatiquement le rectangle blanc pour simuler une imprimante

    fenetre.mainloop()


etape_1()
etape_2()
etape_3()
etape_4()
etape_5()
etape_6()


