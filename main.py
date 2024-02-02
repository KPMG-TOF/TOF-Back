from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.analysis import analysis_router
from domain.upload import upload_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router.router)
app.include_router(upload_router.router)

