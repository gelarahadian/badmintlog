from models.latihan import TechnicalTraining, PhysicalTraining
from models.performa import PerformanceRecord
from models.user import User

user = User("Badminton Player")
user.load_from_file("data/training.json")

while True:
    print("\n=== BadmintLog ===")
    print("1. Add technical training")
    print("2. Add physical training")
    print("3. Add performance record")
    print("4. Show all trainings")
    print("5. Show all performance records")
    print("6. Save and exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        date = input("Date (YYYY-MM-DD): ")
        duration = int(input("Duration (minutes): "))
        skill_type = input("Type of technique (smash, netting, etc.): ")
        user.add_training(TechnicalTraining(date, duration, skill_type))

    elif choice == '2':
        date = input("Date (YYYY-MM-DD): ")
        duration = int(input("Duration (minutes): "))
        focus = input("Physical focus (stamina, agility, etc.): ")
        user.add_training(PhysicalTraining(date, duration, focus))

    elif choice == '3':
        date = input("Date (YYYY-MM-DD): ")
        stamina = int(input("Stamina score (1-10): "))
        accuracy = int(input("Shot accuracy score (1-10): "))
        notes = input("Additional notes: ")
        user.add_performance(PerformanceRecord(date, stamina, accuracy, notes))

    elif choice == '4':
        user.show_trainings()

    elif choice == '5':
        user.show_performances()

    elif choice == '6':
        user.save_to_file("data/training.json")
        print("Data saved. Exiting...")
        break
    else:
        print("Invalid choice.")