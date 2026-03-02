from CommonLibrary import *
result = Blueprint("admin_logout", __name__)
@result.route("/admin/logout")
def view():
    session.pop("username", None)
    return redirect("/")
