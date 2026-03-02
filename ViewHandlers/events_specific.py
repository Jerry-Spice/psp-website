from CommonLibrary import *
result = Blueprint("events_specific", __name__)
@result.route("/events/<event_name>")
def view(event_name):
    event = None
    for e in current_app.maggie.events:
        if e.name.replace(" ", "-").replace("/", "&") == event_name:
            event = e
            formatted_description = markdown.markdown(event.description)
            return render_template(
                "events/event-template.html",
                event_data=event,
                formatted_description=formatted_description,
            )
    return redirect("/")
