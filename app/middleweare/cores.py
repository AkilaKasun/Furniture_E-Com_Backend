import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app: FastAPI) -> None:
    frontend_domain = os.getenv("FRONTEND_DOMAIN", "http://localhost:4200").strip()

    origins = [
        frontend_domain,
        "http://127.0.0.1:4200",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )