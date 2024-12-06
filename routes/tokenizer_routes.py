from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from controllers.token_controller import authenticate_user, create_access_token

router = APIRouter()
security = HTTPBasic()


# Route pour obtenir un token
@router.get("/token")
def login_for_access_token(credentials: HTTPBasicCredentials = Depends(security)):
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": credentials.username+"  +  "+credentials.password}
    )
    return {"access_token": access_token, "token_type": "bearer"}
