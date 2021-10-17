import json
import pandas as pd


class Database:

    def __init__(self):
       
        self.courses = self.load_courses()


    def load_courses(self):
        """Load all courses from database."""
        with open("new_file.json", "r") as file:
            data = file.read()
            df = json.loads(data)
        file.close()
        return df

    
    def write_all_changes(self, calender):
        """Write all changes to database."""
        changes = calender.modified
        with open ("new_file.json","w") as file:
            data = json.dumps(changes, indent=2)
            file.write(data)
        file.close()
