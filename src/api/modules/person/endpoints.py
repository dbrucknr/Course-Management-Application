from functools import partial
from database import *

async def people(
    records: PaginatedResponse[Person] = Depends(
        partial(select_all_paginated, Person)
    )
) -> PaginatedResponse[Person]:
    return records