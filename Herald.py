import json

from Announcement import Announcement

# It's called Herald because he's the guy with announcements
class Herald(object):
    def __init__(self, announcements_file):
        self.announcements_file = announcements_file
        self.announcements = []
        self.process_announcements_file(self.announcements_file)
    
    def process_announcements_file(self, filename):
        with open(filename, "r") as f:
            data = json.loads(f.read())["announcements"]
            f.close()
        for announcement in data:
            self.announcements.append(
                Announcement(
                    announcement["title"],
                    announcement["content"],
                    announcement["date"],
                    announcement["time"],
                    announcement["user"]
                )
            )
    
    def __str__(self):
        msg = "["
        for announcement in self.announcements:
            msg += str(announcement) + ","
        return msg + "]"