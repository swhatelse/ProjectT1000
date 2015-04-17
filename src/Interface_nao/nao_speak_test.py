import Interface_sortie
import Interface_mouvement
import Interface_entree
Interface_sortie.Interface_sortie("A toi de jouer")
Interface_sortie.Interface_sortie("Laisse moi le temps de reflechir")

mouv = Interface_mouvement.Interface_mouvement()
mouv.Faire(1)
mouv.Faire(2)

photo = Interface_entree.Interface_entree()
photo.Prendre_Photo()
