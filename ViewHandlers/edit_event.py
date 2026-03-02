from CommonLibrary import *
result = Blueprint("edit_event", __name__)
@result.route("/admin/edit-event")
def view():
    if "username" in session:
        events = current_app.maggie.events.copy()
        events.sort(key=lambda x: str(x.date) + str(x.time), reverse=True)
        return render_template("edit_event.html", events=events)
    return redirect("/")
