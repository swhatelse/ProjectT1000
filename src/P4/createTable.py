import Plateau

def createTable(reds, yellows, emptys):
	
	reds = sorted(reds, key = lambda x:x.pt);
	yellows = sorted(yellows, key = lambda x:x.pt);
	emptys = sorted(yellows, key = lambda x:x.pt);
	
	plateau = Plateau.Plateau();
    
	#~ si il existe des pions
	if(len(reds) > 0 and len(yellows) > 0):
		
		x = 0;
		y = 0;
		rRed = reds[0].size/2
		rYell = yellows[0].size/2
		
		while len(emptys)>0 :
			#~ Retrait des 6 premiers puis tri sur les Y 
			for i in range (0,5):
				tmp.append(emptys.remove(0));
			tmp = sorted(tmp, key = lambda x:x.pt[1]);
			
			for e in tmp :
				#~	Range X	and Range Y 
				if (	len(reds) > 0
				and e.pt[0]-rRed>=reds[0].pt[0] and e.pt[0]+rRed<=reds[0].pt[0] 
				and e.pt[1]-rRed>=reds[0].pt[1] and e.pt[1]+rRed<=reds[0].pt[1]):
					plateau.plateau[x][y] = Plateau.J[1];
					reds.remove(0);
					if(len(reds) > 0):
						rRed = reds[0].size/2
				#~
				elif (	len(yellows) > 0
				and e.pt[0]-rYell>=yellows[0].pt[0] and e.pt[0]+rYell<=yellows[0].pt[0] 
				and e.pt[1]-rYell>=yellows[0].pt[1] and e.pt[1]+rYell<=yellows[0].pt[1]):
					plateau.plateau[x][y] = Plateau.J[2];
					yellows.remove(0);
					if(len(yellows) > 0):
						rYell = yellows[0].size/2
				#~ 
				x += 1;
			y += 1;
	return plateau;
