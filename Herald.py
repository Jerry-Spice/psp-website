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
    
    def add_announcement(self, new_announcement):
        
        self.announcements.append(new_announcement)

        announcements_dict = {
            "announcements": []
        }
        for announcement in self.announcements:
            announcements_dict["announcements"].append(announcement.toJSON())
        with open(self.announcements_file, "w") as f:
            f.write(json.dumps(announcements_dict))
            f.close()

    def __str__(self):
        msg = "["
        for announcement in self.announcements:
            msg += str(announcement) + ","
        return msg + "]"