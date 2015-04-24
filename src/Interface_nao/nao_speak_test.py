import Interface_sortie
import Interface_mouvement
import Interface_entree


#Interface_sortie.Interface_sortie("A toi de jouer", 65)
#Interface_sortie.Interface_sortie("Laisse moi le temps de reflechir", 50)

#mouv = Interface_mouvement.Interface_mouvement()
#mouv.Faire(7, 5.0)#a mettre que si sa plante au milieu (pour eviter que le robot tombe en arriere)
#mouv.Faire(0, 30.0)
#mouv.Faire(1, 10.0)
#mouv.Faire(2, 10.0)
#mouv.Faire(3, 10.0)
#mouv.Faire(4, 10.0)
#mouv.Faire(6, 30.0)



#photo = Interface_entree.Interface_entree()
#photo.Prendre_Photo()

Action = Interface_entree.Interface_entree()
resultat = Action.Attente_senseur("J'attend une action de votre part")
if(resultat == 0) :
    Interface_sortie.Interface_sortie("Je n'ai pas eu d'interaction", "")
else:
    Interface_sortie.Interface_sortie("J'ai eu une interaction", "")
