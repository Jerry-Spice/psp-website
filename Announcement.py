class Announcement(object):
    def __init__(self, title, content, date, time, user):
        self.title = title
        self.content = content
        self.date = date
        self.time = time
        self.user = user
    
    def __str__(self):
        return self.title + " @" + self.date + "|" + self.time + "|by: " + self.user + "\n" + self.content 