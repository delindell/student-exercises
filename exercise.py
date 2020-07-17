class Exercise:

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __str__(self):
        return f'The name of the exercise is {self.name} in {self.language}'
        