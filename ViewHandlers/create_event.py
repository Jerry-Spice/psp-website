from CommonLibrary import *
result = Blueprint("create_event", __name__)
@result.route("/admin/create-event")
def view():
    if "username" in session:
        return render_template("create_event.html")
    return redirect("/")
