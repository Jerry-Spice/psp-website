class User(object):
    def __init__(self, username, password, points):
        self.username = username
        self.password = password
        self.points = points
    
    def __str__(self):
        return str(self.username) + " | " + self.password + " | " + self.points
    