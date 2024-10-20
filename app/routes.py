from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi import status

# Create a Router for routes
api_router = APIRouter()

# Simulating the resources and IP set
ip_set = set()

# Example functions (log_resource_usage, intro)
def log_resource_usage():
    # Simulate resource usage logging
    return {"cpu": "20%", "memory": "50%"}

def intro():
    # Simulate an introduction message
    return {"message": "Welcome to the API"}

# Route to check resource usage
@api_router.get("/resource_usage")
async def check_resource():
    return log_resource_usage()

# Default route
@api_router.get("/")
async def default():
    return intro()

# Route to get list of IPs
@api_router.get("/get_ip")
async def get_ip():
    ip_address = list(ip_set)
    return JSONResponse(content=ip_address, status_code=status.HTTP_200_OK)

# Route to set IP
@api_router.get("/set_ip")
async def set_ip(request: Request):
    ip_address = request.headers.get('X-Forwarded-For', request.client.host)
    ip_set.add(ip_address)
    return "IP Received", status.HTTP_200_OK
