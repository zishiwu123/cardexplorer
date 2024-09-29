from enum import Enum
from pydantic import BaseModel


class CardRarity(Enum):
    COMMON = 'Common'
    UNCOMMON = 'Uncommon'
    RARE = 'Rare'
    SUPER_RARE = 'Super Rare'
    LEGENDARY = 'Legendary'
    ENCHANTED = 'Enchanted'

class InkColor(Enum):
    AMBER = 'Amber'
    AMETHYST = 'Amethyst'
    EMERALD = 'Emerald'
    RUBY = 'Ruby'
    SAPPHIRE = 'Sapphire'
    STEEL = 'Steel'

class Card(BaseModel):
    id: int
    name: str
    set_number: int
    card_number: str # Dalmatian puppy has value '4a' so this field must be string
    ink_color: InkColor
    rarity: CardRarity
