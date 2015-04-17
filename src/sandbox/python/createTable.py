import Plateau

def createPython(reds, yellows, emptys):
	reds.sort();
	yellows.sort();
	allInOne = reds+yellows+emptys;
    allInOne.sort();
    
    if len(allInOne) != 42 :
		raise None;
	
	x = 0;
	y = 0;
	plateau = Plateau.Plateau();
	for e in allInOne:
		if (e.x==reds[0].x &&  e.y==reds[0].y):
			plateau.plateau[x][y] = Plateau.J[1];
			reds.remove(0);
		else if (e.x==yellows[0].x &&  e.y==yellows[0].y):
			plateau.plateau[x][y] = Plateau.J[2];
			yellows.remove(0);
		x += 1;
		if (x == plateau.NB_LIGNE):
			y += 1;
	return plateau;
