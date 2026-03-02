from CommonLibrary import *
result = Blueprint("edit_announcement_process", __name__)
@result.route("/admin/edit-announcement/<original_announcement_name>/process", methods=["GET", "POST"])
def view(original_announcement_name):
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
            for announcement in current_app.herald.announcements:
                if (
                    announcement.title.replace(" ", "-").replace("/", "&")
                    == original_announcement_name
                ):
                    announcement.title = new_title
                    announcement.content = new_content
                    announcement.date = (
                        str(new_month) + "/" + str(new_day) + "/" + str(new_year)
                    )
                    announcement.time = (
                        str(new_hour) + ":" + str(new_minutes) + str(new_mode)
                    )
                    announcement.user = new_user
                    current_app.herald.update_files()
                    return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")
