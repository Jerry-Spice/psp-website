import markdown

class Announcement(object):
    def __init__(self, title, content, date, time, user):
        self.title = title
        self.content = markdown.markdown(content)
        self.date = date
        self.time = time
        self.user = user
    
    def toJSON(self):
        return {
            "title": self.title,
            "content": self.content,
            "date": self.date,
            "time": self.time,
            "user": self.user
        }

    def __str__(self):
        return self.title + " @" + self.date + "|" + self.time + "|by: " + self.user + "\n" + self.content 