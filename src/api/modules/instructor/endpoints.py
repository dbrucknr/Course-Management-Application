from functools import partial
from database import *

async def all(
    records: PaginatedResponse[Instructor] = Depends(
        partial(select_all_paginated, Instructor)
    )
) -> PaginatedResponse[Instructor]:
    return records