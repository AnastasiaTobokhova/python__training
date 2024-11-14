# School Catalogue
# Let’s put your knowledge of classes to the test by creating a digital school catalog for the New York City Department
# of Education. The Department of Education wants the catalog to hold quick reference material for each school
# in the city.
#
# We need to create classes for primary and high schools.
# Because these classes share properties and methods, each will inherit from a parent School class.
# Our parent and three child classes have the following properties, getters, setters, and methods:
#
# School
# Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'),
# and numberOfStudents (integer)
# Getters: all properties have getters
# Setters: the numberOfStudents property has a setter
# Methods: A __repr__ method that displays information about the school.
# Primary
# Includes everything in the School class, plus one additional property
# Properties: pickupPolicy (string, like "Pickup after 3pm")
# Middle
# Does not include any additional properties or methods
# High
# Includes everything in the School class, plus one additional property
# Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])

class School:
    def __init__(self, name, level, number_of_students):
        self.name = name
        self.level = level
        self.number_of_students = number_of_students

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_number_of_students(self):
        return self.number_of_students

    def set_number_of_students(self, new_number_of_students):
        self.number_of_students = new_number_of_students

    def __repr__(self):
        return f'A {self.level} school named {self.name} with {self.number_of_students} students'


class Primary(School):
    def __init__(self, name, number_of_students, pickup_policy):
        super().__init__(name, 'primary', number_of_students)
        self.pickup_policy = pickup_policy

    def get_pickup_policy(self):
        return self.pickup_policy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + "The pickup policy is {self.pickup_policy}"


class Middle(School):
    def __init__(self, name, number_of_students):
        super().__init__(name, 'Middle', number_of_students)


class High(School):
    def __init__(self, name, number_of_students, sports_team):
        super().__init__(name, 'high', number_of_students)
        self.sports_team = sports_team

    def get_sports_team(self):
        return ['backetball', 'tennis']

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + "The sports team we have {self.sports_team}"


a = School("Codecademy", "high", 100)
print(a)
print(a.get_name())
print(a.get_level())
a.set_number_of_students(200)
print(a.get_number_of_students())

b = Primary("Codecademy", 300, "Pickup Allowed")
print(b.get_pickup_policy())
print(b)

c = High("Codecademy High", 500, ["Tennis", "Basketball"])

