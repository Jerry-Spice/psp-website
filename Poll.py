class Poll(object):
    def __init__(self, question, description, votes):
        self.question = question
        self.description = description
        self.votes = votes

    def __str__(self):
        return self.question + "\n" + self.description + "\n" + self.votes