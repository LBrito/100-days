class HighScores(object):

    def __init__(self, scores):
        self.scores = scores
        self.top = sorted(scores, reverse=True)[:3]

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.top)

    def personal_top(self):
        return self.top

    def is_latest_top_score(self):
        return self.latest() >= self.personal_best()

    def get_latest_top_diff(self):
        return self.personal_best() - self.latest()

    def report(self):
        diff = ["That's",
                (" " if self.is_latest_top_score() else f" {self.get_latest_top_diff()} short of "),
                "your personal best!"]
        return f"Your latest score was {self.latest()}. " + "".join(diff)
