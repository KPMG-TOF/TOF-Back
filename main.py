from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.analysis import analysis_router
from domain.upload import upload_router
from domain.docs import docs_router
from domain.rfp import rfp_router

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:3030",  # Add this line to allow access from http://localhost:3030

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
app.include_router(docs_router.router)
app.include_router(rfp_router.router)