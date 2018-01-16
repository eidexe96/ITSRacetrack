from neopixel import *
import time
import checkpointLogic as cpl
#import sound


LED_COUNT      = 24      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_RGB   # Strip type and colour ordering

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
# Intialize the library (must be called once before other functions).
strip.begin()

#strip.setPixelColorRGB(0, Grün, Rot, Blau)
    
def allOff():
    for x in range(24):
        strip.setPixelColorRGB(x, 0, 0, 0)
    
    

def allGreen():
    for x in range(24):
        strip.setPixelColorRGB(x, 255, 0, 0)

    
def allYellow():
    for x in range(24):
        strip.setPixelColorRGB(x, 255, 255, 0)

def firstLight():
    strip.setPixelColorRGB(0, 0, 255, 0)
    strip.setPixelColorRGB(1, 0, 255,  0)
    strip.setPixelColorRGB(2, 0, 255,  0)
    strip.setPixelColorRGB(3, 0, 255,  0)
    strip.setPixelColorRGB(4, 0, 0, 0)
    strip.setPixelColorRGB(5, 0, 0, 0)
    strip.setPixelColorRGB(6, 0, 0, 0)
    strip.setPixelColorRGB(7, 0, 0, 0)
    strip.setPixelColorRGB(8, 0, 0, 0)
    strip.setPixelColorRGB(9, 0, 0, 0)
    strip.setPixelColorRGB(10, 0, 0, 0)
    strip.setPixelColorRGB(11, 0, 0, 0)
    strip.setPixelColorRGB(12, 0, 0, 0)
    strip.setPixelColorRGB(13, 0, 0, 0)
    strip.setPixelColorRGB(14, 0, 255, 0)
    strip.setPixelColorRGB(15, 0, 255, 0)
    strip.setPixelColorRGB(16, 0, 255, 0)
    strip.setPixelColorRGB(17, 0, 255, 0)
    strip.setPixelColorRGB(18, 0, 0, 0)
    strip.setPixelColorRGB(19, 0, 0, 0)
    strip.setPixelColorRGB(20, 0, 255, 0)
    strip.setPixelColorRGB(21, 0, 255, 0)
    strip.setPixelColorRGB(22, 0, 0, 0)
    strip.setPixelColorRGB(23, 0, 0, 0)
    
def secondLight():
    strip.setPixelColorRGB(0, 0, 255, 0)
    strip.setPixelColorRGB(1, 0, 255, 0)
    strip.setPixelColorRGB(2, 0, 255, 0)
    strip.setPixelColorRGB(3, 0, 255, 0)
    strip.setPixelColorRGB(4, 0, 255, 0)
    strip.setPixelColorRGB(5, 0, 255, 0)
    strip.setPixelColorRGB(6, 0, 255, 0)
    strip.setPixelColorRGB(7, 0, 0, 0)
    strip.setPixelColorRGB(8, 0, 0, 0)
    strip.setPixelColorRGB(9, 0, 0, 0)
    strip.setPixelColorRGB(10, 0, 0, 0)
    strip.setPixelColorRGB(11, 0, 255, 0)
    strip.setPixelColorRGB(12, 0, 255, 0)
    strip.setPixelColorRGB(13, 0, 255, 0)
    strip.setPixelColorRGB(14, 0, 255, 0)
    strip.setPixelColorRGB(15, 0, 255, 0)
    strip.setPixelColorRGB(16, 0, 255, 0)
    strip.setPixelColorRGB(17, 0, 255, 0)
    strip.setPixelColorRGB(18, 0, 0, 0)
    strip.setPixelColorRGB(19, 0, 255, 0)
    strip.setPixelColorRGB(20, 0, 255, 0)
    strip.setPixelColorRGB(21, 0, 255, 0)
    strip.setPixelColorRGB(22, 0, 255, 0)
    strip.setPixelColorRGB(23, 0, 0, 0)

    
def allRed():
    for x in range(24):
        strip.setPixelColorRGB(x, 0, 255, 0)
    

def allBlue():
    for x in range(24):
        strip.setPixelColorRGB(x, 0, 0, 255)
    
    
def flashRed():                                  #Lichtsignal bei Fehlstart
    allRed()
    strip.show()
    time.sleep(0.3)
    allOff()
    strip.show()
    time.sleep(0.1)
    allRed()
    strip.show()
    time.sleep(0.3)
    allOff()
    strip.show()
    time.sleep(0.1)
    allRed()
    strip.show()
    time.sleep(0.3)
    allOff()
    strip.show()
    
def flashGreen():
    allGreen()
    strip.show()
    time.sleep(0.3)
    allOff()
    strip.show()
    time.sleep(0.1)
    allGreen()
    strip.show()
    time.sleep(0.3)
    allOff()
    strip.show()
    time.sleep(0.1)
    allGreen()
    strip.show()
    time.sleep(0.3)
    allOff()
    strip.show()
    
def flashBlue():
    allBlue()
    strip.show()
    time.sleep(0.3)
    allOff()
    strip.show()
    time.sleep(0.1)
    allBlue()
    strip.show()
    time.sleep(0.3)
    allOff()
    strip.show()
    time.sleep(0.1)
    allBlue()
    strip.show()
    time.sleep(0.3)
    allOff()
    strip.show()

    
def playStartSequence():
    #playSound(-2)
    print("firstLight")
    firstLight()
    strip.show()
    time.sleep(2)
    #playSound(-1)
    check = False #cpl.checkpointReached(0)
    if check == True:                  
        print("Fehlstart")
        allOff()
        strip.show()
        time.sleep(0.5)
        flashRed()
        #playSound('')               #Hier fehlt noch Variable für Loser Sound
        allOff()
        strip.show()
        return True               
                                    
    else:
        print("SecondLight")
        secondLight()
        strip.show()
        time.sleep(2)
        #playSound(-1)
        check = False #cpl.checkpointReached(0)
        if check == True:
            print("Fehlstart")
            allOff()
            strip.show()
            time.sleep(0.5)
            flashRed()
            #playSound('')
            allOff()
            strip.show()
            return True
            
        else:
            print("allRed")
            allRed()
            strip.show()
            time.sleep(2)
            #playSound(-1)
            check = False #cpl.checkpointReached(0)
            if check == True:
                print("Fehlstart")
                allOff()
                strip.show()
                time.sleep(0.5)
                flashRed()
                #playSound('')
                allOff()
                strip.show()
                return True
            
            else:
                print("allGreen")
                allGreen()
                startSignal = 1
                strip.show()
                time.sleep(2)
                #playSound(0)
                allOff()
                strip.show()

    
def stopLightExpress():
    a = 0
    while a < 2:
        a += 1
        allYellow()
        strip.show()
        time.sleep(0.5)
        allOff()
        strip.show()
        time.sleep(0.2)
        allYellow()
        strip.show()
        time.sleep(0.5)
        allOff()
        strip.show()
        time.sleep(0.2)
        allYellow()
        strip.show()
        time.sleep(0.5)
        allOff()
        strip.show()
        time.sleep(0.2)


def startLightExpress():
        allBlue()
        strip.show()
        
        
    
    

def raceEnd():
    allOff()
    strip.show()
    
    

#playStartSequence()
#allRed()
#strip.show()
#time.sleep(5)
#stopLightExpress()
#allOff()
#strip.show()
