from naoqi import ALProxy
"""
Cette classe permet a nao de signaler vocalement les infos

"""

class Interface_sortie :
    """
    @Text est le texte que l'on desire faire dire a nao
    @Vitesse est la vitesse a laquelle nao va dire sa phrase
    """
    def __init__(self, Text, Vitesse) :
        try:#on tente de ce connecter au proxy du dialogue
		    interface_nao = ALProxy("ALTextToSpeech", "localhost", 9559)
        except: #on renvoi l'erreur
            self.logger.error("Module 'ALTEXtToSpeech' not found.")

        if(Text !="") :
            if(Vitesse != "") :
                self.Phrase = "\RSPD=" + str(Vitesse) + "\ "
            else :
                self.Phrase = "\RSPD= 100\ "
		    
            self.Phrase += Text
            self.Phrase += "\RST\ "      
            interface_nao.post.say(str(self.Phrase)) #on dis notre texte
       
            
