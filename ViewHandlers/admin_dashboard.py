from CommonLibrary import *
result = Blueprint("admin_dashboard", __name__)
@result.route("/admin/dashboard")
def view():
    if "username" in session:
        return render_template("dashboard.html", username=session["username"])
    return redirect("/", code=302)
