import csv
from pathlib import Path
from typing import List
from .card import Card

BASE_PATH_DIR = Path(__file__).parent

def load_cards() -> List[Card]:
    cards = []
    # as_posix() used in case this is running on Windows
    cards_file_path = Path(BASE_PATH_DIR, 'data', 'lorcana_cards.csv').as_posix()
    with open(cards_file_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cards.append(Card(**row))
    return cards
