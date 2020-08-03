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

    def all_js_exercises(self):
            
            """Retrieve all exercises"""
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
            
            """Retrieve all exercises"""
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

reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_js_exercises()

