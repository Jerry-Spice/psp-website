from flask import Flask, render_template, request, session, redirect
from html_to_markdown import convert
import markdown

import datetime, calendar

from Maggie import Maggie
from Herald import Herald
from configmanager import ConfigManager
from Event import Event
from Announcement import Announcement

app = Flask(__name__)
app.secret_key = ConfigManager("key.cfg").get_key()
users = ConfigManager("./data/users.cfg").get_key().split("\n")
for i in range(len(users)):
    users[i] = users[i].split(",")

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
            formatted_description = markdown.markdown(event.description)
            return render_template("events/event-template.html", event_data=event, formatted_description=formatted_description)
    return redirect("/")

@app.route("/admin")
def admin_login():
    if "username" in session:
        return redirect("/admin/dashboard")
    if "error" not in session:
        session["error"] = False
    return render_template("login.html", failure=session["error"])

@app.route("/admin/verification", methods=["GET", "POST"])
def admin_verification():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        for user in users:
            if user[0] == username and user[1] == password and int(user[2]) < 2:
                session["username"] = username
                session["mode"] = user[2]
                session["error"] = False
                return redirect("/admin/dashboard", code=302)
    session["error"] = True
    return redirect("/admin", code=302)

@app.route("/admin/dashboard")
def admin_dashboard():
    if "username" in session:
        return render_template("dashboard.html", username=session["username"])
    return redirect("/", code=302)

@app.route("/admin/logout")
def admin_logout():
    session.pop("username", None)
    return redirect("/")

@app.route("/admin/create-event")
def create_event():
    if "username" in session:
        return render_template("create_event.html")
    return redirect("/")

@app.route("/admin/create-event/process", methods=["GET", "POST"])
def create_event_process():
    if "username" in session:
        if request.method == "POST":
            name = request.form["name"]
            description = request.form["description"]
            date = request.form["date"]
            time = request.form["time"]
            point_kind = request.form["point_kind"]
            attendance_before = {"yes": [], "maybe": [], "no": []}
            attendance_after = {"yes": [], "no": []}
            hour = int(time.split(":")[0])
            minute = time.split(":")[1]
            mode = "AM"
            if hour < 12:
                mode = "AM"
            else:
                mode = "PM"
                hour -= 12
            if hour == 0:
                    hour = 12
            year = int(date.split("-")[0])
            month = int(date.split("-")[1])
            day = int(date.split("-")[2])
            maggie.add_event(Event(name, description, str(month)+"/"+str(day)+"/"+str(year), str(hour)+":"+str(minute)+str(mode), point_kind, attendance_before, attendance_after))
            return redirect("/admin/dashboard", code=302)
        return redirect("/admin/dashboard", code=302)
    return redirect("/")


@app.route("/admin/edit-event")
def edit_event():
    if "username" in session:
        events = maggie.events.copy()
        events.sort(key=lambda x: str(x.date) + str(x.time), reverse=True)
        return render_template("edit_event.html", events=events)
    return redirect("/")

@app.route("/admin/edit-event/<event_name>")
def edit_event_specific(event_name):
    if "username" in session:
        event = None
        for e in maggie.events:
            if e.name.replace(" ", "-") == event_name:
                event = e
                time_formatted = ""
                date_formatted = ""
                """if "pm" in event.time.lower():
                    if int(event.time[0:-2].split(":")[0]) != 12:
                        hour = str(int(event.time[0:-2].split(":")[0]) + 12)
                    else: 
                        hour = "12"
                    minute = event.time[0:-2].split(":")[1]
                    time_formatted = hour + ":" + minute
                else:
                    if int(event.time[0:-2].split(":")[0]) == 12:
                        hour = "00"
                    else:
                        hour = event.time[0:-2].split(":")[0]
                    minute = event.time[0:-2].split(":")[1]
                    time_formatted = hour + ":" + minute"""
                
                hour = int(event.time[0:-2].split(":")[0])
                minute = int(event.time[0:-2].split(":")[1])
                if "pm" in event.time.lower():
                    hour += 12
                hour %= 24

                if hour < 10:
                    time_formatted+="0"
                time_formatted+=str(hour)+":"
                if minute < 10:
                    time_formatted += "0"
                time_formatted+=str(minute)

                print(time_formatted)
                day = event.date.split("/")[1]
                month = event.date.split("/")[0]
                year = event.date.split("/")[2]
                if int( month) < 10:
                    month = "0" + month
                if int(day) < 10:
                    day = "0" + day
                
                date_formatted = year + "-" + month + "-" + day

                return render_template("edit_event_specific.html", event_data=event, description_formatted=convert(event.description), time_formatted=time_formatted, date_formatted=date_formatted)
        return redirect("/admin/dashboard")
    return redirect("/")

@app.route("/admin/edit-event/<original_event_name>/delete", methods=["GET","POST"])
def edit_event_delete(original_event_name):
    if "username" in session:
        if request.method == "POST":
            for event in maggie.events:
                if event.name.replace(" ", "-") == original_event_name:
                    maggie.events.remove(event)
                    maggie.update_files()
                    return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")    

@app.route("/admin/edit-event/<original_event_name>/process", methods=["GET","POST"])
def edit_event_process(original_event_name):
    if "username" in session:
        if request.method == "POST":
            new_name = request.form["name"]
            new_description = request.form["description"]
            new_date = request.form["date"]
            new_time = request.form["time"]
            new_point_kind = request.form["point_kind"]
            new_hour = int(new_time.split(":")[0])
            new_minute = new_time.split(":")[1]
            new_mode = "AM"
            if new_hour < 12:
                new_mode = "AM"
            else:
                new_mode = "PM"
                new_hour -= 12
            if new_hour == 0:
                    new_hour = 12
            new_year = int(new_date.split("-")[0])
            new_month = int(new_date.split("-")[1])
            new_day = int(new_date.split("-")[2])
            for event in maggie.events:
                if event.name.replace(" ", "-") == original_event_name:
                    event.name = new_name
                    event.description = new_description
                    event.date = str(new_month) + "/" + str(new_day) + "/" + str(new_year)
                    event.time = str(new_hour) + ":" + str(new_minute) + str(new_mode)
                    event.point_kind = new_point_kind
                    print(event)
                    maggie.update_files()
                    return redirect("/admin/dashboard")
                
        return redirect("/admin/dashboard")
    return redirect("/")

@app.route("/admin/create-announcement")
def create_announcement():
    if "username" in session:
        return render_template("create_announcement.html")
    return redirect("/")

@app.route("/admin/create-announcement/process", methods=["GET", "POST"])
def create_announcement_process():
    if "username" in session:
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            day = datetime.datetime.now().day
            month = datetime.datetime.now().month
            year = datetime.datetime.now().year
            hour = datetime.datetime.now().hour
            minutes = datetime.datetime.now().minute
            mode = "AM"
            mode = "AM"
            if hour < 12:
                mode = "AM"
            else:
                mode = "PM"
                hour -= 12
            if hour == 0:
                    hour = 12
            if minutes < 10:
                minutes = "0" + str(minutes)
            else:
                minutes = str(minutes)
            user = session["username"]
            herald.add_announcement(Announcement(title, description, str(month) + "/" + str(day) + "/" + str(year), str(hour) + ":" + str(minutes) + str(mode), str(user)))
            return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")

@app.route("/admin/edit-announcement")
def edit_announcement():
    if "username" in session:
        return render_template("edit_announcement.html", announcements=herald.announcements.copy())
    return redirect("/")

@app.route("/admin/edit-announcement/<original_announcement_name>")
def edit_announcement_specific(original_announcement_name):
    if "username" in session:
        for announcement in herald.announcements:
            if announcement.title.replace(" ", "-") == original_announcement_name:
                formatted_content = convert(announcement.content)
                return render_template("edit_announcement_specific.html", announcement=announcement, formatted_content=formatted_content)
    return redirect("/")

@app.route("/admin/edit-announcement/<original_announcement_name>/delete", methods=["GET","POST"])
def edit_announcement_delete(original_announcement_name):
    if "username" in session:
        if request.method == "POST":
            for announcement in herald.announcements:
                if announcement.title.replace(" ", "-") == original_announcement_name:
                    herald.announcements.remove(announcement)
                    herald.update_files()
                    return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")  

@app.route("/admin/edit-announcement/<original_announcement_name>/process", methods=["GET","POST"])
def edit_announcement_process(original_announcement_name):
    if "username" in session:
        if request.method == "POST":
            new_title = request.form["title"]
            new_content = request.form["description"]
            new_day = datetime.datetime.now().day
            new_month = datetime.datetime.now().month
            new_year = datetime.datetime.now().year
            new_hour = datetime.datetime.now().hour
            new_minutes = datetime.datetime.now().minute
            new_mode = "AM"
            new_mode = "AM"
            if new_hour < 12:
                new_mode = "AM"
            else:
                new_mode = "PM"
                new_hour -= 12
            if new_hour == 0:
                    new_hour = 12
            if new_minutes < 10:
                new_minutes = "0" + str(new_minutes)
            else:
                new_minutes = str(new_minutes)
            new_user = session["username"]
            for announcement in herald.announcements:
                if announcement.title.replace(" ", "-") == original_announcement_name:
                    announcement.title = new_title
                    announcement.content = new_content
                    announcement.date =str(new_month) + "/" + str(new_day) + "/" + str(new_year)
                    announcement.time = str(new_hour) + ":" + str(new_minutes) + str(new_mode)
                    announcement.user = new_user
                    herald.update_files()
                    return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")

@app.route("/admin/create-user")
def create_user():
    if "username" in session:
        return render_template("create_user.html")
    return redirect("/")

@app.route("/admin/create-user/process", methods=["GET","POST"])
def create_user_process():
    if "username" in session:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            with open("./data/users.cfg", "a+") as f:
                f.write(str(username) + "," + str(password) + ",3\n")
                f.close()
            global users
            users.append([str(username), str(password), str(3)])
            return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")

@app.route("/admin/edit-user")
def edit_user():
    if "username" in session:
        global users
        return render_template("edit_user.html", users=users[0:-1])
    return redirect("/")

@app.route("/admin/edit-user/<username>")
def edit_user_specific(username):
    if "username" in session:
        global users
        for user in users:
            if user[0] == username:
                return render_template("edit_user_specific.html", user=user)
    return redirect("/")

@app.route("/admin/edit-user/<username>/process", methods=["GET", "POST"])
def edit_user_process(username):
    if "username" in session:
        if request.method == "POST":
            global users
            for user in users:
                if user[0] == username and user[2] != 0:
                    user[0] = request.form["username"]
                    user[1] = request.form["password"]
                    if int(session["mode"]) < 2:
                        user[2] = int(request.form["mode"])
            with open("./data/users.cfg", "w") as f:
                for user in users:
                    if user[0] != '':
                        f.write(str(user[0]))
                        f.write(",")
                        f.write(str(user[1]))
                        f.write(",")
                        f.write(str(user[2]))
                        f.write("\n")
                f.close()
        return redirect("/admin/dashboard")
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
