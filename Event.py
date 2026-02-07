import markdown

class Event(object):
    def __init__(self, name, description, date, time, point_kind, attendance_before, attendance_after):
        self.name = name
        self.description = markdown.markdown(description)
        self.date = date
        self.time = time
        self.point_kind = point_kind
        self.attendance_before = attendance_before
        self.attendance_after = attendance_after
    
    def get_date_day(self):
        return self.date.split("/")[1]
    
    def get_date_month(self):
        return self.date.split("/")[0]

    def get_date_year(self):
        return self.date.split("/")[2]

    def __str__(self):
        return self.name + " @" + self.date + "|" + self.time + "]\n" + self.description + "\n" + self.point_kind + "\n" + str(self.attendance_before) + "\n" + str(self.attendance_after)