from fastapi import FastAPI
from .data import load_cards

app = FastAPI()
cards = load_cards()

@app.get("/")
async def root():
    return {"cards": load_cards()}
