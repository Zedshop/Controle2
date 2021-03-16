#Zakaria Mehdaoui G26
#Question 4
#a)
x1 = (note[2]+notes[1][2]+notes[2][2]+notes[3][2]+notes[4][2]+notes[5][2])/6
print("La moyenne de l'élève 1 est de ", x1)
#4)b
xlev1_math = (notes[0][2]+notes[2][2]+notes[5][2])/3
print("La moyenne de l'élève 1 en maths est de : ",xlev1_math)
#4)c
#Essaie
def moyenne_tuples():
    eleve = input("Entrez le nom de l'élève: ")
    matiere  = input("Choisissez la matère: ")
    cpt = 0
    moyenne = 0
   
    for i in range(8):
        if(notes[i][0] == eleve):
            if(notes[i][1] == matiere):
                moyenne += notes[i][2]
                cpt += 1
    moyenne = moyenne/cpt
    print(moyenne)
               
moyenne_tuples(notes)

#Question 5
#Essaie
class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur 

def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)

import numpy as np

onote = Note([i] for i in notes)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

