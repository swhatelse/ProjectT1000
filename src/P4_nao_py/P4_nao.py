import Plateau
import Victoire
import Interface_sortie

class P4_nao :

	def __init__(self) :
	
		self.jeu_fini = false # boolean pour arreter le jeu
		self.compteur = 0 # notre compteur de coup pour vérifier l'égalité
		self.gagnant = 0
		self.joueur_courant = 0
		self.Plateau
		#on designe le joueur qui commence la partie
		self.joueur_courant = 1 #pour le moment on fait commencer le joueur 1

		while self.jeu_fini != true : 
			if self.compteur == 42 :  # égalité
				self.jeu_fini = true
				self.gagnant = 0 # on met a 0 le gagnant pour éviter qu'il garde en mémoire un joueur.
				Interface_sortie("Egalité")
				break #on arrete la boucle a ce moment la
			#fin if egalité
			if self.joueur_courant == 1 :
				Interface_sortie("C'est ton tour") #on demande au joueur humain de jouer
			else : #on fait jouer nao

				self.Plateau = Interface_entree()#on recupere la matrice du plateau
				Interface_sortie("Laisse-moi le temps de réfléchir...")
			
				c3[7]={0,6,5,1,2,4,3},r[7]   #c3 désigne l'ordre de préférence, du moins vers le plus.
				c = -1       #  nbJetonsByColonne qu'on va jouer
			
				for j=0;j<7;j++ : # on regarde d'abord si l'ordi peut gagner en un endroit
					if (nbJetonsByColonne [c3[j]]==6) :
						r[c3[j]]=-1;
					else :
						r[c3[j]]=IA(iaOrdinateur,self.joueur_courant,self.Plateau,nbJetonsByColonne,c3[j]) 
						if (r[c3[j]]==J) :
							c=c3[j]
							break
						
					
				#   on regarde si l'ordi peut ne pas perdre
				if c == -1 : 
					for j=0;j<7;j++ :
						if r[c3[j]] != -1 : 
							c=c3[j]
					
						Interface_sortie("Je place mon jeton dans la colonne " + str(c));
			

			l=nbJetonsByColonne[c];   #ligne
			Plateau.set_case_Plateau(c, l, joueur_courant) #on met le jeton dans notre Plateau
			nbJetonsByColonne[c]++

			#on verifie si le coup est gagnant
			self.gagnant = gagne(colonne,ligne,joueur_courant,Plateau);
			if self.gagnant != -1 :
				self.jeu_fini = true
			
			#on change de joueur_courant
			if (joueur_courant == 1) :
				joueur_courant = 2
			else :
				joueur_courant = 1
			
			compteur++ #on incrémente le nombre de tour
		#fin du while des coups joueur
		
		#on donne le resultat du jeu
		if self.gagnant == 1 :
			Interface_sortie("Bravo le joueur 1 a gagne")
		else if self.gagnant == 2 :
			Interface_sortie("Bravo le joueur 2 a gagne")

#fin de la fonction principal
	def IA(I, joueur_courant, Plateau, nbJetonsByColonne[7], c) :
		I--;        #on descend dans la profondeur du calcul
		s=0;
		if (gagne(c,nbJetonsByColonne[c], joueur_courant,Plateau) ==-1)  :  #si ce que je joue ne me fait pas tout de suite gagner
			
			if I != 0 :
				r=0,l,g,h;
				l = nbJetonsByColonne[c]   #on joue le nbJetonsByColonne c
				Plateau.set_case_Plateau(c, l, joueur_courant)
				nbJetonsByColonne[c]++
				# changement de joueur
				if (joueur_courant == 1) 
					joueur_courant = 2
				else :
					joueur_courant = 1
				for (int i=0;i<7;i++) : # on regarde tous les coups possibles
					if nbJetonsByColonne[i] == 6 : 
						r++
					else :
						g=IA(I,joueur_courant,Plateau,nbJetonsByColonne,i)
						if g == joueur_courant : 
							s= joueur_courant
						else :
							if g != 0 : 
								r++
					
				joueur_courant++
				if joueur_courant == 3 
					joueur_courant = 1
				if r == 7 : 
					s = joueur_courant #si toutes les solutions mènent à perdre...
				nbJetonsByColonne[c]--
				plateau.set_case_plateau(c, l, 0)
		
		else: 
			s = J
		I++
		return s  # s prend la valeur du joueur qui gagne, 0 si personne ne gagne
	#fin methode IA

