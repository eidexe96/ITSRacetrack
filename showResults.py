import pandas as pd
import time
import math

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
        html = '''<html><head><style>body {background: linear-gradient(#16171d, #3b1218);color: #315153;font-family: 'Open Sans', sans-serif;}table {border-collapse: collapse;border:0px solid;width: 100%;}td{border:0px;min-width: 65px;height: 35px;}th{border:0px;color: #962d3e;}th,td{text-align:center;vertical-align: middle;border-bottom: 1px solid #131f20;}tr:hover {background-color: #962d3e;color:white;}h1{text-align: center;color:dcd4eb;}</style><link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400" rel="stylesheet"><title>Racing Info</title><meta http-equiv="refresh" content="5"></head><body><h1>Racing Infos here</h1>''' 
        html += text
        html +='<p>presented by Team Racetrack</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
    elif activeCheckpoint > 0 and activeCheckpoint < 9:
        #show Live Time
        dt = time.time() - starttime
        livetime = str(math.floor(dt/60))
        livetime += " Minuten "
        livetime += str(round(dt%60))
        livetime += " Sekunden"
        htmlOut= open(htmlpage,"w")
        html = ''''<html><head><style>body {background: linear-gradient(#16171d, #3b1218);color: #315153;font-family: 'Open Sans', sans-serif;}table {border-collapse: collapse;border:0px solid;width: 100%;}td{border:0px;min-width: 65px;height: 35px;}th{border:0px;color: #962d3e;}th,td{text-align:center;vertical-align: middle;border-bottom: 1px solid #131f20;}tr:hover {background-color: #962d3e;color:white;}h1{text-align: center;color:dcd4eb;}</style><link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400" rel="stylesheet"><title>Racing Info</title><meta http-equiv="refresh" content="5"></head><body><h1>Racing Infos here</h1><p id="livetime">''' 
        html += livetime      #aktuell gefahrene Zeit seit Start
        html +='</p><p>presented by Team Racetrack</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
    elif activeCheckpoint == 9:
        #show Results after Race End
        fn = "test.csv"
        df = pd.read_csv(fn)
        dfsorttime = df.sort_values([' gesamtzeit'])
        dfhighscore = dfsorttime.drop_duplicates(subset='teamname', keep='first')
        dfh = dfhighscore#[[0,1,2,8,10]]#ggf. noch rundenzeit und einzelzeiten 3 bis 7
        table = pd.DataFrame.to_html(dfh)
        htmlOut= open(htmlpage,"w")
        html = '''<html><head><style>body {background: linear-gradient(#16171d, #3b1218);color: #315153;font-family: 'Open Sans', sans-serif;}table {border-collapse: collapse;border:0px solid;width: 100%;}td{border:0px;min-width: 65px;height: 35px;}th{border:0px;color: #962d3e;}th,td{text-align:center;vertical-align: middle;border-bottom: 1px solid #131f20;}tr:hover {background-color: #962d3e;color:white;}h1{text-align: center;color:dcd4eb;}</style><link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400" rel="stylesheet"><title>Racing Info</title><meta http-equiv="refresh" content="5"></head><body><h1>Racing Infos here</h1>'''  
        html += table
        html +='<p>presented by Team Racetrack</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
    else:
        #show Error
        htmlOut= open(htmlpage,"w")
        html = '''<html><head><style>body {background: linear-gradient(#16171d, #3b1218);color: #315153;font-family: 'Open Sans', sans-serif;}table {border-collapse: collapse;border:0px solid;width: 100%;}td{border:0px;min-width: 65px;height: 35px;}th{border:0px;color: #962d3e;}th,td{text-align:center;vertical-align: middle;border-bottom: 1px solid #131f20;}tr:hover {background-color: #962d3e;color:white;}h1{text-align: center;color:dcd4eb;}</style><link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400" rel="stylesheet"><title>Racing Info</title><meta http-equiv="refresh" content="5"></head><body><h1>Racing Infos here</h1>'''  
        html += "An Error occured. Please contact your beloved RaceTrack Team!"
        html +='<p>Thank you.</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
