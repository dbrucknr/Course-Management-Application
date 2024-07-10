# Org Based Models
class University:
    id: int
    name: str

class School:
    """A School Belongs to a University"""
    id: int
    name: str
    university_id: int

class Department:
    """A Department Belongs to a School"""
    id: int
    name: str
    school_id: int

class Course:
    "A Course Belongs to a Department"
    id: int
    name: str
    department_id: int

# Role Based Models
class Person:
    id: int
    name: str
    email: str
    password: str

class Student:
    id: int
    person_id: int

class Instructor:
    id: int
    person_id: int

class Admin:
    id: int
    person_id: int