from fastapi import FastAPI
from typing import Optional
from .card import CardRarity, InkColor
from .data import search_cards, load_cards

app = FastAPI()
cards = load_cards()

@app.get("/")
async def root(
    card_name: Optional[str] = None,
    set_number: Optional[int] = None,
    card_number: Optional[str] = None,
    ink_color: Optional[InkColor] = None,
    rarity: Optional[CardRarity] = None):
    return {"cards": search_cards(cards, card_name, set_number, card_number, ink_color, rarity)}
