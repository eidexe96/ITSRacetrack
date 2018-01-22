from subprocess import call
from random import randint
import math
import light as lit
import time
import pandas as pd
import heapq

global minu
global sec
global text
global sound


#zeit von s in min & s umwandeln:

def timeConvert(t):
    minu = math.floor(t/60)
    sec = t%60
    return(minu,sec)

#TeamID in TeamName konvertieren

def IDconvert(teamID):
    
    if(teamID == 1):
        TeamName = "Optimus Pi"
        d_TeamName = "Tiem Optimus Pei"
        #d_info = "Erschaffen in den Flammen Mordors. Gekommen um Seibertronn zu retten"
        
    elif (teamID == 2):
        TeamName = "X"    
        d_TeamName = "Tiem X"
        #d_info = ""
        
    elif(teamID == 3):
        TeamName = "Team 2"
        d_TeamName = "Tiem 2"
        #d_info = ""
        
    elif(teamID == 4):
        TeamName = "Pink Danger"
        d_TeamName = "Tiem Pink Däinscher"
        #d_info = "Sie Anderdogs will reis"

    elif(teamID == 5):
        TeamName = "Racing Team 1"
        d_TeamName = "Räißing Tiem 1"
        #d_info = ""

    elif(teamID == 7):    
        TeamName = ""
        d_TeamName = ""
        #d_info = ""

        
    else:
        return "error"
    
    return TeamName
    return d_TeamName

#Auslesen der Datenbank:  
    
def readData(TeamName):
    
    fn = "test.csv"
    df1 = pd.read_csv(fn)
    df2 = df1.loc[df1['Teamname'] == TeamName]
    
    df3 = df1.loc[df1['Teamname'] == "X"]
    df4 = df1.loc[df1['Teamname'] == "Team 2"]
    df5 = df1.loc[df1['Teamname'] == "Pink Danger"]
    df6 = df1.loc[df1['Teamname'] == "Racing Team 1"]
    df7 = df1.loc[df1['Teamname'] == "Optimus Pi"]
    df8 = df1.loc[df1['Teamname'] == " "]

    best_runde_x = df3[' Rundenzeit'].min()
    best_runde_team2 = df4[' Rundenzeit'].min()
    best_runde_pinkdanger = df5[' Rundenzeit'].min()
    best_runde_racingteam1 = df6[' Rundenzeit'].min()
    best_runde_optimuspi = df7[' Rundenzeit'].min()
    best_runde_ = df8[' Rundenzeit'].min()
    
    all_runde = (best_runde_x, best_runde_team2, best_runde_pinkdanger, best_runde_racingteam1, best_runde_optimuspi, best_runde_ )

    best_gesamt_x = df3[' Gesamtzeit'].min()
    best_gesamt_team2 = df4[' Gesamtzeit'].min()
    best_gesamt_pinkdanger = df5[' Gesamtzeit'].min()
    best_gesamt_racingteam1 = df6[' Gesamtzeit'].min()
    best_gesamt_optimuspi = df7[' Gesamtzeit'].min()
    best_gesamt_ = df8[' Gesamtzeit'].min()
   
    all_gesamt = (best_gesamt_x, best_gesamt_team2, best_gesamt_pinkdanger, best_gesamt_racingteam1, best_gesamt_optimuspi, best_gesamt_ )
    
    best_runde = df1[' Rundenzeit'].min()
    best_gesamt = df1[' Gesamtzeit'].min()
    
    worst_runde = max(all_runde)
    
    worst_gesamt = max(all_gesamt)
    
    4th_best_gesamt = max(heapq.nsmallest(4, all_gesamt))
    4th_best_runde = max(heapq.nsmallest(4, all_runde))

    
    bestP_runde = df2[' Rundenzeit'].min()
    bestP_gesamt = df2[' Gesamtzeit'].min()
    
    worstP_runde = df2[' Rundenzeit'].max()
    worstP_gesamt = df2[' Gesamtzeit'].max()
    
    #best_01 = df1[' Checkpoint 1'].min()
    #best_12 = df1[' Checkpoint 2'].min()
    #best_23 = df1[' Checkpoint 3'].min()
    #best_30 = df1[' Checkpoint 4'].min()
    
    #worst_01 = df1[' Checkpoint 1'].max()
    #worst_12 = df1[' Checkpoint 2'].max()
    #worst_23 = df1[' Checkpoint 3'].max()
    #worst_30 = df1[' Checkpoint 4'].max()
    
    #bestP_01 = df2[' Checkpoint 1'].min()
    #bestP_12 = df2[' Checkpoint 2'].min()
    #bestP_23 = df2[' Checkpoint 3'].min()
    #bestP_30 = df2[' Checkpoint 4'].min()

    #worstP_01 = df2[' Checkpoint 1'].max()
    #worstP_12 = df2[' Checkpoint 2'].max()
    #worstP_23 = df2[' Checkpoint 3'].max()
    #worstP_30 = df2[' Checkpoint 4'].max()
    
    
    return (best_runde, best_gesamt, worst_runde, worst_gesamt, bestP_runde, bestP_gesamt, worstP_runde, worstP_gesamt, 4th_best_gesamt, 4th_best_runde)

#Kommentar-Text aus Team, Checkpoint und Renndaten erstellen

def commentary(check, d_TeamName, best_runde, best_gesamt, worst_runde, worst_gesamt, bestP_runde, bestP_gesamt, worstP_runde, worstP_gesamt):

#Ansage am Start:

    if check == 0:
        
        #Team hält Gesamtrekord:
        
        if bestP_gesamt == best_gesamt:
            z = randint(0,5)
            minu, sec = timeConvert(best_gesamt)
            if minu != 1:
                text_m = "Minuten"
            else:
                text_m = "Minute"
                
            if z == 0:
                text = "Der Gesamtrekordhalter %s steht am Start. " %(d_TeamName)
            elif z == 1:
                text = "Mit %s %s %s Sekunden hält %s derzeit den Streckenrekord." %(minu,text_m,sec,d_TeamName)
            elif z == 2:
                text = "Bestzeithalter %s macht sich bereit. Ihre bisherige Zeit: %s %s, %s Sekunden." %(d_TeamName,minu,text_m,sec)
            elif z == 3:
                text = "Das bisher beste Team %s muss sich noch einmal behaupten." %(d_TeamName)
            elif z == 4:
                text = "%s ist Rekordhalter mit einer Zeit von %s %s %s" %(d_TeamName,minu,text_m,sec)
            elif z == 5:    
                text = "Aufgepasst! Gut hinschauen. %s war bisher mit annähernd Lichtgeschwindigkeit unterwegs." %(d_TeamName)
                
        #Team hält Rundenrekord aber nicht Gesamtrekord:
        
        elif bestP_runde == best_runde: 
            z = randint(0,5)
            minu, sec = timeConvert(best_runde)
            if minu != 1:
                text_m = "Minuten"
            else:
                text_m = "Minute"
                
            if z == 0:
                text = "Der Rundenrekordhalter %s steht am Start" %(d_TeamName)
            elif z == 1:
                text = "%s hält bisher den Rundenrekord. Wird es jetzt auch den Gesamtrekord einfahren?" %(d_TeamName)
            elif z == 2:
                text = "%s hat die Rundenbestzeit von %s Minuten %s Sekunden aufgestellt. Wird %s seinen eigenen Rekord brechen?" %(d_TeamName,minu,sec,d_TeamName)
            elif z == 3:
                text = "Der Rundenrekord ist nur die halbe Miete. Jetzt will %s den Gesamtrekord!" %(d_TeamName)
            elif z == 4:
                text = "Mit einer Rundenzeit von %s %s %s Sekunden Rekordhalter: %s" %(minu,text_m,sec,d_TeamName)
            elif z == 5:
                text = "Für eine schnelle Runde hat's bei %s gereicht. Jetzt sollen's zwei am Stück sein." %(d_TeamName)
                
        #Team hält Negativ-Gesamtrekord:
                
        elif bestP_gesamt == worst_gesamt: 
            z = randint(0,4)
            minu, sec = timeConvert(worst_gesamt)
            if minu != 1:
                text_m = "Minuten"
            else:
                text_m = "Minute"
                
            if z == 0:
                text = "%s ist bisher das langsamste. Man erhofft Besserung." %(d_TeamName)
            elif z == 1:
                text = "%s hat nun die Chance seine Ehre wieder herzustellen." %(d_TeamName)
            elif z == 2:
                text = "Ein Wunder, dass sich %s nach ihrem bisherigem Ergebnis nochmal an den Start traut. Naja" %(d_TeamName)
            elif z == 3:
                text = "Dieser Durchgang könnte etwas länger dauern. %s ist am Start." %(d_TeamName)
            elif z == 4:
                text = "Das könnte ein laaaaaangsames Rennen werden. Aber vielleicht ist %s für eine Überraschung gut." %(d_TeamName)
            elif z == 5
                text = "Mit einer Zeit von %s %s %s Sekunden führt %s das Feld von hinten an." %(minu,text_m,sec,d_TeamName)

        #Team hält Negativ-Rundenrekord aber nicht Negativ-Gesamtrekord:
                
        elif bestP_runde == worst_runde: 
            z = randint(0,2)
            minu, sex = timeConvert(worst_runde)
            if minu != 1:
                text_m = "Minuten"
            else:
                text_m = "Minute"
            
            if z == 0:
                text = "Hier kommt %s mit der bisher schlechtesten Rundenzeit" %(d_TeamName)
            elif z == 1:
                text = "%s hat bisher die schechteste Runde aufgestellt. Aber immerhin nicht die schlechteste Gesamtzeit." %(d_TeamName)
            elif z == 2:
                text = "Schlechteste Rundenzeit aber nicht schlechteste Gesamtzeit? %s hats geschafft" %(d_TeamName)
           
        #sonst:
        
        else:
            z = randint(0,16)
            if z == 0:
                text = "%s steht am Start bereit." %(d_TeamName)
            elif z == 1:
                text = "Nun am Start %s." %(d_TeamName)
            elif z == 2:
                text = "Als nächstes %s." %(d_TeamName)
            elif z == 3:
                text = "An der Startlinie steht das Auto von %s" %(d_TeamName)
            elif z == 4:
                text = "%s will versuchen alle Rekorde zu brechen." %(d_TeamName)
            elif z == 5:
                text = "Ferrari oder Ente? Die Stunde der Wahrheit für %s" %(d_TeamName)
            elif z == 6:
                text = "Wer hat noch nicht, wer will nochmal? %s" %(d_TeamName)
            elif z == 7:
                text = "%s macht sich bereit." %(d_TeamName)
            elif z == 8:
                text = "Nun endlich %s " %(d_TeamName)
            elif z == 9:
                text = "Für %s stellt sich jetzt die Frage: Gepard oder Schnecke." %(d_TeamName)
            elif z == 10:
                text = "Man darf gespannt sein, wie dieser Versuch für %s laufen wird" %(d_TeamName)
            elif z == 11:
                text = "%s steht an der Linie." %(d_TeamName)
            elif z == 12:
                text = "%s ist am Start." %(d_TeamName)
            elif z == 13:
                text = "Strecke frei für %s." %(d_TeamName)
            elif z == 14:
                text = "Jetzt heißt es Bleifuß auspacken für %s" %(d_TeamName)
            elif z == 15:
                text = "%s wills wissen." %(d_TeamName)
            elif z == 16
                text = "Bisher eher im Mittelfeld zuhause: %s" %(d_TeamName)
        
        z2 = randint(0,29)
        if z2 == 0:
            text2 = " Licht aus, Spot an!"
        elif z2 == 1:
            text2 = " Los gehts!"
        elif z2 == 2:
            text2 = " Und ab geht die wilde Fahrt!"
        elif z2 == 3:
            text2 = " Auf gehts!"
        elif z2 == 4:
            text2 = " Ab geht die Luzzi"
        elif z2 == 5:
            text2 = " Mats ab!"
        elif z2 == 6:
            text2 = " Auf die Plätze!"
        elif z2 == 7:
            text2 = " Startet die Ampel!"
        elif z2 == 8:
            text2 = " Brrrrumm brrumm!"
        elif z2 == 9:
            text2 = " Ab gehts!"
        elif z2 == 10:
            text2 = " Startet die Motoren!"
        elif z2 == 11:
            text2 = " Ab geht die Post!"
        elif z2 == 13:
            text2 = " Drei, zwei, eins!"
        elif z2 == 14:
            text2 = " Auf los gehts los!"
        elif z2 == 15:
            text2 = " Räddi, sätt!"
        elif z2 == 16:
            text2 = " Uuuuuund los!"
        elif z2 == 17:
            text2 = " Auf ein neues!"
        elif z2 == 18:
            text2 = " Lasst die Spiele beginnen!"
        elif z2 == 19:
            text2 = " Viel Glück!"
        elif z2 == 20:
            text2 = " Viel Erfolg!" 
        elif z2 == 21:
            text2 = " Hals und Beinbruch!"
        elif z2 == 22:
            text2 = " Und ab dafür!"
        elif z2 == 23:
            text2 = " Toi toi toi!"  
        elif z2 == 24:
            text2 = " Gut Holz!"
        elif z2 == 25:
            text2 = " Leinen los!"
        elif z2 == 26:
            text2 = " Denn man to!"
        elif z2 == 27:
            text2 = " Frisch auf!"
        elif z2 == 28:
            text2 = " Jetzt aber ran an die Buletten!"
        elif z2 == 29:
            text2 = " Aufi!"
            
        text = text+text2
        
        
#Ansage nach 2 Runden:
              
    elif check == 9:
        time_end = time.time() - starttime
        minu,sec = timeConvert(time_end)
        if minu != 1:
                text_m = "Minuten"
            else:
                text_m = "Minute"
                
        if time_end < best_gesamt:
            text = "Neue Bestzeit von %s %s %s Sekunden von %s"%(minu,text_m,sec,d_TeamName)
        elif time_end < bestP_gesamt:
            text = "Neue persönliche Bestzeit von %s %s %s Sekunden von %s"%(minu,text_m,sec,d_TeamName)
        elif time_end > worst_gesamt:
            text = "Neue schlechteste Gesamtzeit von %s %s %s Sekunden von %s"%(minu,text_m,sec,d_TeamName)   
        elif time_end > worstP_gesamt:
            text = "Neue persönliche schlechteste Zeit von %s %s %s Sekunden von %s"%(minu,text_m,sec,d_TeamName)  
        else
            text = "Mittelmaß von %s %s %s Sekunden von %s"%(minu,text_m,sec,d_TeamName)  
            
        z2 = randint(0,9)
        if z2 == 0:
            text2 = " Wer ist der nächste?"
        elif z2 == 1:
            text2 = " Der nächste bitte!"
        elif z2 == 2:
            text2 = " Wer kommt jetzt?"
        elif z2 == 3:
            text2 = " Bitte das nächste Auto an den Start!"
        elif z2 == 4:
            text2 = " Näxt plies!"
        elif z2 == 5:
            text2 = " Huus näxt?"
        elif z2 == 6:
            text2 = " Wer ist als nächstes an der Reihe?"
        elif z2 == 7:
            text2 = " Wer ist nun dran?"
        elif z2 == 8:
            text2 = " Wir sind gespannt aufs nächste Tiem!"
        
        
        text = text+text2
    return text
            
''''#Ansage am 1. Checkpoint (bei beiden Durchgängen):

    elif check == 1 or check == 5:
        
        if t < best_01:
            z = randint(0,12)
            t = 
            timeConvert(t)
            if z == 0:
                text = "Seit dem letzten Checkpoint ist %s %s Minuten %s Sekunden unterwegs" %(d_TeamName,minu,sec)
            elif z == 1:
                text = "%s ist bisher das schnellste Team in Abschnitt 1" %(d_TeamName)
            elif z == 2:
                text = "Ein neuer Abschnittsrekord von %s Minuten %s Sekunden" %(minu,sec)
            elif z == 3:
                text = "%s Minuten und %s Sekunden ist der neue Rekord für Abschnitt 1" %(minu,sec)
            elif z == 4:
                text = "%s sind bisher die Schnellsten in Abschnitt 1" %(d_TeamName)
            elif z == 5:
                text = "Eine neue Bestzeit in Abschnitt 1"
            elif z == 6:
                text = "In Abschnitt 1 bisher die schnellste Zeit mit %s Minuten %s Sekunden" %(minu,sec)
            elif z == 7:
                text = "Brumm Brumm. Wie schnell %s in diesem Abschnitt ist" %(d_TeamName)
            elif z == 8:
                text = "%s geht ab. Daher auch der Name Ab schnitt. LOL. Hahaha. " %(d_TeamName)
            elif z == 9:
                text = "Eine super Zeit für diesen Abschnitt!"
            elif z == 10:
                text = "Bei der Geschwindigkeit kommt ja Dopingverdacht auf"
            elif z == 11:
                text = "Das Auto scheint mit Lachgaseinspritzung unterwegs zu sein."
            elif z == 12:
                text = "Der Turbo ist an bei %s!" %(d_TeamName)
                
            #nur bei Abschnitt 1:
            elif z == 9:
                text = "%s steigt gut in die Runde ein mit %s Minuten %s Sekunden auf dem ersten Abschnitt" %(d_TeamName,minu,sec)
            elif z == 10:
                text = "%s legt einen super Anfang in diese Runde hin" %(d_TeamName)
            elif z == 11:
                text = "Ein perfekter Start in die Runde von %s" %(d_TeamName)
            
            
        elif t < bestP_01:
            z = randint(1,3)
            if z == 1:
                
        elif t > worst_01:
            z = randint(1,3)
            if z == 1:
                
        elif z > worstP_01:
            z = randint(1,3)
            if z == 1:
                
        else
            text = ""
            
#Ansage am 2. Checkpoint (bei beiden Durchgängen):
       
    elif check == 2 or check == 6:
        
        if t < best12:
            z = randint(0,8)
            timeConvert(t)
            if z == 0:
                text = "Seit dem letzten Checkpoint ist %s %s Minuten %s Sekunden unterwegs" %(d_TeamName,minu,sec)
            elif z == 1:
                text = "%s ist bisher das schnellste Team in Abschnitt 1" %(d_TeamName)
            elif z == 2:
                text = "Ein neuer Abschnittsrekord von %s Minuten %s Sekunden" %(minu,sec)
            elif z == 3:
                text = "%s Minuten und %s Sekunden ist der neue Rekord für Abschnitt 1" %(minu,sec)
            elif z == 4:
                text = "%s sind bisher die Schnellsten in Abschnitt 1" %(d_TeamName)
            elif z == 5:
                text = "Eine neue Bestzeit in Abschnitt 1"
            elif z == 6:
                text = "In Abschnitt 1 bisher die schnellste Zeit mit %s Minuten %s Sekunden" %(minu,sec)
            elif z == 7:
                text = "Brumm Brumm. Wie schnell %s in diesem Abschnitt ist" %(d_TeamName)
            elif z == 8:
                text = "%s geht ab. Daher auch der Name Ab schnitt. LOL. Hahaha. " %(d_TeamName)
            elif z == 9:
                text = "Eine super Zeit für diesen Abschnitt!"
            elif z == 10:
                text = "Bei der Geschwindigkeit kommt ja Dopingverdacht auf"
            elif z == 11:
                text = "Das Auto scheint mit Lachgaseinspritzung unterwegs zu sein."
            elif z == 12:
                text = "Der Turbo ist an bei %s!" %(d_TeamName)
                
        elif t < bestP_12:
            text = "Beispiel 2"
        elif t > worst_12:
            text = "Beispiel 3"
        elif t > worstP_12:
            text = "Beispiel 4"
        else
            z = randint(0,30)
            if z == 0:
                text = "Wer Durchschnitt mag, der mag %s." %(d_TeamName)
            elif z == 1:
                text = "Eine ordentliche Zeit auf diesem Abschnitt von %s." %(d_TeamName)
            elif z == 2:
                text = "%s mit gutem Mittelmaß." %(d_TeamName)
            elif z == 3:
                text = "Mit der Zeit liegt %s im Mittelfeld." %(d_TeamName)
            elif z == 4:
                text = "Nichts halbes und ganzes von %s." %(d_TeamName)
            elif z == 5:
                text = "Die Zeit von %s auf dem Abschnitt war eher Mittelklasse." %(d_TeamName)
            elif z == 6:
                text = "%s mit einer eher mäßigen Zeit." %(d_TeamName)
            elif z == 7:
                text = "Eine mittelprächtige Leistung von %s." %(d_TeamName)
            elif z == 8:
                text = "Nicht berauschend, was %s hier abliefert." %(d_TeamName)
            elif z == 9:
                text = "%s ist mit moderater Geschwindigkeit unterwegs" %(d_TeamName)
            elif z == 10:
                text = "Ein passables Ergebnis auf diesem Abschnitt"
            elif z == 11:
                text = "Das war jetzt so lala."
            elif z == 12:
                text = "Ein durchwachsenes Abschnittsergebnis."
            elif z == 13:
                text = "Das war so einigermaßen."
            elif z == 14:
                text = "Ich sag mal okay."
            elif z == 15:
                text = "Die Zeit ist nicht überwältigend."
            elif z == 16:
                text = "Das war eine mittelmäßige Zeit"
            elif z == 17:
                text = "Die Zeit hätte besser sein können. Aber auch schlechter."
            elif z == 18:
                text = "Der Traum von %s: Nicht Mercedes sondern Opel" %(d_TeamName) 
            elif z == 19:
                text = "Der Traum von %s: Nicht Mercedes sondern Opel" %(d_TeamName) 
            elif z == 18:
                text = "Der Traum von %s: Nicht Mercedes sondern Opel" %(d_TeamName) 
            elif z == 18:
                text = "Der Traum von %s: Nicht Mercedes sondern Opel" %(d_TeamName) 
            else:
                text = ""
                
#Ansage am 3. Checkpoint (bei beiden Durchgängen):
 
    elif check == 3 or check == 7:
        
        if t < best23:
            z = randint(0,9)
            timeConvert(t)
            if z == 0:
                text = "Seit dem letzten Checkpoint ist %s %s Minuten %s Sekunden unterwegs" %(d_TeamName,minu,sec)
            elif z == 1:
                text = "%s ist bisher das schnellste Team in Abschnitt 3" %(d_TeamName)
            elif z == 2:
                text = "Ein neuer Abschnittsrekord von %s Minuten %s Sekunden" %(minu,sec)
            elif z == 3:
                text = "%s Minuten und %s Sekunden ist der neue Rekord für Abschnitt 3" %(minu,sec)
            elif z == 4:
                text = "%s sind bisher die Schnellsten in Abschnitt 3" %(d_TeamName)
            elif z == 5:
                text = "Eine neue Bestzeit in Abschnitt 3"
            elif z == 6:
                text = "In Abschnitt 3 bisher die schnellste Zeit mit %s Minuten %s Sekunden" %(minu,sec)
            elif z == 7:
                text = "Brumm Brumm. Wie schnell %s in diesem Abschnitt ist" %(d_TeamName)
            elif z == 8:
                text = "%s geht ab. Daher auch der Name Ab schnitt. Hahaha." %(d_TeamName)
                
        elif t < bestP_23:
            text = "Beispiel 2"
        elif t > worst_23:
            text = "Beispiel 3"
        elif z > worstP_23:
            text = "Beispiel 4"
        else
            text = ""           
            
''''
            
''''#Ansage nach einer Runde:

    elif check == 4:
        
        if t < best_runde:
            z = randint(0,9)
            if z == 0:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            
        elif t < bestP_runde:
            z = randint(0,9)
            if z == 0:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            
        elif t > worst_runde:
            z = randint(0,9)
            if z == 0:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
               
        elif t > worstP_runde:
            z = randint(0,9)
            if z == 0:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
              
        else
            z = randint(0,9)
            if z == 0:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"
            elif z == 1:
                text = "Beispiel 1"''''
            
                

                
    

#Kommentartext vorlesen mit Sprachsynthese:

def synthesis(text):
    
    speed = 200
    call(["espeak", "-vmb-de4", "-a 80" , speed, text, "2>/dev/null"])
    
def playSpeech(check, teamid):
    TeamName, d_TeamName = IDconvert(teamid)
    
    best_runde, best_gesamt, worst_runde, worst_gesamt, bestP_runde, bestP_gesamt, worstP_runde, worstP_gesamt, 4th_best_gesamt, 4th_best_runde = readData(TeamName)
    
    text = commentary(best_runde, best_gesamt, worst_runde, worst_gesamt, bestP_runde, bestP_gesamt, worstP_runde, worstP_gesamt, 4th_best_gesamt, 4th_best_runde)
    
    synthesis(text)


def s_speech(var2):
    call(["pico2wave", "-lang=de-DE", "-wave=/home/pi/work/sound/test.wav", var2])
    call(["aplay", "/home/pi/work/sound/test.wav"])
    call(["rm", "/home/pi/work/sound/test.wav"])
    
    
    
#sound function

def playSound(check, teamid, starttime):
    if check == -4
        sound = "beep_1.wav"
        
    elif check == -3:
        sound = "scan.wav" 
        
    elif check == -2:
        sound = "start.wav"
        
    elif check == -1:
        sound = "beep_1.wav"
        
    elif check == 0:
        sound = "beep_2.wav"
        
    elif check == 1 or check == 2 or check == 3 or check == 5 or check == 6:
        sound = "checkpoint.wav"
        
    elif check == 7:
        sound = "checkpoint.wav"
        lit.allBlue()
        lit.strip.show()
        
    elif check == 4:
        sound = "2nd_lap.wav"
        
    elif check == 8:
        4th_best_gesamt = readData(teamid)[8]
        time_now = time.time() - starttime
        if time_now < 4th_best_gesamt:
            sound = "end_good.wav"
        else:
            sound = "end_bad.wav"

    
    call(["aplay", "/home/pi/work/its/ITSRacetrack/sounds/"+sound])
    
    if check == 8:
        time.sleep(8)
        playSpeech(check, teamid, time_now)
        time.spleep(10)
        
    
    
