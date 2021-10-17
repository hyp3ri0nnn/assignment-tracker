import json

from database_ import Database
from course import Course, Assignment
from datetime import date 
import pandas as pd 

class Calender:
    """A calender template."""

    def __init__(self):
        
        self.modified = ''
        self.database = Database()
        self.original = self.database.load_courses()


    def print_calender(self):
        """Print that calender to the console."""        
        courses = self.original["courses"]
        for i in courses:
            name_of_course = i["name"]
            code_of_course = i["code"]
            teacher = i["teacher"]
            assignments = i["assignments"]
            ass_table = pd.DataFrame(assignments)
            # print(table)
            print(f"\n{code_of_course:>20} - {name_of_course} - {teacher}\n")
            print(ass_table)
            print("---------------------------------------------------------")


    def __len__(self):
        return len(self.original["courses"])


    def add_new_course(self):
        """Add new course and save it to json file."""
        print("set the course attributes: \n (Do not enter any value to use defaults.")
        code = input("Enter the Code of course(required): ")
        name = input("Enter the name of course(optional): ")
        teacher = input("Enter name of the teacher(optional): ")
        assignments = []
        
        course = Course(code, name, teacher, assignments)
        course_json = course.course_json()
        self.original["courses"].append(course_json)
        self.modified = self.original
        self.database.write_all_changes(self)


    def add_new_assignment(self):
        """Add new assignment and save it to json file."""
        choice = self.choose_course()
        print("set assignment variables: \n (Do not enter any value to use defaults.")
        name = str(input("Name(required): "))
        start_date = input("Start date(dd-mm-yyyy -> ex: 12-10-2021):(optional)")
        finish_date = input("Finish date(dd-mm-yyyy -> ex: 12-10-2021): (optional)")
        done = str(input("Did it finished(y/n): (optional)"))
        if not start_date: 
            start_date = date.today()
            start_date = start_date.strftime("%d-%m-%Y")
        if done == "y":
            done = 1
        else: done = 0
        assignment = Assignment(name, start_date, finish_date, done)
        assignment = assignment.ass_json()
        choice["assignments"].append(assignment)
        self.modified = self.original
        self.database.write_all_changes(self)

    def choose_course(self):
        """Return a chosen course.
            Raise an error if not exist."""

        options = self.original["courses"]
        print("Choose from here(Select 0 for new course): \n")
        for opt in range(len(options)):
            print(f"Press {opt + 1} for ->  {options[opt]['code']}")

        choice = int(input()) - 1
        if not (len(options) > choice >= 0):
            raise IndexError
        else:
            course = options[choice]
            return course 

    
        # print(options)
        # course_code = input()


new = Calender()
# new.add_new_assignment()
# new.add_new_course()
new.print_calender()
print(len(new))
# print("before")
# new.print_calender()
# new.new_courses()
# new.add_all()
# print("new")
# new.print_calender()