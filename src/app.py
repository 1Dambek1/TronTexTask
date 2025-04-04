from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.db import engine, Base
from src.tron_app.router import app as tron_app


app = FastAPI(title="TronSearcher", version="1")

# ROUTERS
app.include_router(tron_app)

# SETUP APPS
from src.logging_config import setup_logging

setup_logging()

# CORS

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

# DB(DEBUG)

async def create_db():

    async with engine.begin() as conn:
        try:
            await conn.run_sync(Base.metadata.drop_all)
        except:
            pass
        await  conn.run_sync(Base.metadata.create_all)
@app.get("/db")
async def create():
    await create_db()
    return True






