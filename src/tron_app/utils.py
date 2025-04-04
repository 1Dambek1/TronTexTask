from tronpy import Tron
from tronpy.providers import HTTPProvider
from src.config import config
from loguru import logger
from .schema import TronWalletResponse

client = Tron(HTTPProvider(api_key=config.tron_data.TRON_API_KEY))

def fetch_wallet_data(address: str) -> TronWalletResponse | None:
    try:
        acc =  client.get_account(address)
        resources =  client.get_account_resource(address)

        return {
            "address": address,
            "balance": acc.get("balance", 0) / 1_000_000,
            "bandwidth": resources.get("free_net_limit", 0),
            "energy": resources.get("EnergyLimit", 0)
        }
    except Exception as e:
        logger.error(f"when {address} start searching was error {e}")
        return None
