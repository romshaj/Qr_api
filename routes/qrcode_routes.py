from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from dataclasses import dataclass
from controllers.qr_controller import save_qr
from jose import JWTError, jwt
from fastapi import Form
from controllers.token_controller import SECRET_KEY, ALGORITHM, getpass
from typing import Annotated
import time
from pydantic import BaseModel
from typing import Optional

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()


@dataclass
class QrCode(BaseModel):
    id_client: str
    id_id: str
    #nom_client: str | None = None
    nom_client: Optional[str] = None


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options={'verify_exp':False})
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        else:
            userpass = username.split("  +  ")
            username = userpass[0]
            passw = userpass[1]
            testuserldap = getpass(username, passw)
            if not testuserldap:
                raise credentials_exception
    except JWTError:
        raise credentials_exception
    return True


@router.post("/save")
def read(item: QrCode, token: Annotated[str, Depends(get_current_user)]):
    data = item.dict()
    save_qr(data)
    return {"message": "Save OK", "status": True}
