import json
from models.latihan import TechnicalTraining, PhysicalTraining
from models.performa import PerformanceRecord

class User:
    def __init__(self, name):
        self.name = name
        self.trainings = []
        self.performances = []

    def add_training(self, training):
        self.trainings.append(training)

    def add_performance(self, performance):
        self.performances.append(performance)

    def show_trainings(self):
        for t in self.trainings:
            print(t.training_description())

    def show_performances(self):
        for p in self.performances:
            print(p.summary())

    def save_to_file(self, filename):
        data = {
            "trainings": [vars(t) for t in self.trainings],
            "performances": [vars(p) for p in self.performances]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.trainings = []
                for t in data.get("trainings", []):
                    if "skill_type" in t:
                        self.trainings.append(TechnicalTraining(t["date"], t["duration"], t["skill_type"]))
                    elif "focus" in t:
                        self.trainings.append(PhysicalTraining(t["date"], t["duration"], t["focus"]))
                self.performances = [PerformanceRecord(p["date"], p["stamina"], p["accuracy"], p["notes"]) for p in data.get("performances", [])]
        except FileNotFoundError:
            pass
