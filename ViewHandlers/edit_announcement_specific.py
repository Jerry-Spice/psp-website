from CommonLibrary import *
result = Blueprint("edit_announcement_specific", __name__)
@result.route("/admin/edit-announcement/<original_announcement_name>")
def view(original_announcement_name):
    if "username" in session:
        for announcement in current_app.herald.announcements:
            if (
                announcement.title.replace(" ", "-").replace("/", "&")
                == original_announcement_name
            ):
                formatted_content = convert(announcement.content)
                return render_template(
                    "edit_announcement_specific.html",
                    announcement=announcement,
                    formatted_content=formatted_content,
                )
    return redirect("/")
