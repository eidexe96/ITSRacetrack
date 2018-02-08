import pandas as pd
import time

def writeToDb(teamid, gesamtzeit, rundenzeit, zeit01, zeit12, zeit23, zeit30, liveZeit):    #Übersetzt Teamid und schreibt alle Zeiten in eine CSV-Datei
    global time
    if(teamid == 1):
        teamname = "Optimus Pi"
        teammitglieder = "Amdi; Basti; Patrick"
        info = "Erschaffen in den Flammen Mordors; gekommen um Cybertron zu retten"
    elif (teamid == 2):
        teamname = "X"
        teammitglieder = "Goekhan; Alex; Julia"
        info="empty"
    elif(teamid == 3):
        teamname = "Team 2"
        teammitglieder = "Joern; Darius; Mirco"
        info="Das ist doch egal! Das ist eh nur vorlaeufig..."
    elif(teamid == 4):
        teamname = "Pink Danger"
        teammitglieder = "Rafia; Tobias; Luisa; Michael"
        info = "The Underdogs will rise!"
    elif(teamid == 5):
        teamname = "Racing Team 1"
        teammitglieder = "Jannika; Hauke; Simon"
        info= "empty"
    elif(teamid == 7):
        teamname = "The Highspeedcoder"
        teammitglieder = "Flo; Michel; Fabian"
        info= ""
    else:
        return "error"
    
    rightnow = time.strftime("%d.%m.%Y %H:%M:%S")
    
    with open('test.csv', 'a') as fd:
        fd.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s \n'%(teamname, teammitglieder, gesamtzeit, rundenzeit, zeit01, zeit12, zeit23, zeit30, info, rightnow))
 