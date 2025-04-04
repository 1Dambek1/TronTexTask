from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi.concurrency import run_in_threadpool

from .utils import fetch_wallet_data
from .schema import  WalletResponse, FilterEnum
from .service import create_wallet_info, filter_wallet_info_pagination
from loguru import logger

from src.db import get_session


app = APIRouter(prefix="/tron", tags=["tron"])

@app.post("/wallet", response_model=WalletResponse)
async def get_wallet_info(address:str, session: Session = Depends(get_session)):
    wallet = await run_in_threadpool(fetch_wallet_data, address)
    if not wallet:
        logger.info(f"{address} is not found")
        raise HTTPException(status_code=400, detail="Invalid address")
    saved_wallet = await create_wallet_info(session, address, wallet)
    return saved_wallet

@app.get("/wallets", response_model=list[WalletResponse])
async def list_wallets(skip: int = 0, limit: int = Query(default=10, le=50),createdAtFilter:FilterEnum = None, session: Session = Depends(get_session)):
    wallet = await filter_wallet_info_pagination(session, skip, limit,createdAtFilter)
    return wallet
