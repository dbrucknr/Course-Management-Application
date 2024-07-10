from sqlmodel.ext.asyncio.session import AsyncSession

from models import Person, Student, Instructor
from main import database

async def generate_person(name: str) -> Person:
    # session: AsyncSession = await database.get_session()
    async for session in database.get_session():
        person = Person(name=name, email=f"{ name.lower() }@university.edu")
        session.add(person)
        await session.commit()
        await session.refresh(person)
        return person

async def generate_student(person: Person) -> Student:
    session: AsyncSession = await database.get_session()
    student = Student(person=person)

async def generate_instructor(person: Person) -> Instructor:
    session: AsyncSession = await database.get_session()
    instructor = Instructor(person=person)