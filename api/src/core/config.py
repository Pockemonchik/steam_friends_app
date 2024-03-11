import os
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

class Settings(BaseSettings):
    mode: str = os.environ.get("MODE", "DEV")
    db_url:str = os.environ.get("DB_URL", "locahost")
    db_echo:bool = bool(os.environ.get("DB_ECHO", False))
    kafka_server:str = os.environ.get("KAFKA_SERVER", 'broker:29092')
    kafka_topic:str = os.environ.get("KAFKA_TOPIC", "notify_friends")
    kafka_client_id:str = os.environ.get("KAFKA_CLEIENT_ID",'python-producer')
    
settings = Settings()
