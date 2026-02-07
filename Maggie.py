import json
from Event import Event

# It's called Maggie because she's an events and experience management major
class Maggie(object):
    def __init__(self, events_file):
        self.events_file = events_file
        self.events = []
        self.process_file(self.events_file)
    
    def process_file(self, filename):
        """
        Here's how events are stored in general. Everything is stored as JSON.:
        """
        with open(filename, "r") as f:
            data = json.loads(f.read())["events"]
            f.close()
        for i in range(len(data)):
            self.events.append(
                Event(
                    data[i]["name"],
                    data[i]["description"],
                    data[i]["date"],
                    data[i]["time"],
                    data[i]["point_kind"],
                    data[i]["attendance_before"],
                    data[i]["attendance_after"]
                )
            )
    
    def __str__(self):
        msg = "["
        for event in self.events:
            msg += str(event) + ","
        return msg