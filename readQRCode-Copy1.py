#import pygame
import pygame.camera
from pygame.locals import *
from PIL import Image
import zbarlight
    

def takePicture():
    print("enter takePicture")
    #pygame.init()
    #print("pygame init")
    pygame.camera.init()
    print ("pygame camera init")
    cam = pygame.camera.Camera("/dev/video0",(320,240))
    print("cam define")
    cam.start()
    print("camstart")
    img = cam.get_image()
    print("img define")
    pygame.image.save(img,"./qrphoto/qrphoto.jpg")
    print("pygame image save")
    cam.stop()
    print("camstop")
    pygame.quit()
    print("leave takePicture")


def qrRead():
    print("enter qrRead")
    file_path = './qrphoto/qrphoto.jpg'
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
        
    codes = [b'1']
    codes = zbarlight.scan_codes('qrcode', image)
    if codes == [b'1']:
        codes = 1
    elif codes == [b'2']:
        codes = 2
    elif codes == [b'3']:
        codes = 3
    elif codes == [b'4']:
        codes = 4
    elif codes == [b'5']:
        codes = 5
    elif codes == [b'6']:
        codes = 6
    elif codes == [b'7']:
        codes = 7
    elif codes == [b'8']:
        codes = 8
    elif codes == [b'9']:
        codes = 9
    else: codes = 0 #return "0",False
    print(codes)
    print("qrRead")
    return codes
    #os.remove(" ./qrphoto/qrphoto.jpg")
  
    
def readQRCode():
    print("enter readQRCode")
    takePicture()
    teamid = qrRead()
    print("leave readQRCode")
    return teamid

