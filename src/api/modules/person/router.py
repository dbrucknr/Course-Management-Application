from fastapi import APIRouter

from api.modules.person import endpoints
from database import *

router = APIRouter(prefix="/people")

router.add_api_route(
    path="/",
    endpoint=endpoints.all,
    response_model=PaginatedResponse[PersonPublic]
)