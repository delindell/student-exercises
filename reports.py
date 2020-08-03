import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __str__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'


class Cohort():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

class Exercise():
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name}'

class JavaScript():
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'JS exercise {self.name}'      

class Python():
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.language} exercise {self.name}' 

class CSharp():
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.language} exercise {self.name}'

class StudentCohorts():
    def __init__(self, first, last, cohort):
        self.first = first
        self.last = last
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first} {self.last} is in {self.cohort}'

class InstructorCohorts():
    def __init__(self, first, last, cohort):
        self.first = first
        self.last = last
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first} {self.last} teaches {self.cohort}'

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/davis/workspace/python/exercises/studentExercises/student_exercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from students s
            join cohorts c on s.cohort_id = c.id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

    def all_cohorts(self):
            
            """Retrieve all cohorts with the cohort name"""
            with sqlite3.connect(self.db_path) as conn:
                
                conn.row_factory = lambda cursor, row: Cohort(row  [1])
                
                db_cursor = conn.cursor()
                
                db_cursor.execute("""
                select c.id,
                    c.name
                from cohorts c
                order by c.name
                """)
                all_cohorts = db_cursor.fetchall()
                
                for cohort in all_cohorts:
                    print(cohort)   

    def all_js_exercises(self):
            
            """Retrieve all JS exercises"""
            with sqlite3.connect(self.db_path) as conn:
                
                conn.row_factory = lambda cursor, row: JavaScript(row[1], row[2])
                
                db_cursor = conn.cursor()
                
                db_cursor.execute("""
                select e.id,
                    e.name,
                    e.language
                from exercises e
                where e.language = 'JavaScript'
                order by e.name
                """)
                all_exercises = db_cursor.fetchall()
                
                for exercise in all_exercises:
                    print(exercise)

    def all_python_exercises(self):
            
            """Retrieve all Python exercises"""
            with sqlite3.connect(self.db_path) as conn:
                
                conn.row_factory = lambda cursor, row: Python(row[1], row[2])
                
                db_cursor = conn.cursor()
                
                db_cursor.execute("""
                select e.id,
                    e.name,
                    e.language
                from exercises e
                where e.language = 'Python'
                order by e.name
                """)
                all_exercises = db_cursor.fetchall()
                
                for exercise in all_exercises:
                    print(exercise)

    def all_csharp_exercises(self):
            
            """Retrieve all C# exercises"""
            with sqlite3.connect(self.db_path) as conn:
                
                conn.row_factory = lambda cursor, row: CSharp(row[1], row[2])
                
                db_cursor = conn.cursor()
                
                db_cursor.execute("""
                select e.id,
                    e.name,
                    e.language
                from exercises e
                where e.language = 'C#'
                order by e.name
                """)
                all_exercises = db_cursor.fetchall()
                
                for exercise in all_exercises:
                    print(exercise)

    def all_students_in_cohorts(self):
            
            """Retrieve all students in cohorts"""
            with sqlite3.connect(self.db_path) as conn:
                
                conn.row_factory = lambda cursor, row: StudentCohorts(row[1], row[2], row[5])
                
                db_cursor = conn.cursor()
                
                db_cursor.execute("""
                SELECT s.id,
                s.first_name,
                s.last_name,
                s.cohort_id,
                c.id,
                c.name
                FROM students s
                join cohorts c 
                on c.id = s.cohort_id
                order by c.name; 
                """)

                all_students = db_cursor.fetchall()
                
                for student in all_students:
                    print(student)

    def all_instructors_in_cohorts(self):
            
            """Retrieve all instructors in cohorts"""
            with sqlite3.connect(self.db_path) as conn:
                
                conn.row_factory = lambda cursor, row: InstructorCohorts(row[1], row[2], row[5])
                
                db_cursor = conn.cursor()
                
                db_cursor.execute("""
                SELECT i.id,
                i.first_name,
                i.last_name,
                i.cohort_id,
                c.id,
                c.name
                FROM instructors i
                JOIN cohorts c
                on c.id = i.cohort_id
                order by c.name;
                """)

                all_instructors = db_cursor.fetchall()
                
                for instructor in all_instructors:
                    print(instructor)

    def students_with_exercises(self):

        exercises = dict()
        student_workload = dict()
        popular_exercises = dict()

        """Retrieve all exercises assigned to students"""

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
            e.id exercise_id,
            e.name,
            s.id,
            s.first_name,
            s.last_name
            FROM exercises e
            JOIN student_exercises se on se.exercise_id = e.id
            JOIN students s on s.id = se.student_id;
            """)

        data_set = db_cursor.fetchall()

        """"Grouping by student workload"""

        for row in data_set:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if student_name not in student_workload:
                student_workload[student_name] = [exercise_name]
            else:
                student_workload[student_name].append(exercise_name)

        for student_name, exercises in student_workload.items():
            print(f'{student_name} is working on:')
            for exercise in exercises:
                print(f'\t* {exercise}')

        """"Grouping by popular exercises"""

        for row in data_set:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'

            if exercise_name not in popular_exercises:
                popular_exercises[exercise_name] = [student_name]
            else:
                popular_exercises[exercise_name].append(student_name)

        for exercise_name, students in popular_exercises.items():
            print(f'{exercise_name} is being worked on by:')
            for student in students:
                print(f'\t* {student}')

    def instructor_assignments(self):

        """"Getting exercises assigned by instructors"""

        assigned_exercises = dict()
        student_assigned_exercises_with_instuctors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
            e.id exercise_id,
            e.name,
            s.id,
            s.first_name student_first,
            s.last_name student_last,
            s.cohort_id,
            c.id,
            i.id,
            i.first_name,
            i.last_name,
            i.cohort_id
            FROM exercises e
            JOIN student_exercises se on se.exercise_id = e.id
            JOIN students s on s.id = se.student_id
            JOIN cohorts c on c.id = s.cohort_id
            JOIN instructors i on i.cohort_id = c.id;
            """)

        data_set = db_cursor.fetchall()

        for row in data_set:
            exercise_id = row[0]
            exercise_name = row[1] 
            instructor_id = row[2]
            instructor_name = f'{row[8]} {row[9]}'

            if instructor_name not in assigned_exercises:
                assigned_exercises[instructor_name] = [exercise_name]
            else:
                assigned_exercises[instructor_name].append(exercise_name)

        for instructor_name, exercises in assigned_exercises.items():
            print(f'{instructor_name} has assigned:')
            for exercise in exercises:
                print(f'\t* {exercise}')

        for row in data_set:
            exercise_id = row[0]
            exercise_name = row[1]
            student_id = row[2]
            student_name = f'{row[3]} {row[4]}'
            instructor_name = f'{row[8]} {row[9]}'

            if exercise_name not in student_assigned_exercises_with_instuctors:
                student_assigned_exercises_with_instuctors[exercise_name] = [instructor_name]
                student_assigned_exercises_with_instuctors[exercise_name] = [student_name]
            else:
                student_assigned_exercises_with_instuctors[exercise_name].append(instructor_name)
                student_assigned_exercises_with_instuctors[exercise_name].append(student_name)

            print(student_assigned_exercises_with_instuctors)
        # for exercise_name, students, instructors in student_assigned_exercises_with_instuctors.items():
        #     print(f'{exercise_name}:')
        #     for student in students:
        #         for instructor in instructors:
        #             print(f'{instructor} has assigned this to {student}')

reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_js_exercises()
reports.all_python_exercises() 
reports.all_csharp_exercises()
reports.all_students_in_cohorts() 
reports.all_instructors_in_cohorts()
reports.students_with_exercises()
reports.instructor_assignments() 


