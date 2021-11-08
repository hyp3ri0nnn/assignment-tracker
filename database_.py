import json
import pandas as pd
from os.path import exists


class Database:

    def __init__(self):
        
        self.create_database()
        self.courses = self.load_courses()



    def create_database(self):

        database = {"courses":[]}
        if not exists("db/new_file.json"):
            with open("db/new_file.json","w") as file:
                data = json.dumps(database, indent=2)
                file.write(data)
                file.close()


    def load_courses(self):
        """Load all courses from database."""
        with open("db/new_file.json", "r") as file:
            data = file.read()
            df = json.loads(data)
        file.close()
        return df

    
    def write_all_changes(self, calendar):
        """Write all changes to database."""
        changes = calendar.modified
        with open ("db/new_file.json","w") as file:
            data = json.dumps(changes, indent=2)
            file.write(data)
        file.close()
