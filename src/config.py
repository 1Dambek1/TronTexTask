from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR  = Path(__file__).parent.parent

class EnvData(BaseSettings):
    DB_URl:str
    DB_URl_ASYNC:str

class TronSetUp(BaseSettings):

    TRON_API_KEY:str

class Config(BaseModel):

    env_data:EnvData = EnvData()
    tron_data:TronSetUp = TronSetUp()

config = Config()
