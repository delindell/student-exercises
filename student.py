from nssPerson import NSSPerson

class Student(NSSPerson):
    
    def __init__(self, first_name, last_name, slack_handle, cohort_name):
        super().__init__(first_name, last_name, slack_handle, cohort_name)
        self.exercises_collection = []

    def add_exercise(self, exercise):
        self.exercises_collection.append(exercise)

    def __str__(self):
        return f'The students name is {self.first_name}'
        