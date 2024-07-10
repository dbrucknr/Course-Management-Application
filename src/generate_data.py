from typing import AsyncIterator
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from faker import Faker
from asyncstdlib import map
from models import Person, Student, Instructor
from main import database

fake = Faker()

async def generate_person(name: str) -> Person:
    async for session in database.get_session():
        email_prefix = name.replace(" ", "_").lower()
        person = Person(name=name, email=f"{ email_prefix }@university.edu")
        statement = select(Person).where(Person.email == person.email)
        result = await session.exec(statement)
        existing_email = result.one_or_none()
        if existing_email:
            return 
        session.add(person)
        await session.commit()
        await session.refresh(instance=person)
        return person

async def generate_student(person: Person) -> Student:
    async for session in database.get_session():
        student = Student(person=person)
        session.add(student)
        await session.commit()
        await session.refresh(instance=student)

async def generate_instructor(person: Person) -> Instructor:
    session: AsyncSession = await database.get_session()
    instructor = Instructor(person=person)
    session.add(instructor)
    await session.commit()
    await session.refresh(instance=instructor)

async def generate_name(_: int) -> str:
    return fake.name()

async def generate_names(n: int) -> AsyncIterator[str]:
    names: AsyncIterator[str] = map(generate_name, range(n))
    return names

async def generate_data():
    # names = [fake.name() for _ in range(10000)]
    names = await generate_names(1000)
    [await generate_person(name) async for name in names]
