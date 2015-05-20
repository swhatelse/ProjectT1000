from naoqi import ALProxy
"""
Cette classe permet a nao de signaler vocalement les infos

"""
# A LIRE
############################################################
# Pas sûr que ça soit bien de créer un objet juste pour ça
# car ça veux dire qu'on va créer un objet pour toute les fois
# où Nao va parler, et ils vont rester en mémoire jusqu'à ce que
# le garbage collector veuille bien les supprimer.
# Donc c'est pour ça que j'ai remplacé par une fonction simple
#############################################################
## 
# class Interface_sortie :
#     """
#     @Text est le texte que l'on desire faire dire a nao
#     @Vitesse est la vitesse a laquelle nao va dire sa phrase
#     """
#     def __init__(self, Text, Vitesse) :
#         try:#on tente de ce connecter au proxy du dialogue
# 		    interface_nao = ALProxy("ALTextToSpeech", "localhost", 9559)
#         except: #on renvoi l'erreur
#             self.logger.error("Module 'ALTEXtToSpeech' not found.")

#         if(Text !="") :
#             if(Vitesse != "") :
#                 self.Phrase = "\RSPD=" + str(Vitesse) + "\ "
#             else :
#                 self.Phrase = "\RSPD= 100\ "
		    
#             self.Phrase += Text
#             self.Phrase += "\RST\ "      
#             interface_nao.post.say(str(self.Phrase)) #on dis notre texte

            
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
            
