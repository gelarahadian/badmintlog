from abc import ABC, abstractmethod

class Training(ABC):
    def __init__(self, date, duration):
        self.date = date
        self.duration = duration

    @abstractmethod
    def training_description(self):
        pass

class TechnicalTraining(Training):
    def __init__(self, date, duration, skill_type):
        super().__init__(date, duration)
        self.skill_type = skill_type

    def training_description(self):
        return f"[Technical] {self.date}: {self.skill_type} for {self.duration} minutes"

class PhysicalTraining(Training):
    def __init__(self, date, duration, focus):
        super().__init__(date, duration)
        self.focus = focus

    def training_description(self):
        return f"[Physical] {self.date}: Focus on {self.focus} for {self.duration} minutes"


### File: models/performa.py
class PerformanceRecord:
    def __init__(self, date, stamina, accuracy, notes):
        self.date = date
        self.stamina = stamina
        self.accuracy = accuracy
        self.notes = notes

    def summary(self):
        return f"{self.date} | Stamina: {self.stamina}/10 | Accuracy: {self.accuracy}/10 | Notes: {self.notes}"