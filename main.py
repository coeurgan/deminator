# -*- coding: utf-8 -*-
 
from Tkinter import * 

fenetre = Tk()

#label = Label(fenetre, text="Hello World")
#label.pack()

# bouton de sortie
#bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
#bouton.pack()

menuBar = Menu(fenetre)
fenetre['menu'] = menuBar

sousMenu = Menu(menuBar)
menuBar.add_cascade(label='Fichier', menu=sousMenu)
sousMenu.add_command(label='Commencer')
sousMenu.add_command(label='Quitter', command=fenetre.quit)


fenetre.mainloop()
