class Cohort:

    def __init__(self, name):
        self.name = name
        self.student_collection = []
        self.instructor_collection = []

    def __str__(self):
        return 'This is {self.name}'
