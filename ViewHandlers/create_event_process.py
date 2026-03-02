from CommonLibrary import *
result = Blueprint("process_event_creation", __name__)
@result.route("/admin/create-event/process", methods=["GET", "POST"])
def view():
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
            current_app.maggie.add_event(
                Event(
                    name,
                    description,
                    str(month) + "/" + str(day) + "/" + str(year),
                    str(hour) + ":" + str(minute) + str(mode),
                    point_kind,
                    attendance_before,
                    attendance_after,
                )
            )
            return redirect("/admin/dashboard", code=302)
        return redirect("/admin/dashboard", code=302)
    return redirect("/")
