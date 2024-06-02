from decouple import config
from enum import Enum;

class AppSettings(str, Enum):
    APP_NAME =  config("APP_NAME", default="FastAPI App");
