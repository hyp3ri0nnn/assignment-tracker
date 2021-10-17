import json
from datetime import datetime, date

class Course:
    """A course template. """

    def __init__(self, code, name=None, teacher=None, assignments=[]):

        self.code = code 
        self.name = name
        self.teacher = teacher 
        self.assignments = assignments


    def course_json(self):
        """Return a json format of course."""
        course = {"name" : self.name,
                "teacher": self.teacher,
                "code": self.code,
                "assignments":self.assignments}
        return course


class Assignment:

    def __init__(self,assignment_name, started_date, finished_date, done):
        """An assignment template for course."""
        self.ass_name = assignment_name
        self.started_date = started_date
        self.finish_date = finished_date
        self.finished = done


    def ass_json(self):
        """Return json format of assignment."""
        assignment = {"name": self.ass_name,
                    "started" : self.started_date,
                    "deadline": self.finish_date,
                    "done":self.finished}
        return assignment


