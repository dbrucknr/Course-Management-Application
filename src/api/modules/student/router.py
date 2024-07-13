from fastapi import APIRouter

from api.modules.student import endpoints
from database import *

router = APIRouter(prefix="/students")

router.add_api_route(
    path="/",
    endpoint=endpoints.all,
    response_model=PaginatedResponse[PublicStudent]
)
