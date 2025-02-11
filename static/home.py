from flask import Flask
from flask import render_template

#TIME STUFF ----------------------------------------------------
from datetime import datetime
import pytz
pst_zone = pytz.timezone("America/Los_Angeles")
now = datetime.now(pst_zone)
currentDay = int(now.strftime("%d"))
currentHour = int(now.strftime("%H"))
currentMonth = int(now.strftime("%m"))
currentMinute = int(now.strftime("%M"))
currentWeekday = int(now.strftime("%u"))
#print(str(currentHour%12)+":"+str(currentMinute)) 
isOpen = None
OpenColor = None
if ((currentHour<17 and currentHour>=9) and currentWeekday < 6):
    isOpen = "Open"
else:
    if(currentWeekday>=6):
        isOpen = "We are closed until Monday @ 9 am"
    else:
        isOpen = "Closed, we open at 9 am"
#----------------------------------------------------------------

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', open = isOpen)

