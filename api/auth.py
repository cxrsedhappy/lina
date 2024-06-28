from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from core.config import setting

router = APIRouter(prefix='/auth', tags=['Auth'])

SECRET_KEY = setting.SECRET_KEY
ALGORITHM = setting.ALGORITHM

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth_bearer = OAuth2PasswordBearer(tokenUrl=' auth/token')



