import Plateau
import Joueur

def Is_Victorieux(colonne, ligne, Joueur, Plateau):
	return Victoire(colonne, ligne, Joueur, Plateau)


" Classe qui dit si le coup jouer fait gagner le joueur"
class victoire :

	def __init__(self, colonne, ligne, Joueur, Plateau):# renvoie Joueur si le joueur gagne, sinon -1.
	
	j[4]
	k[3]
		
	for i=0;i<4;i++ :
		j[i]=1
	
	for i=0;i<3;i++ :
		k[i]=1

	for i=1; i<4; i++ :
		if (colonne - i) > -1 :
			if ((Plateau.get_case_plateau(colonne - i, ligne) == Joueur) && (j[0]==i)) : 
				j[0]++
			if ((ligne - i > -1)&&(j[1]==i)) :
				if(Plateau.get_case_plateau(colonne - i, ligne - i) == Joueur) : 
					j[1]++
			
			if ((ligne + i < 6)&&(j[2]==i)) : 
				if(Plateau.get_case_plateau(colonne - i, ligne + i) == Joueur) :
					j[2]++
			
		#fin if
		if ((ligne - i > -1)&&(j[3]==i)) :
			if(Plateau.get_case_plateau(colonne, ligne - i) == Joueur) : 
				j[3]++
		
	#fin for
	for (i=1; i<4; i++) :
	
		if (colonne + i < 7) :
		
			if ((Plateau.get_case_plateau(colonne + i, ligne) == Joueur) && (k[0]==i)) :
				k[0]++
			if ((ligne - i > -1)&&(k[2]==i)) :
				if(Plateau.get_case_plateau(colonne + i, ligne - i) == Joueur) : 
					k[2]++
			if ((ligne + i < 6)&&(k[1]==i)) : 
				if(Plateau.get_case_plateau(colonne + i, ligne + i) == Joueur) : 
					k[1]++
			
	#fin du for

	if ((k[0]+j[0]>=5)||(k[1]+j[1]>=5)||(k[2]+j[2]>=5)||(j[3]==4)) : 
		return Joueur
	else :
		return -1
#fin de la classe
