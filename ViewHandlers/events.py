from CommonLibrary import *
result = Blueprint("events", __name__)
@result.route("/events")
def view():
    events = current_app.maggie.events.copy()
    events.sort(key=lambda x: str(x.date) + str(x.time), reverse=True)
    return render_template("events.html", events=events)
