#!/usr/bin/env python2

class Interface_entree:

    def __init__(self):

    def Prendre_Photo(self) :#on prend une photo 
        # try:
		#     self.photoCapture = ALProxy( "ALPhotoCapture", "localhost", 9559)
        # except:
        #     Interface_sortie.Interface_sortie("Module 'ALPhotoCapture' not found.", "")

        # resolution = self.resolutionMap['1280 x 960']
        # cameraID = self.cameraMap['Top']
        # fileName = 'nao_pic_test'
        # self.photoCapture.setResolution(resolution)
        # self.photoCapture.setCameraID(cameraID)
        # self.photoCapture.setPictureFormat("png")
        # self.photoCapture.takePicture( self.recordFolder, fileName)


    def Attente_senseur(self, Texte):
        # #on attend la reponse du senseur sur le crane

        # if(Texte != "") :#si on a du texte on le dis
        #     #Interface_sortie.Interface_sortie(Texte, "")#on dis notre texte 
        #     print Texte
        # self.ANSWER = 0     
        # self.NB_TENTATIVE = 5 #nombre de tentative avant l'arret de l'attente        
        # self.compteur_tentative = 0
        # try:     
        #     myBrocker = ALBroker("myBrocker", "0.0.0.0",0, "localhost", 9559)
        # except:
        #     print("Impossible de connecter le broker")

        # ReactToTouch = ReactToTouchModule.ReactToTouchModule("ReactToTouch")
               
        # print ReactToTouch.getIsTouched()

        # #on attend que le pied gauche du robot soit toucher
        # try:        
        #     while (not ReactToTouch.getIsTouched() and self.compteur_tentative != self.NB_TENTATIVE):
        #         time.sleep(1)        
        #         self.compteur_tentative += 1 #on incremente notre compteur de tentative
        # except KeyboardInterrupt:
        #     myBrocker.shutdown()
        #     sys.exit(0)
        
        # print ReactToTouch.getIsTouched()
        # #fin du while
        # #on verifie si le while c'est fini a cause du compteur
        # if(self.compteur_tentative != self.NB_TENTATIVE):
        #     self.ANSWER = 1

        # myBrocker.shutdown()
        # return self.ANSWER
