from CommonLibrary import *
result = Blueprint("calendar", __name__)
@result.route("/calendar")
def view():
    return redirect(
        "/calendar/" + str(calendar.month_name[datetime.datetime.now().month])
    )
