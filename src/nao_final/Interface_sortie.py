from naoqi import ALProxy
"""
Cette fonction permet a nao de signaler vocalement les infos

"""

def Interface_sortie(Text, Vitesse) :
    try:#on tente de ce connecter au proxy du dialogue
		interface_nao = ALProxy("ALTextToSpeech", "localhost", 9559)
    except: #on renvoi l'erreur
        logger.error("Module 'ALTEXtToSpeech' not found.")

    if(Text !="") :
        if(Vitesse != "") :
            Phrase = "\RSPD=" + str(Vitesse) + "\ "
        else :
            Phrase = "\RSPD= 100\ "
		    
        Phrase += Text
        Phrase += "\RST\ "      
        interface_nao.post.say(str(Phrase)) #on dis notre texte
            
