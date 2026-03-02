from CommonLibrary import *
result = Blueprint("edit_announcement_deletion", __name__)
@result.route("/admin/edit-announcement/<original_announcement_name>/delete", methods=["GET", "POST"])
def view(original_announcement_name):
    if "username" in session:
        if request.method == "POST":
            for announcement in current_app.herald.announcements:
                if (
                    announcement.title.replace(" ", "-").replace("/", "&")
                    == original_announcement_name
                ):
                    current_app.herald.announcements.remove(announcement)
                    current_app.herald.update_files()
                    return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")
