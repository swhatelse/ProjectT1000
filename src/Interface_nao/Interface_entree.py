"""
Cette classe permet de transformer l'image recu en matrice pour le jeu du puissance4


"""
from naoqi import ALProxy
import Interface_sortie
import sys
import time



class Interface_entree :

	def __init__(self):
		self.recordFolder = "/home/nao/P4/"
		self.resolutionMap = {
	            '160 x 120': 0,
	            '320 x 240': 1,
	            '640 x 480': 2,
	            '1280 x 960': 3
	        }
	        self.cameraMap = {
	            'Default': -1,
	            'Top': 0,
	            'Bottom': 1
	        }

	def Prendre_Photo(self) :#on prend une photo 
		try:
			self.photoCapture = ALProxy( "ALPhotoCapture", "localhost", 9559)
		except:
			Interface_sortie.Interface_sortie("Module 'ALPhotoCapture' not found.")

	        
	        resolution = self.resolutionMap['1280 x 960']
	        cameraID = self.cameraMap['Top']
	        fileName = 'nao_pic_test'
	        self.photoCapture.setResolution(resolution)
	        self.photoCapture.setCameraID(cameraID)
	        self.photoCapture.setPictureFormat("png")
	        self.photoCapture.takePicture( self.recordFolder, fileName )
        	
