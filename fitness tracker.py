import datetime
# Define class to represent a Workout
class Workout:
    def __init__(self, workout_name, date,time_period):
        self.workout_name = workout_name
        self.date = date
        self.time_period = time_period

    def __str__(self):
        return f"logged workout - {self.workout_name} on {self.date} of duration {self.time_period} minutes"

# Define class to manage the Fitness Tracker
class FitnessTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout_name, time_period):
        date = datetime.date.today().strftime("%d/%m/%Y")
        new_workout = Workout(workout_name,date,time_period)
        self.workouts.append(new_workout)
        print(f"Workout added: {new_workout}")

    def view_workouts(self):
        if not self.workouts:
            print("No workouts logged.")
        else:
            print("Logged Workouts:")
            for workout in self.workouts:
                print(workout)
def main():
    tracker = FitnessTracker()
    while True:
        print("\nFitness Tracker:")
        print("1. Add Workout")
        print("2. View Workouts")
        print("3. Exit")
        choice = input("Choose an option(1/2/3): ")

        if choice == '1':
            workout_name = input("Enter workout name(🏃🏿/ 🏋🏿‍♀️/ 🚴🏿‍♀️/ 🤸🏿/ 💪🏿) : ")
            time_period = input("Enter time_period in minutes: ")
            try:
                time_period = int(time_period)
                tracker.add_workout(workout_name, time_period)
            except ValueError:
                print("Invalid time_period. Please enter a number.")
        elif choice == '2':
            tracker.view_workouts()
        elif choice == '3':
            print("Exiting Fitness Tracker......")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
