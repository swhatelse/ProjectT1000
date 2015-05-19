import Plateau
def perr(message):
    print message
    
def createTable(reds, yellows, emptys):
    reds = sorted(reds, key = lambda x:x.pt);
    yellows = sorted(yellows, key = lambda x:x.pt);
    emptys = sorted(emptys, key = lambda x:x.pt);
    
    plateau = Plateau.Plateau(perr);
    
    #~ si il existe des pions
    if(len(reds) > 0 and len(yellows) > 0):
        
        x = 0;
        y = 0;
        rRed = reds[len(reds)-1].size
        rYell = yellows[len(yellows)-1].size
        while len(emptys)>0 :
            #~ Retrait des 6 premiers puis tri sur les Y 
            #~ print "---------------------------------"
            tmp=[]
            for i in range (0,plateau.NB_LIGNE):
                if(len(emptys)>0):
                    tmp.append(emptys.pop(0));
            tmp = sorted(tmp, key = lambda x:x.pt[1]);
            x=0
            for e in tmp :
                #~ print e
                #~  Range X and Range Y 
                #~ print str(e.pt[0])+" "+str(e.pt[1]) +" "+str(reds[len(reds)-1].pt[0])+" "+str(reds[len(reds)-1].pt[1]),
                #~ print " "+str(len(reds))
                num=-1
                red=None
                for i,r in enumerate(reds):
                    if (    len(reds) > 0
                    and e.pt[0]-rRed<=r.pt[0] and e.pt[0]+rRed>=r.pt[0] 
                    and e.pt[1]-rRed<=r.pt[1] and e.pt[1]+rRed>=r.pt[1]):
                        num=i
                        red=r
                        break
                if(num>=0):
                    reds.pop(i)
                    plateau.plateau[x][y] = Plateau.J[1];
                else:
                    num=-1
                    yell=None
                    for i,ye in enumerate(yellows):
                        if (    len(reds) > 0
                        and e.pt[0]-rYell<=ye.pt[0] and e.pt[0]+rYell>=ye.pt[0] 
                        and e.pt[1]-rYell<=ye.pt[1] and e.pt[1]+rYell>=ye.pt[1]):
                            num=i
                            yell=ye
                            break
                    if(num>=0):
                        yellows.pop(i)
                        plateau.plateau[x][y] = Plateau.J[2];
                 
                x += 1;
            y += 1;   
                    
                #~ if (    len(reds) > 0
                #~ and e.pt[0]-rRed<=reds[len(reds)-1].pt[0] and e.pt[0]+rRed>=reds[len(reds)-1].pt[0] 
                #~ and e.pt[1]-rRed<=reds[len(reds)-1].pt[1] and e.pt[1]+rRed>=reds[len(reds)-1].pt[1]):
                    #~ plateau.plateau[x][y] = Plateau.J[1];
                    #~ reds.pop();
                    #~ print "red"
                    #~ if(len(reds) > 0):
                        #~ rRed = reds[len(reds)-1].size
                #~ #~
                #~ elif (  len(yellows) > 0
                #~ and e.pt[0]-rYell<=yellows[len(yellows)-1].pt[0] and e.pt[0]+rYell>=yellows[len(yellows)-1].pt[0] 
                #~ and e.pt[1]-rYell<=yellows[len(yellows)-1].pt[1] and e.pt[1]+rYell>=yellows[len(yellows)-1].pt[1]):
                    #~ plateau.plateau[x][y] = Plateau.J[2];
                    #~ yellows.pop();
                    #~ print "yellow"
                    #~ if(len(yellows) > 0):
                        #~ rYell = yellows[len(yellows)-1].size
                        
                
    #~ print len(reds)
    return plateau;
