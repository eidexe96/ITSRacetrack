import pandas as pd
import time

def writeToDb(teamid, gesamtzeit, rundenzeit, zeit01, zeit12, zeit23, zeit30, liveZeit):
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
        teammitglieder = "Joern; Darius; Miro"
        info="Das ist doch egal! Das ist eh nur vorlaeufig..."
    elif(teamid == 4):
        teamname = "Pink Danger"
        teammitglieder = "Rafia; Tobias; Luisa; Michael"
        info = "The Underdogs will rise!"
    elif(teamid == 5):
        teamname = "Racing Team 1"
        teammitglieder = "Jannika; Hauke; Simon"
        info= "empty"
    else:
        return "error"
    
    rightnow = time.strftime("%d.%m.%Y %H:%M:%S")
    #inputdf = pd.DataFrame({ 'Teammitglieder' : [teammitglieder], 'Teamname' : [teamname],'BesteGesamtzeit' : [gesamtzeit], 'Rundenzeit' : [rundenzeit], 'Bestzeit01' : [zeit01], 'Bestzeit12' : [zeit12], 'Bestzeit23' : [zeit23], 'Bestzeit30' : [zeit30], 'Info' : [info], 'LiveZeit' : [liveZeit], 'Datum' : [rightnow]})
    
    with open('test.csv', 'a') as fd:
        fd.write('%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \n'%(teamname, teammitglieder, gesamtzeit, rundenzeit, zeit01, zeit12, zeit23, zeit30, info, rightnow))
 