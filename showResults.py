import pandas as pd
import time
import math
global check

def showTime(starttime):
    result = time.time() - starttime
    s = round(result%60,1)
    m = math.floor(result/60)
    out = "Die erreichte Gesamtzeit für zwei Runden beträgt: "
    out += str(m)
    out += " Min "
    out += str(s)
    out += " Sek. Herzlichen Glückwunsch!"
    print(out)
    
def showResults(activeCheckpoint, teamid, starttime):
    fn = "test.csv" #CSV - Datenbank
    htmlpage = "test.html" #Zieldatei html
    if activeCheckpoint == 0:
        #show Team info
        #df = pd.read_csv(fn)     #pd.DataFrame.from_csv(fn)
        #table = pd.DataFrame.to_html(df)
        text = "Ein Auto wurde erkannt. Das Rennen beginnt. Viel Erfolg!"
        htmlOut= open(htmlpage,"w")
        prefixFile = open("htmlPrefix.txt", 'r')
        html = prefixFile.read()
        html += text
        html +='<p>presented by Team Racetrack</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
        prefixFile.close()
    elif activeCheckpoint > 0 and activeCheckpoint < 9:
        #show Live Time
        df = pd.read_csv("test.csv")
        df = df.sort_values(' Gesamtzeit')
        df = df.drop_duplicates(subset='Teamname', keep='first')
        df = df[['Teamname', ' Checkpoint1', ' Checkpoint2', ' Checkpoint3', ' Checkpoint4']]
        entries = df['Teamname'].count()
        teams = ['Racetrack', 'Optimus Pi', 'X', 'Team2', 'Pink Danger', 'Racing Team 1', '', 'The Speedcoders']
        if activeCheckpoint == 1:
            global checkpoints
            global lastCheckpoint
            checktime = round(time.time()-starttime,0)
            lastCheckpoint = time.time()
            checkpoints = [checktime,'NaN','NaN','NaN']
            check = " Checkpoint1"
            df = df.append({'Teamname' : teams[teamid], ' Checkpoint1' : checktime}, ignore_index = True)
        else:
            toLastCheckpoint = checkpoints[(activeCheckpoint-2)%4]
            check = " Checkpoint"
            check += str(activeCheckpoint%4)
            checkpoints[(activeCheckpoint-1)%4] = round(time.time() - lastCheckpoint,0)
            lastCheckpoint = time.time()
            df[0:entries] #löscht den letzten Eintrag
            if activeCheckpoint == 2 or activeCheckpoint == 6:
                df = df.append({'Teamname' : teams[teamid], ' Checkpoint1' : checkpoints[0], ' Checkpoint2' : checkpoints[1]}, ignore_index = True)
            elif activeCheckpoint == 3 or activeCheckpoint == 7:
                df = df.append({'Teamname' : teams[teamid], ' Checkpoint1' : checkpoints[0], ' Checkpoint2' : checkpoints[1], ' Checkpoint3' : checkpoints[2]}, ignore_index = True)
            elif activeCheckpoint == 5:
                df = df.append({'Teamname' : teams[teamid], ' Checkpoint1' : checkpoints[0]}, ignore_index = True)
            else:
                df = df.append({'Teamname' : teams[teamid], ' Checkpoint1' : checkpoints[0], ' Checkpoint2' : checkpoints[1], ' Checkpoint3' : checkpoints[2], ' Checkpoint4' : checkpoints[3]}, ignore_index = True)
                check = " Checkpoint4"
        #df = df.sort_values([check])
        table = pd.DataFrame.to_html(df)
        
        htmlOut= open(htmlpage,"w")
        prefixFile = open("htmlPrefix.txt", 'r')
        html = prefixFile.read()
        html += table
        html +='</p><p>presented by Team Racetrack</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
        prefixFile.close()
    elif activeCheckpoint == 9:
        #show Results after Race End
        fn = "test.csv"
        df = pd.read_csv(fn)
        dfsorttime = df.sort_values([' Gesamtzeit'])
        dfhighscore = dfsorttime.drop_duplicates(subset='Teamname', keep='first')
        dfh = dfhighscore#[[0,1,2,8,10]]#ggf. noch rundenzeit und einzelzeiten 3 bis 7
        table = pd.DataFrame.to_html(dfh)
        htmlOut= open(htmlpage,"w")
        prefixFile = open("htmlPrefix.txt", 'r')
        html = prefixFile.read()  
        html += table
        html +='<p>presented by Team Racetrack</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
        prefixFile.close()
    else:
        #show Error
        htmlOut= open(htmlpage,"w")
        prefixFile = open("htmlPrefix.txt", 'r')
        html = prefixFile.read() 
        html += "An Error occured. Please contact your beloved RaceTrack Team!"
        html +='<p>Thank you.</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
        prefixFile.close()
