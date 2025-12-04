

class Task:
    def __init__(self, name, importance, length):
        self.name = name
        self.importance = importance
        self.length = length

    def __repr__(self):
        return (f"Task (name={self.name}, "f"importance={self.importance}, length={self.length})")

tasks = []  