from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi import status

api_router = APIRouter()

# Route for leetcode
@api_router.get("/leetcode")
async def leetcode():
    return status.HTTP_200_OK

# Route for chodechef
@api_router.get("/codechef")
async def codechef():
    return status.HTTP_200_OK

