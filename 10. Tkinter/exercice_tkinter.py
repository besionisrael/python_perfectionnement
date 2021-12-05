# Le formulaire doit afficher le logo circulaire  ainsi qu'un message invitant 
# l'utilisateur à laisser un commentaire sur le circuit. L'utilisateur peut saisir son nom, 
# son adresse électronique et un commentaire multiligne dans les champs de saisie du formulaire, 
# qui comportera deux boutons, Envoyer et Effacer. L'appui sur le bouton "submit" aura trois effets :
# il imprimera le contenu des champs de saisie dans la sortie console, il effacera le contenu actuel
# du champ de saisie et il informera l'utilisateur que ses commentaires ont été soumis avec succès. 
# Enfin, si l'utilisateur appuie sur le bouton d'effacement, comme on peut s'y attendre, le contenu
# de ces champs de saisie sera effacé. 



from tkinter import *
from tkinter import ttk

class Feedback:

    def __init__(self, master):    
        pass

            
def main():            
    
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()
    
if __name__ == "__main__": main()

