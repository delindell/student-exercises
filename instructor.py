class Instructor:

    def __init__(self, first_name, last_name, slack_handle, specialty, cohort_name):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.specialty = specialty
        self.cohort_name = cohort_name

    def assign_exercise(self, student, exercise):
        student.add_exercise(exercise)
