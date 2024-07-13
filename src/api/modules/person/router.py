from fastapi import APIRouter

from api.modules.person import endpoints
from database import *

router = APIRouter(prefix="/test")

router.add_api_route(
    path="/people",
    endpoint=endpoints.people,
    response_model=PaginatedResponse[PersonPublic]
)