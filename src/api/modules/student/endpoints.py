from functools import partial
from database import *

async def all(
    records: PaginatedResponse[Student] = Depends(
        partial(select_all_paginated, Student)
    )
) -> PaginatedResponse[Student]:
    return records