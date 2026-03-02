from CommonLibrary import *
result = Blueprint("edit_event_specific", __name__)
@result.route("/admin/edit-event/<event_name>")
def view(event_name):
    if "username" in session:
        event = None
        for e in current_app.maggie.events:
            if e.name.replace(" ", "-").replace("/", "&") == event_name:
                event = e
                time_formatted = ""
                date_formatted = ""
                hour = int(event.time[0:-2].split(":")[0])
                minute = int(event.time[0:-2].split(":")[1])
                if "pm" in event.time.lower():
                    hour += 12
                hour %= 24

                if hour < 10:
                    time_formatted += "0"
                time_formatted += str(hour) + ":"
                if minute < 10:
                    time_formatted += "0"
                time_formatted += str(minute)

                print(time_formatted)
                day = event.date.split("/")[1]
                month = event.date.split("/")[0]
                year = event.date.split("/")[2]
                if int(month) < 10:
                    month = "0" + month
                if int(day) < 10:
                    day = "0" + day

                date_formatted = year + "-" + month + "-" + day

                return render_template(
                    "edit_event_specific.html",
                    event_data=event,
                    description_formatted=convert(event.description),
                    time_formatted=time_formatted,
                    date_formatted=date_formatted,
                )
        return redirect("/admin/dashboard")
    return redirect("/")
