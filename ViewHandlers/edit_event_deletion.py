from CommonLibrary import *
result = Blueprint("edit_event_deletion", __name__)
@result.route("/admin/edit-event/<original_event_name>/delete", methods=["GET", "POST"])
def view(original_event_name):
    if "username" in session:
        if request.method == "POST":
            for event in current_app.maggie.events:
                if (
                    event.name.replace(" ", "-").replace("/", "&")
                    == original_event_name
                ):
                    current_app.maggie.events.remove(event)
                    current_app.maggie.update_files()
                    return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")
