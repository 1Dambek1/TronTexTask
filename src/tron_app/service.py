from sqlalchemy import select
from src.models.TronDataModel import WalletInfo
from sqlalchemy.ext.asyncio import AsyncSession

from loguru import logger

from .schema import FilterEnum, WalletResponse


async def create_wallet_info(db: AsyncSession, address: str, data: dict) -> WalletResponse:
    wallet = WalletInfo(
        address=address,
        balance=data["balance"],
        bandwidth=data["bandwidth"],
        energy=data["energy"]
    )
    db.add(wallet)
    await db.commit()

    logger.info(f"{address} was created acces in db")

    await db.refresh(wallet)
    return wallet

async def filter_wallet_info_pagination(db: AsyncSession, skip: int, limit: int, filter:FilterEnum | None)-> list[WalletResponse]:

    subQuery= select(WalletInfo).offset(skip).limit(limit)
    if filter:
     if filter.value == "desc":
       query = subQuery.order_by(WalletInfo.created_at.desc())
     elif filter.value == "asc":
       query = subQuery.order_by(WalletInfo.created_at.asc())
    else:
       query = subQuery
    data = (await db.scalars(query)).all()
    return data
