#Zakaria Mehdaoui G26
#Question 4
note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
#a)
x1 = (notes[0][2]+notes[1][2]+notes[2][2]+notes[3][2]+notes[4][2]+notes[5][2])/6
print("La moyenne de l'élève 1 est de ", x1)
#4)b
xlev1_math = (notes[0][2]+notes[2][2]+notes[5][2])/3
print("La moyenne de l'élève 1 en maths est de : ",xlev1_math)
#4)c
#Essaie
def moyenne_tuple(notes, eleve=None, matiere=None):

    notes_elv = [note for note in notes if note[0] == eleve] if eleve is not None else notes
    notes_elv_matiere = [n for n in notes_elv if n[1] == matiere] if matiere is not None else notes_elv
    return sum([n[2] for n in notes_elv_matiere])/len(notes_elv_matiere)
#Q5

class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)


class Note:
  instances = []  
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur

    Note.instances.append(self)

  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"


  @classmethod
  def vider(cls):
    cls.instances = []

  @classmethod
  def moyenne(cls):
    return(sum(n.valeur for n in cls.instances)/len(cls.instances))


if __name__ == '__main__':
    note1 = ('eleve1', 'math', 13)
    note2 = ('eleve1', 'physique', 15)
    note3 = ('eleve1', 'math', 13)
    note4 = ('eleve1', 'eco', 12)
    note5 = ('eleve1', 'eco', 13)
    note6 = ('eleve1', 'math', 12)
    note7 = ('eleve2', 'math', 13)
    note8 = ('eleve2', 'math', 14)

    notes = [note1, note2, note3, note4, note5, note6,note7,note8]

    notes_elv1 = [note for note in notes if note[0] == 'eleve1']

    print(notes_elv1)

    print(sum(note[2] for note in notes_elv1)/len(notes_elv1))

    notes_elv1_math = [n for n in notes_elv1 if n[1] == 'math']

    print(sum(n[2] for n in notes_elv1_math)/len(notes_elv1_math))

    print(moyenne_tuple(notes, 'eleve1', 'math'))

    onote = Note('eleve1', 'maths', 13)

    onotes = [Note(eleve, matiere,  valeur) for eleve, matiere, valeur in notes]

    onotes = [Note(*note) for note in notes]

    Note.vider()

    onotes = [Note(*note) for note in notes]

    print(Note.moyenne())
