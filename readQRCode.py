from PIL import Image
import zbarlight
import cv2
import time    
    
    
def takePicture():
    print("enter takePicture")
    
    cap = cv2.VideoCapture(0)
    print("Video captured")
    ret, frame = cap.read()
    print("frame read")
    
    fp = "qrphoto.jpg"
    print("picture saved")
    cv2.imwrite(fp, frame)
    
    print ("leave takePicture")


def qrRead():
    print("enter qrRead")
    file_path = 'qrphoto.jpg'
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
        
    
    codes = zbarlight.scan_codes('qrcode', image)
    #codes = 5
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
    time.sleep(1)
    teamid = qrRead()
    print("leave readQRCode")
    return teamid

def qrAlternative():
    teamid = input("Bitte Team-ID eingeben: ")
    return teamid