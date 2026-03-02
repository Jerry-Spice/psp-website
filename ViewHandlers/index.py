from CommonLibrary import *

result = Blueprint("index", __name__)

@result.route("/")
def view():
    month_num = datetime.datetime.now().month
    prev_month_num = month_num - 1
    next_month_num = month_num + 1
    if prev_month_num == 0:
        prev_month_num = 12
    if next_month_num == 13:
        next_month_num = 1
    ## CALCULATE CALENDAR STRUCTURE - days & month & which day the month starts on
    calendar_monthrange = calendar.monthrange(
        datetime.datetime.now().year, datetime.datetime.now().month
    )  # returns a tuple
    first_day_of_month = calendar_monthrange[
        0
    ]  # Calendar.<CONSTANT IN ALL CAPS> use a switch statement
    number_of_days = calendar_monthrange[1]  # just a number

    first_day_of_month_number = 0
    match first_day_of_month:
        case calendar.SUNDAY:
            first_day_of_month_number = 0
        case calendar.MONDAY:
            first_day_of_month_number = 1
        case calendar.TUESDAY:
            first_day_of_month_number = 2
        case calendar.WEDNESDAY:
            first_day_of_month_number = 3
        case calendar.THURSDAY:
            first_day_of_month_number = 4
        case calendar.FRIDAY:
            first_day_of_month_number = 5
        case calendar.SATURDAY:
            first_day_of_month_number = 6

    ## ORGANIZE EVENTS INTO A 2D LIST
    events = []
    for i in range(number_of_days):
        events.append([])
    for event in current_app.maggie.events:
        if int(event.get_date_month()) == int(datetime.datetime.now().month):
            print(int(event.get_date_day()) - 1)
            events[int(event.get_date_day()) - 1].append(event)

    announcements = current_app.herald.announcements.copy()
    announcements.sort(key=lambda x: str(x.date) + str(x.time), reverse=True)
    return render_template(
        "index.html",
        first_of_month=first_day_of_month_number,
        day_count=number_of_days,
        month_name=calendar.month_name[month_num],
        prev_month=calendar.month_name[prev_month_num],
        next_month=calendar.month_name[next_month_num],
        events=events,
        announcements=announcements,
    )