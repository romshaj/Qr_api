from jose import JWTError, jwt
from passlib.context import CryptContext

# Configuration des paramètres du JWT
SECRET_KEY = "https://smartone.ai"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 1

# Contexte de hachage des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Fonction pour authentifier l'utilisateur
def authenticate_user(username: str, password: str):
    user = getpass(username, password)
    if not user:
        return False
    return True


def getpass(username: str, password: str):
    if username == "ninja" and password == "felin":
        return True
    return False
    # return True


# Fonction pour créer un token d'accès
def create_access_token(data: dict):
    to_encode = data.copy()
    to_encode.update({"exp": 9000})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
