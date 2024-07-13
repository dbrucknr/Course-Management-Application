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

# https://stackoverflow.com/questions/74252768/missinggreenlet-greenlet-spawn-has-not-been-called

class PersonBase(SQLModel):
    name: str
    email: str = Field(index=True, unique=True)

class Person(PersonBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student: Optional["Student"] = Relationship(back_populates="person", sa_relationship_kwargs={'lazy': 'selectin'})
    instructor: Optional["Instructor"] = Relationship(back_populates="person")


class PersonPublic(SQLModel):
    name: str
    email: str

class StudentBase(SQLModel):
    person_id: int = Field(foreign_key="person.id")
    

class Student(StudentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    person: Optional[Person] = Relationship(back_populates="student", sa_relationship_kwargs={'lazy': 'selectin'})

class PublicStudent(StudentBase):
    id: int
    person: PersonPublic




class Instructor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    person_id: int = Field(foreign_key="person.id")
    person: Optional[Person] = Relationship(back_populates="instructor")

# class Admin(SQLModel, table=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
    