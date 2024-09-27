import csv
from pathlib import Path
from typing import List, Optional
from .card import Card, CardRarity, InkColor

BASE_PATH_DIR = Path(__file__).parent

def search_cards(
    cards: List[Card],
    card_name: Optional[str] = None,
    set_number: Optional[int] = None,
    card_number: Optional[str] = None,
    ink_color: Optional[InkColor] = None,
    rarity: Optional[CardRarity] = None) -> List[Card]:

    matching_cards = cards
    if card_name:
        matching_cards = [c for c in matching_cards if card_name.lower() in c.name.lower()]
    if set_number:
        matching_cards = [c for c in matching_cards if set_number == c.set_number]
    if card_number:
        matching_cards = [c for c in matching_cards if card_number.lower() == c.card_number.lower()]
    if ink_color:
        # since InkColor and Rarity are enums, they can't have lowercase input if the enum value is uppercase
        matching_cards = [c for c in matching_cards if ink_color == c.ink_color]
    if rarity:
        matching_cards = [c for c in matching_cards if rarity == c.rarity]
    return matching_cards

def load_cards() -> List[Card]:
    cards = []
    # as_posix() used in case this is running on Windows
    cards_file_path = Path(BASE_PATH_DIR, 'data', 'lorcana_cards.csv').as_posix()
    with open(cards_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cards.append(Card(**row))
    return cards
