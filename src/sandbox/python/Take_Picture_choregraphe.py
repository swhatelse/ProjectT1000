import time

class MyClass(GeneratedClass):
    def __init__(self):
        try: # disable autoBind
          GeneratedClass.__init__(self, False)
        except TypeError: # if NAOqi < 1.14
          GeneratedClass.__init__( self )
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

        self.recordFolder = "/home/nao/recordings/cameras/"

    def onLoad(self):
        self.bIsRunning = False
        self.photoCapture = ALProxy( "ALPhotoCapture" )

    def onUnload(self):
        pass

    def onInput_onStart(self):
        if( self.bIsRunning ):
            return
        self.bIsRunning = True
        resolution = self.resolutionMap[self.getParameter("Resolution")]
        cameraID = self.cameraMap[self.getParameter("Camera")]
        fileName = self.getParameter("File Name")
        self.photoCapture.setResolution(resolution)
        self.photoCapture.setCameraID(cameraID)
        self.photoCapture.setPictureFormat("jpg")
        self.photoCapture.takePicture( self.recordFolder, fileName )
        self.bIsRunning = False
        self.onStopped()
