from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from .card import CardRarity, InkColor
from .data import search_cards, load_cards

app = FastAPI()
cards = load_cards()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root(
    card_name: Optional[str] = None,
    set_number: Optional[int] = None,
    card_number: Optional[str] = None,
    ink_color: Optional[InkColor] = None,
    rarity: Optional[CardRarity] = None):
    return {"cards": search_cards(cards, card_name, set_number, card_number, ink_color, rarity)}
