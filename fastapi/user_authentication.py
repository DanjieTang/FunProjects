from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi import FastAPI, Depends, Form, Request
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from dataclass import *
from database_wrapper import SQLAlchemyWrapper
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from exception import AuthenticationError

server_secret_key = "Danjie's server"
app = FastAPI()
token_expiration_time = timedelta(minutes=15)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
database = SQLAlchemyWrapper("database.db")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_token(token: str) -> bool | int:
    """
    Verify if the token if valid.

    :param token: Token from frontend.
    :return: If token if valid, return user id. Otherwise false.
    """
    try:
        decoded = jwt.decode(token, key=server_secret_key)
        user = database.select_one(User, User.username == decoded["sub"])
        return user.id
    except:
        return False


@app.exception_handler(AuthenticationError)
def token_expired_exception_handler(request, exc: AuthenticationError):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})


@app.post("/create_account")
async def create_account(
    username: str = Form(...),
    password: str = Form(...),
    age: int = Form(...),
    real_name: str = Form(...),
) -> bool:
    """
    Create account for user.

    :param form_data: Containing data for username and password.
    :return: True if user successfully created, false otherwise.
    """
    # Check for duplication
    username = username
    search_result = database.select_first(User, User.username == username)
    if search_result:
        # If some result has been found, meaning username exists.
        return False

    hashed_password = pwd_context.hash(password)
    user = User(
        username=username, real_name=real_name, age=age, hashed_password=hashed_password
    )
    database.insert(user)
    return True


@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> str:
    try:
        # Try and see if user exists in database
        user = database.select_one(User, User.username == form_data.username)
    except:
        raise AuthenticationError()

    if pwd_context.verify(form_data.password, user.hashed_password):
        # If user had entered correct password
        key_info = {
            "sub": form_data.username,
            "exp": datetime.utcnow() + token_expiration_time,
        }
        token = jwt.encode(key_info, key=server_secret_key)
        return token
    else:
        raise AuthenticationError()

@app.post("/open_store")
async def open_store(store_info: Request, token: str = Depends(oauth2_scheme)) -> None:
    # Verify token
    user_id = verify_token(token)
    if user_id == False:
        raise JWTError()

    data = await store_info.json()
    store = Storage(
        store_name=data["store_name"],
        store_location=data["store_location"],
        user_id=user_id,
    )
    database.insert(store)

@app.post("/add_item")
async def add_item(item_info: Request, token: str = Depends(oauth2_scheme)) -> None:
    # Verify token
    user_id = verify_token(token)
    if user_id == False:
        raise JWTError()

    data = await item_info.json()
    item = Item(
        item_name=data["item_name"],
        num=data["num"],
        storage_id=data["storage_id"]
    )
    database.insert(item)

@app.get("/view_all")
async def view_all(token: str = Depends(oauth2_scheme)) -> None:
    # Verify token
    user_id = verify_token(token)
    if user_id == False:
        raise JWTError()

    storages = database.select(Storage, Storage.user_id == user_id)
    for storage in storages:
        items = database.select(Item, Item.storage_id == storage.id)
        print(storage.store_name)
        print("Has " + str(len(items)) + " items:")
        for item in items:
            print(item.item_name)