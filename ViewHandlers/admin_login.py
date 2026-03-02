from CommonLibrary import *
result = Blueprint("admin_login", __name__)
@result.route("/admin", methods=["GET", "POST"])
def view():
    if "username" in session:
        return redirect("/admin/dashboard")
    if "error" not in session:
        session["error"] = False
    return render_template("login.html", failure=session["error"])
