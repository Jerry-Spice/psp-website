from CommonLibrary import *
result = Blueprint("edit_announcement", __name__)
@result.route("/admin/edit-announcement")
def view():
    if "username" in session:
        return render_template(
            "edit_announcement.html", announcements=current_app.herald.announcements.copy()
        )
    return redirect("/")
