from instructor import Instructor
from exercise import Exercise
from student import Student
from cohort import Cohort

# Exercises
joes_sheep_pen = Exercise('Joe\'s Sheep Pen', 'CSharp')
hogwarts_sorting_hat = Exercise('Hogwarts sorting hat', 'COBAL')
tamagotchi = Exercise('Tamagotchi', 'JavaScript')
pet_adoption_center = Exercise('Pet Adoption Center', 'Java')

# Students
brian = Student('Brian', 'Cravens', 'b.craven', 'Cohort 40')
daniel = Student('Daniel', 'Meza', 'd.meza', 'Cohort 47')
john = Student('John', 'Bain', 'j.bain', 'Cohort 40')
adrian = Student('Adrian', 'Garmendia', 'a.garmendia', 'Cohort 40')
patton = Student('Patton', 'Oswalt', 'p.oswalt', 'Cohort 100000')

# Instructors
bryan = Instructor('Bryan', 'Nilsen', 'b.nilsen', 'Reading while walking', 'Cohort 40')
joe = Instructor('Joe', 'Shepard', 'j.shepard', 'announcing minor league baseball games', 'Cohort 100000')
madi = Instructor('Madi', 'Peper', 'm.peper', 'running in circles without losing balance', 'Cohort 47')

# instructors assigning exercises
bryan.assign_exercise(daniel, joes_sheep_pen)
bryan.assign_exercise(daniel, hogwarts_sorting_hat)
bryan.assign_exercise(brian, tamagotchi)
bryan.assign_exercise(brian, joes_sheep_pen)
joe.assign_exercise(john, pet_adoption_center)
joe.assign_exercise(john, tamagotchi)
joe.assign_exercise(adrian, pet_adoption_center)
joe.assign_exercise(adrian, hogwarts_sorting_hat)
madi.assign_exercise(patton, hogwarts_sorting_hat)
madi.assign_exercise(patton, tamagotchi)
madi.assign_exercise(daniel, pet_adoption_center)
madi.assign_exercise(john, hogwarts_sorting_hat)


# Cohorts
cohort_40 = Cohort('Cohort 40')
cohort_40.students.extend([brian, daniel])
cohort_40.instructors.extend([bryan])
cohort_47 = Cohort('Cohort 47')
cohort_47.students.extend([john, adrian])
cohort_47.instructors.extend([madi])
cohort_100000 = Cohort('Cohort 100000')
cohort_100000.students.extend([patton])
cohort_100000.instructors.extend([joe])

# Students List
students = [brian, daniel, john, adrian, patton]

# Exercises list
exercises = [hogwarts_sorting_hat, pet_adoption_center, tamagotchi, joes_sheep_pen]

def student_report():
    for student in students:
        assigned_exercises = []
        for exercise in student.exercises_collection:
            assigned_exercises.append(exercise.name)
        print(f'{student.first_name} is working on {" and ".join(assigned_exercises)}')

student_report()
