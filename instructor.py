from nssPerson import NSSPerson

class Instructor(NSSPerson):

    def __init__(self, first_name, last_name, slack_handle, specialty, cohort_name):
        super().__init__(first_name, last_name, slack_handle, cohort_name)
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.add_exercise(exercise)
