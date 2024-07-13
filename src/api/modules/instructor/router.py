from fastapi import APIRouter

from api.modules.instructor import endpoints
from database import *

router = APIRouter(prefix="/instructors")

router.add_api_route(
    path="/",
    endpoint=endpoints.all,
    response_model=PaginatedResponse[PublicInstructor]
)