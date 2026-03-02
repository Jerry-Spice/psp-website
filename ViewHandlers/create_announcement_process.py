from CommonLibrary import *
result = Blueprint("create_announcement_process", __name__)
@result.route("/admin/create-announcement/process", methods=["GET", "POST"])
def view():
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
            current_app.herald.add_announcement(
                Announcement(
                    title,
                    description,
                    str(month) + "/" + str(day) + "/" + str(year),
                    str(hour) + ":" + str(minutes) + str(mode),
                    str(user),
                )
            )
            return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")

