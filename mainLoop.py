﻿import time
import _thread
import checkpointLogic as cpl
import sound
import light as lit
import showResults as rslt
import buttonPressed as btn
import runServer
import readQRCode as qr
_thread.start_new_thread(runServer.startServer, ())

global abort
abort = False

def startProgramm():
    identified = False
    while identified == False:                                   #Loop solange kein Auto identifiziert ist
        teamid, identified = qr.readQRCode()                     #Wenn der Scan funktioniert hat, wird die teamid und ein True-Flag zurückgegeben
        if identified == True:                                   #Initialisiere Startsequenz sobald ein Auto erkannt wurde
            rslt.showResults(0, teamid, 0)                       #zeigt bisherige Ergebnisse des Teams an
            sound.playSpeech(0, teamid)                          #erzählt infos zum Team
            lit.playStartSequence()                              #startet Ampel, Sounds und Fehlstartkontrolle
    
    starttime = clock()                                          #startet die Zeitmessung unabhängig davon, ob das Auto zu spät los fährt
    activeCheckpoint = 1
    
    while identified == True:                                                   #Loop für Rennen, Messung etc.
        if checkpointReached(activeCheckpoint % 4):
            cpl.saveTime(starttime, activeCheckpoint % 4)                       #speichert die LiveZeit vom aktuellen Checkpoint [0,1,2,3]
            _thread.start_new_thread(lit.startLightExpress,(activeCheckpoint))  #Ampel leuchtet, checkpointabhängig, läuft parallel
            _thread.start_new_thread(sound.playSound,(activeCheckpoint))        #Spielt parallel den Sound, checkpointabhängig [1...8]
            _thread.start_new_thread(sound.playSpeech,(activeCheckpoint, teamid)) #spricht (parallel),checkpointabhängig [1...8],teamid?
            rslt.showResults(activeCheckpoint, teamid, starttime)                #Zeigt Ergebnisse
            activeCheckpoint += 1
        if activeCheckpoint == 9:                                               #beendet das Rennen, speichert und zeigt Ergebnisse
            cpl.prepareDataForDB(teamID)                                        #rechnet einzelne Zeiten aus und schreibt diese in die DB
            rslt.showResults(9, teamid)
            break
        
        if btn.buttonPressed():                                                     #Button zum manuellen Abbrechen/Resetten des Rennens
            if abort:
                lit.stopLightExpress()                                              #Bestätigt visuell Eingabe des Resett-Befehls
                break
            else:
                abort = True
                time.sleep(3)
                
        if abort and not btn.buttonPressed():                                   #Resettet den Button wenn dieser zu früh losgelassen wurde
            abort = False
            

while True:                                                                     #Starts Programm on Buttonpress
    if btn.buttonPressed():
        startProgramm()
        break
        
        
