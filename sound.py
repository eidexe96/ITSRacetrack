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
    sec = int(round(t%60))
    if minu != 1:
        text_m = "Minuten"
    else:
        text_m = "Minute"    
    return(minu,sec,text_m)

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
        TeamName = "The Highspeedcoder"
        d_TeamName = "Tiem sö Heispiedkoda"
        #d_info = ""

        
    else:
        return "error"
    
    return TeamName, d_TeamName

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
    
    fourth_best_gesamt = max(heapq.nsmallest(4, all_gesamt))
    fourth_best_runde = max(heapq.nsmallest(4, all_runde))

    
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
    
    
    return (best_runde, best_gesamt, worst_runde, worst_gesamt, bestP_runde, bestP_gesamt, worstP_runde, worstP_gesamt, fourth_best_gesamt, fourth_best_runde)

#Kommentar-Text aus Team, Checkpoint und Renndaten erstellen

def commentary(check, d_TeamName, best_runde, best_gesamt, worst_runde, worst_gesamt, bestP_runde, bestP_gesamt, worstP_runde, worstP_gesamt, starttime):

    dfx = pd.read_excel("text4.xls")    

    pause = "<break/>"
    mittel_pause = "<break time='750ms'/>"
    lang_pause = "<break time='1200ms'/>"
    minu = " "
    sec = " "
    text_m = "Minuten"
    
#Ansage am Start:

    if check == 0:
        
        #Team hält Gesamtrekord:
        
        if bestP_gesamt == best_gesamt:
            z1 = randint(0,5)
            minu, sec, text_m = timeConvert(best_gesamt)
            text1 = dfx.loc[z1,"0_0"]
                
        #Team hält Rundenrekord aber nicht Gesamtrekord:
        
        elif bestP_runde == best_runde: 
            z1 = randint(0,5)
            minu, sec, text_m = timeConvert(best_runde)
            text1 = dfx.loc[z1,"0_1"]

            
                
        #Team hält Negativ-Gesamtrekord:
                
        elif bestP_gesamt == worst_gesamt: 
            z1 = randint(0,5)
            minu, sec, text_m = timeConvert(worst_gesamt)
            text1 = dfx.loc[z1,"0_2"]
            

        #Team hält Negativ-Rundenrekord aber nicht Negativ-Gesamtrekord:
                
        elif bestP_runde == worst_runde: 
            z1 = randint(0,2)
            minu, sec, text_m = timeConvert(worst_runde)
            text1 = dfx.loc[z1,"0_3"]
            
        #sonst:
        
        else:
            z1 = randint(0,17)
            text1 = dfx.loc[z1,"0_4"]
        
         
        #zweiter Teil:
        z2 = randint(0,44)
        text2 = dfx.loc[z2,"0_5"]
            
        text = text1.format(d_TeamName,minu,text_m,sec)+mittel_pause+text2
        
        
#Ansage nach 2 Runden:
              
    elif check == 9:
        time_end = int(time.time() - starttime -6)
        minu, sec, text_m = timeConvert(time_end)
        print("zeit:")
        print (time_end)  
        print("bestzeit:")
        print (best_gesamt)
        print("bestP_gesamt:")
        print (bestP_gesamt)  
        print("worst_gesamt:")
        print (worst_gesamt)
        print("worstP_gesamt:")
        print (worstP_gesamt)
        
        if time_end <= best_gesamt:
            z1 = randint(0,7)
            text1 = dfx.loc[z1,"9_0"]
        elif time_end <= bestP_gesamt:
            z1 = randint(0,4)
            text1 = dfx.loc[z1,"9_1"]
        elif time_end >= worst_gesamt:
            z1 = randint(0,7)
            text1 = dfx.loc[z1,"9_2"]
        elif time_end >= worstP_gesamt:
            z1 = randint(0,0)
            text1 = dfx.loc[z1,"9_3"]
        else:
            z1 = randint(0,18)
            text1 = dfx.loc[z1,"9_4"]
            
        z2 = randint(0,17)
        text2 = dfx.loc[z2,"9_5"]
        
        text = text1.format(d_TeamName,minu,text_m,sec)+lang_pause+text2
        
    return text
            

            
                
    

#Kommentartext vorlesen mit Sprachsynthese:

def synthesis(text):
    
    #speed = 200
    call(["espeak", "-vmb-de6", "-a 90" ,"-m", "-s 165", text, "2>/dev/null"])
    
def playSpeech(check, teamid, starttime = 0):
    TeamName, d_TeamName = IDconvert(teamid)
    
    best_runde, best_gesamt, worst_runde, worst_gesamt, bestP_runde, bestP_gesamt, worstP_runde, worstP_gesamt, fourth_best_gesamt, fourth_best_runde = readData(TeamName)
    
    text = commentary(check, d_TeamName, best_runde, best_gesamt, worst_runde, worst_gesamt, bestP_runde, bestP_gesamt, worstP_runde, worstP_gesamt, starttime)
    
    synthesis(text)


def s_speech(var2):
    call(["pico2wave", "-lang=de-DE", "-wave=/home/pi/work/sound/test.wav", var2])
    call(["aplay", "/home/pi/work/sound/test.wav"])
    call(["rm", "/home/pi/work/sound/test.wav"])
    
    
    
#sound function

def playSound(check, teamid = 0, starttime = 0):
    if check == -4:
        sound = "restart.wav"
        
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
        sound = "2nd_lap2.wav"
        
    elif check == 8:
        fourth_best_gesamt = readData(teamid)[8]
        time_now = time.time() - starttime 
        if time_now > fourth_best_gesamt:
            sound = "end_bad.wav"
        else:
            sound = "end_good.wav"

    
    call(["aplay", "/home/pi/work/its/ITSRacetrack/sounds/"+sound])


