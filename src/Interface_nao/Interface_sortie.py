from naoqi import ALProxy
"""
Cette classe permet a nao de signaler vocalement les infos


"""

class Interface_sortie :

        def __init__(self, Text) :
		try:#on tente de ce connecter au proxy du dialogue
			interface_nao = ALProxy("ALTextToSpeech", "localhost", 9559)
		except: #on renvoi l'erreur
			self.logger.error("Module 'ALTEXtToSpeech' not found.")

		interface_nao.say(Text) #on dis notre texte
            
