class PerformanceRecord:
    def __init__(self, date, stamina, accuracy, notes):
        self.date = date
        self.stamina = stamina
        self.accuracy = accuracy
        self.notes = notes

    def summary(self):
        return f"{self.date} | Stamina: {self.stamina}/10 | Accuracy: {self.accuracy}/10 | Notes: {self.notes}"