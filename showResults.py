import pandas as pd
import time
import math

def showResults(activeCheckpoint, teamid, starttime):
    fn = "test.csv" #CSV - Datenbank
    htmlpage = "test.html" #Zieldatei html
    if activeCheckpoint == 0:
        #show Team info
        df = pd.DataFrame.from_csv(fn)
        table = pd.DataFrame.to_html(df)
        htmlOut= open(htmlpage,"w")
        html = '<html><head><title>Racing Info</title><meta http-equiv="refresh" content="5"></head><body><p>Racing Infos here</p><a href="http://localhost:8081/0">Anderer Text</a>' 
        html += table
        html +='<p>presented by Dem Boiz</p></body></html>' 
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
        html = '<html><head><title>Racing Info</title><meta http-equiv="refresh" content="5"></head><body><p>Racing Infos here</p><a href="http://localhost:8081/0">Anderer Text</a>' 
        html += livetime      #aktuell gefahrene Zeit seit Start
        html +='<p>presented by Dem Boiz</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
    elif activeCheckpoint == 9:
        #show Results after Race End
        htmlOut= open(htmlpage,"w")
        html = '<html><head><title>Racing Info</title><meta http-equiv="refresh" content="5"></head><body><p>Racing Infos here</p><a href="http://localhost:8081/0">Anderer Text</a>' 
        html += table
        html +='<p>presented by Dem Boiz</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()
    else:
        #show Error
        htmlOut= open(htmlpage,"w")
        html = '<html><head><title>Racing Info</title><meta http-equiv="refresh" content="5"></head><body><p>Racing Infos here</p><a href="http://localhost:8081/0">Anderer Text</a>' 
        html += "An Error occured. Please contact your beloved RaceTrack Team!"
        html +='<p>Thank you.</p></body></html>' 
        htmlOut.write(html)
        htmlOut.close()