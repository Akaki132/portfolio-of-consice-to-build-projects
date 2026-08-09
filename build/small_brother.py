import time

"""
will track danger, constant of more then 100 will represent
assastination attempt regardless of sophistication level of attempt 
"""

def get_danger_level():
    pass



class Person:
    def __init__(self, name=None, birthplace=None):
        self.name = name
        self.birthplace = birthplace

class   President(Person):
    def __init__(self, person=None, location=None, danger=None):
        self.person = person
        self.location = location
        self.danger = danger

    def track_danger(person, location, danger):
        while person in location:
            if get_danger_level() > 100:
                return "active assastination attempt"
            else:
                time.sleep(1)