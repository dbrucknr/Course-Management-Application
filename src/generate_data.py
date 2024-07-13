from typing import AsyncIterator
import random
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from faker import Faker
from asyncstdlib import map
from models import Person, Student, Instructor
from main import database

fake = Faker()

async def check_if_data_exists() -> bool:
    async for session in database.get_session():
        statement = select(Person)
        result = await session.exec(statement)
        people = result.first()
        return True if people else False

async def generate_person(name: str) -> Person | None:
    async for session in database.get_session():
        email_prefix = name.replace(" ", "_").lower()
        person = Person(name=name, email=f"{ email_prefix }@university.edu")
        # Check if email already exists
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
        student = Student(person_id=person.id)
        session.add(student)
        await session.commit()
        await session.refresh(instance=student)

async def generate_instructor(person: Person) -> Instructor:
    async for session in database.get_session():
        instructor = Instructor(person_id=person.id)
        session.add(instructor)
        await session.commit()
        await session.refresh(instance=instructor)

async def generate_name(_: int) -> str:
    return fake.name()

async def generate_names(n: int) -> AsyncIterator[str]:
    names: AsyncIterator[str] = map(generate_name, range(n))
    return names

async def generate(name: str) -> None:
    person = await generate_person(name)
    if person:
        number = random.randint(1, 3)
        if number == 1:
            await generate_instructor(person)
        else:
            await generate_student(person)

async def generate_data() -> None:
    names = await generate_names(7000)
    [await generate(name) async for name in names]
