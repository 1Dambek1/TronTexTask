import datetime
import enum
from pydantic import BaseModel


class WalletResponse(BaseModel):
    id: int
    address: str
    balance: float
    bandwidth: int
    energy: int
    created_at: datetime.datetime

class TronWalletResponse(BaseModel):
    address: str
    balance: float
    bandwidth: int
    energy: int
   
class FilterEnum(enum.Enum):
    desc = "desc"
    asc = "asc"
