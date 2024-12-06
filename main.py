from fastapi import FastAPI
from routes import qrcode_routes, tokenizer_routes
from fastapi.middleware.cors import CORSMiddleware

# Création de l'application FastAPI
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routes
app.include_router(qrcode_routes.router, prefix="/qrcode", tags=["qrcode"])
app.include_router(tokenizer_routes.router, tags=["token"])

@app.get("/")
def read_root():
    return {"Hello": "World"}