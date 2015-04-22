import Plateau

def createTable(reds, yellows, emptys):
    reds.sort();
    yellows.sort();
    pions = reds+yellows;
    pions.sort();
    
    plateau = Plateau.Plateau();
    
    if len(pions)+len(emptys) != plateau.NB_LIGNE*plateau.NB_COLONNE :
        raise "Not 42 cells";
    
    x = 0;
    y = 0;
    
    for e in pions:
        if (e[0]==reds[0][0] and  e[1]==reds[0][1]):
            plateau.plateau[x][y] = Plateau.J[1]; 
            reds.remove(0);
        elif (e[0]==yellows[0][0] and  e[1]==yellows[0][1]):
            plateau.plateau[x][y] = Plateau.J[2];
            yellows.remove(0);
        x += 1;
        if (x == plateau.NB_LIGNE):
            y += 1;
    return plateau;
