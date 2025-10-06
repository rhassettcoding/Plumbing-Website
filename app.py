from flask import Flask
from flask import render_template

#TIME IMPORTS
from datetime import datetime
import pytz

#TIME

OPENING_TIME = "7:30 AM (PST)"
CLOSING_TIME = "5:00 PM (PST)"

pst_zone = pytz.timezone("America/Los_Angeles")
now = datetime.now(pst_zone)
currentDay = int(now.strftime("%d"))
currentHour = int(now.strftime("%H"))
currentMonth = int(now.strftime("%m"))
currentMinute = int(now.strftime("%M"))
currentWeekday = int(now.strftime("%u"))
#print(str(currentHour%12)+":"+str(currentMinute)) 

currentMessage = None
onHolliday = False
if(not onHolliday):
    if ((currentHour<17 and currentHour>=9) and currentWeekday < 6):
        currentMessage = "Open"
    else:
        if(currentWeekday>=6):
            currentMessage = (f"We are closed until Monday at {OPENING_TIME}")
        else:
            currentMessage = (f"We are closed, we open again at {CLOSING_TIME}")
else:
    currentMessage = "RHassett Plumbing is temporarily closed - Please leave us an email or check back soon for our availability status!"
#----------------------------------------------------------------

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html', message = currentMessage)

if __name__ == '__main__':
    app.run(debug=True)

#TO RUN -> python app.py
