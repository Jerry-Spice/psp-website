from CommonLibrary import *
result = Blueprint("create_announcement", __name__)
@result.route("/admin/create-announcement")
def view():
    if "username" in session:
        return render_template("create_announcement.html")
    return redirect("/")
