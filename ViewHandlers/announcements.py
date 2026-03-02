from CommonLibrary import *
result = Blueprint("announcements", __name__)
@result.route("/announcements")
def view():
    announcements = current_app.herald.announcements.copy()
    announcements.sort(key=lambda x: str(x.date) + str(x.time), reverse=True)
    return render_template("announcements.html", announcements=announcements)
