import time
import showResults as rslt                                  #Ausgabe der Rennergebnisse
import readQRCode as qr                                     #QR-Scanner zur Erkennung des Autos & Teams
import _thread
import runServer as rs                                      #Webserver zur Ergebnisausgabe
import checkpointLogic as cpl                               #Alles zu Checkpoints & Zeitmessung
import sound                                                #Alle Sounds & Sprache
import light as lit                                         #Alles zu LEDs
print("import done")


_thread.start_new_thread(rs.startServer,())                 #startet Webserver für die Ergebnisausgabe
global activeCheckpoint
global teamid


def startProgramm(teamid):
                                                            #Rennvorbereitung und Startsequenz
    activeCheckpoint = 1                                    #Checkpoint 1 ist der nächste Checkpoint nach dem Start
    x = time.time()                                         #Nur ein Platzhalter vom richtigen Datentyp
    rslt.showResults(0, teamid, x)
    sound.playSound(-3)                                     
    sound.playSpeech(0, teamid)
    lit.playStartSequence()
    starttime = time.time()                                 

    while teamid != 0:                                      #Schleife während des Rennens
        if cpl.checkpointReached(activeCheckpoint % 4):     #Kontrolliert jeweils den nächsten Checkpoint nach dem zuletzt durchfahrenen, misst Zeiten, spielt Sounds und aktualisiert Zwischenergebnisse
            cpl.saveTime(starttime, activeCheckpoint % 4)
            _thread.start_new_thread(sound.playSound,(activeCheckpoint, teamid, starttime))
            rslt.showResults(activeCheckpoint, teamid, starttime)
            activeCheckpoint += 1
        if activeCheckpoint == 9:                           #beendet das Rennen, speichert und zeigt Ergebnisse, spielt entsprechende Sounds & Sprache und resettet Checkpoints
            cpl.prepareDataForDB(teamid)
            rslt.showResults(9, teamid, starttime)
            lit.raceEnd()
            time.sleep(6)
            sound.playSpeech(9, teamid, starttime)
            activeCheckpoint = 1
            teamid=0
            cpl.resetAll()
     

try:
    teamid=0
    while 1:
        teamid = qr.readQRCode()        #Führt solange die QR-Code Funktion aus, bis diese ein Auto erkennt. Erfasst die TeamID
        if teamid != 0:
            startProgramm(teamid)       #Wurde ein Auto erkannt, wird die Rennlogik ausgeführt
            time.sleep(8)               #verhindert Probleme,wenn in zwei Threads SOunds abgespielt werden. Der Pi hat keine Mischfunktion und kann immer nur in einem Thread Sound ausgeben.
            sound.playSound(-4)         #signalisiert Bereitschaft zum erneuten Rennstart
except KeyboardInterrupt:               #Manueller Abbruch über die Konsole
    print("Programm aborted")
    lit.raceEnd()                       #schaltet die LEDs aus und deinitialisiert diese
    cpl.GPIO.cleanup()                  #resettet die GPIOs und gibt diese wieder frei
    pass