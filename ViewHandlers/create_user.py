from CommonLibrary import *
result = Blueprint("create_user", __name__)
@result.route("/admin/create-user")
def view():
    if "username" in session:
        return render_template("create_user.html")
    return redirect("/")
