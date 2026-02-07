from flask import Flask, render_template
import os

import datetime, calendar

from Maggie import Maggie
from Herald import Herald

app = Flask(__name__)

maggie = Maggie("./data/events.json")
herald = Herald("./data/announcements.json")

@app.route("/")
def index():

    ## CALCULATE CALENDAR STRUCTURE - days & month & which day the month starts on
    calendar_monthrange = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month) # returns a tuple
    first_day_of_month = calendar_monthrange[0] # Calendar.<CONSTANT IN ALL CAPS> use a switch statement
    number_of_days = calendar_monthrange[1] # just a number

    first_day_of_month_number = 0
    match (first_day_of_month):
        case calendar.SUNDAY:
            first_day_of_month_number = 0
        case calendar.MONDAY:
            first_day_of_month_number = 1
        case calendar.TUESDAY:
            first_day_of_month_number = 2
        case calendar.WEDNESDAY:
            first_day_of_month_number = 3
        case calendar.THURSDAY:
            first_day_of_month_number = 4
        case calendar.FRIDAY:
            first_day_of_month_number = 5
        case calendar.SATURDAY:
            first_day_of_month_number = 6

    ## ORGANIZE EVENTS INTO A 2D LIST
    events = []
    for i in range(number_of_days):
        events.append([])
    for event in maggie.events:
        if int(event.get_date_month()) == int(datetime.datetime.now().month):
            print(int(event.get_date_day()) - 1)
            events[int(event.get_date_day()) - 1].append(event)
    
    announcements = herald.announcements.copy()
    announcements.sort(key=lambda x: str(x.date)+str(x.time), reverse=True)

    return render_template("index.html", 
                           first_of_month=first_day_of_month_number, 
                           day_count=number_of_days, 
                           month_name=calendar.month_name[datetime.datetime.now().month],
                           events=events,
                           announcements=announcements
                           )

@app.route("/calendar")
def calendar_view():
    ## CALCULATE CALENDAR STRUCTURE - days & month & which day the month starts on
    calendar_monthrange = calendar.monthrange(datetime.datetime.now().year, datetime.datetime.now().month) # returns a tuple
    first_day_of_month = calendar_monthrange[0] # Calendar.<CONSTANT IN ALL CAPS> use a switch statement
    number_of_days = calendar_monthrange[1] # just a number

    first_day_of_month_number = 0
    match (first_day_of_month):
        case calendar.SUNDAY:
            first_day_of_month_number = 0
        case calendar.MONDAY:
            first_day_of_month_number = 1
        case calendar.TUESDAY:
            first_day_of_month_number = 2
        case calendar.WEDNESDAY:
            first_day_of_month_number = 3
        case calendar.THURSDAY:
            first_day_of_month_number = 4
        case calendar.FRIDAY:
            first_day_of_month_number = 5
        case calendar.SATURDAY:
            first_day_of_month_number = 6

    ## ORGANIZE EVENTS INTO A 2D LIST
    events = []
    for i in range(number_of_days):
        events.append([])
    for event in maggie.events:
        if int(event.get_date_month()) == int(datetime.datetime.now().month):
            print(int(event.get_date_day()) - 1)
            events[int(event.get_date_day()) - 1].append(event)
    return render_template("calendar.html", 
                           first_of_month=first_day_of_month_number, 
                           day_count=number_of_days, 
                           month_name=calendar.month_name[datetime.datetime.now().month],
                           events=events
                        )

@app.route("/announcements")
def announcements():
    announcements = herald.announcements.copy()
    announcements.sort(key=lambda x: str(x.date)+str(x.time), reverse=True)
    return render_template("announcements.html", announcements=announcements)

@app.route("/events")
def events_view():
    events = maggie.events.copy()
    events.sort(key=lambda x: str(x.date) + str(x.time), reverse=True)
    return render_template("events.html", events = events)

@app.route("/events/<event_name>")
def event_render(event_name):
    event = None
    for e in maggie.events:
        if e.name.replace(" ", "-") == event_name:
            event = e
    if event == None or "event-" + event_name + ".html" not in os.listdir("./templates/events"):
        return render_template("events/unknown-event.html")
    return render_template("events/event-" + event_name+".html", event_data=event)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
