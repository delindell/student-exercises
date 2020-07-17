class Student:
    
    def __init__(self, first_name, last_name, slack_handle, cohort_name):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort_name = cohort_name
        self.exercises_collection = []

    def add_exercise(self, exercise):
        self.exercises_collection.append(exercise)

    def __str__(self):
        return f'The students name is {self.first_name}'
        