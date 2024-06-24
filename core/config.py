import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Setting(BaseModel):
    DB_URL: str = os.environ.get('DATABASE_URI')
    DB_ECHO: bool = True


setting = Setting()