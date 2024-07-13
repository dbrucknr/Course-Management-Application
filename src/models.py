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


from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(index=True, unique=True)
    student: Optional["Student"] = Relationship(back_populates="person")
    instructor: Optional["Instructor"] = Relationship(back_populates="person")


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.id")
    person: Optional[Person] = Relationship(back_populates="student")

# class PublicStudent(Student):
#     person: Person

class Instructor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.id")
    person: Optional[Person] = Relationship(back_populates="instructor")

# class Admin(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
    