from fastapi import FastAPI
from .routers import messages, users, auth
from .database import Base, engine
from fastapi.middleware.cors import CORSMiddleware


api = FastAPI()

origins = ["*"]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

api.include_router(messages.router)
api.include_router(users.router)
api.include_router(auth.router)