from CommonLibrary import *
result = Blueprint("edit_event_specific_process", __name__)
@result.route("/admin/edit-event/<original_event_name>/process", methods=["GET","POST"])
def view(original_event_name):
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
            for event in current_app.maggie.events:
                if (
                    event.name.replace(" ", "-").replace("/", "&")
                    == original_event_name
                ):
                    event.name = new_name
                    event.description = new_description
                    event.date = (
                        str(new_month) + "/" + str(new_day) + "/" + str(new_year)
                    )
                    event.time = str(new_hour) + ":" + str(new_minute) + str(new_mode)
                    event.point_kind = new_point_kind
                    print(event)
                    current_app.maggie.update_files()
                    return redirect("/admin/dashboard")

        return redirect("/admin/dashboard")
    return redirect("/")
