from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.routes import api_router

def create_app():
    app = FastAPI(debug=True)

    app.add_middleware(SessionMiddleware, secret_key="your-secret-key") 

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )

    app.include_router(api_router)

    return app