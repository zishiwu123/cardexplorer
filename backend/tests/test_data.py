from typing import Dict, List
import unittest
from app.card import Card, CardRarity, InkColor
from app.data import load_cards, search_cards

def json_to_card(card_json_list: List[Dict]) -> List[Card]:
    return [Card(**card_json) for card_json in card_json_list]

class TestLoadCards(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._cards = load_cards()

    def test_num_total_cards(self):
        actual = len(self._cards)
        NUM_CARDS_AFTER_SET_5 = 1107
        self.assertEqual(actual, NUM_CARDS_AFTER_SET_5)

    def test_search_cards_by_name(self):
        CARD_NAME_SUBSTRING = "Ariel"
        actual = search_cards(self._cards, CARD_NAME_SUBSTRING, None, None, None, None)
        expected = json_to_card([
            {
                "id": 1,
                "name": "Ariel - On Human Legs",
                "set_number": 1,
                "card_number": "1",
                "ink_color": "Amber",
                "rarity": "Uncommon"
            },
            {
                "id": 2,
                "name": "Ariel - Spectacular Singer",
                "set_number": 1,
                "card_number": "2",
                "ink_color": "Amber",
                "rarity": "Super Rare"
            },
            {
                "id": 137,
                "name": "Ariel - Whoseit Collector",
                "set_number": 1,
                "card_number": "137",
                "ink_color": "Sapphire",
                "rarity": "Rare"
            },
            {
                "id": 539,
                "name": "Ariel - Adventurous Collector",
                "set_number": 3,
                "card_number": "103",
                "ink_color": "Ruby",
                "rarity": "Super Rare"
            },
            {
                "id": 662,
                "name": "Ariel - Singing Mermaid",
                "set_number": 4,
                "card_number": "3",
                "ink_color": "Amber",
                "rarity": "Rare"
            },
            {
                "id": 798,
                "name": "Ariel - Treasure Collector",
                "set_number": 4,
                "card_number": "139",
                "ink_color": "Sapphire",
                "rarity": "Super Rare"
            },
            {
                "id": 828,
                "name": "Ariel's Grotto - A Secret Place",
                "set_number": 4,
                "card_number": "169",
                "ink_color": "Sapphire",
                "rarity": "Rare"
            },
            {
                "id": 833,
                "name": "Ariel - Determined Mermaid",
                "set_number": 4,
                "card_number": "174",
                "ink_color": "Steel",
                "rarity": "Common"
            },
            {
                "id": 834,
                "name": "Ariel - Sonic Warrior",
                "set_number": 4,
                "card_number": "175",
                "ink_color": "Steel",
                "rarity": "Super Rare"
            },
            {
                "id": 878,
                "name": "Ariel's Grotto - A Secret Place",
                "set_number": 4,
                "card_number": "219",
                "ink_color": "Sapphire",
                "rarity": "Enchanted"
            },
            {
                "id": 879,
                "name": "Ariel - Sonic Warrior",
                "set_number": 4,
                "card_number": "220",
                "ink_color": "Steel",
                "rarity": "Enchanted"
            }
        ])
        self.assertEqual(actual, expected)

    def test_search_cards_by_name_and_set_number(self):
        # Don't do a search by set number attribute alone because that is too many cards!
        # Same goes for the rarity and ink color attributes.
        CARD_NAME_SUBSTRING = "Ariel"
        SET_NUMBER = 1
        actual = search_cards(self._cards, CARD_NAME_SUBSTRING, SET_NUMBER, None, None, None)
        expected = json_to_card([
            {
                "id": 1,
                "name": "Ariel - On Human Legs",
                "set_number": 1,
                "card_number": "1",
                "ink_color": "Amber",
                "rarity": "Uncommon"
            },
            {
                "id": 2,
                "name": "Ariel - Spectacular Singer",
                "set_number": 1,
                "card_number": "2",
                "ink_color": "Amber",
                "rarity": "Super Rare"
            },
            {
                "id": 137,
                "name": "Ariel - Whoseit Collector",
                "set_number": 1,
                "card_number": "137",
                "ink_color": "Sapphire",
                "rarity": "Rare"
            }
        ])
        self.assertEqual(actual, expected)

    def test_search_card_by_card_number(self):
        CARD_NUMBER = "1"
        actual = search_cards(self._cards, None, None, CARD_NUMBER, None, None)
        expected = json_to_card([
            {
                "id": 1,
                "name": "Ariel - On Human Legs",
                "set_number": 1,
                "card_number": "1",
                "ink_color": "Amber",
                "rarity": "Uncommon"
            },
            {
                "id": 217,
                "name": "Bashful - Hopeless Romantic",
                "set_number": 2,
                "card_number": "1",
                "ink_color": "Amber",
                "rarity": "Uncommon"
            },
            {
                "id": 433,
                "name": "Baloo - von Bruinwald XIII",
                "set_number": 3,
                "card_number": "1",
                "ink_color": "Amber",
                "rarity": "Rare"
            },
            {
                "id": 660,
                "name": "Agustin Madrigal - Clumsy Dad",
                "set_number": 4,
                "card_number": "1",
                "ink_color": "Amber",
                "rarity": "Common"
            },
            {
                "id": 885,
                "name": "Koda - Talkative Cub",
                "set_number": 5,
                "card_number": "1",
                "ink_color": "Amber",
                "rarity": "Rare"
            }
        ])
        self.assertEqual(actual, expected)

    def test_search_card_by_card_number_contains_letter(self):
        CARD_NUMBER = "4a"
        actual = search_cards(self._cards, None, None, CARD_NUMBER, None, None)
        expected = json_to_card([
            {
            "id": 436,
            "name": "Dalmatian Puppy - Tail Wagger",
            "set_number": 3,
            "card_number": "4a",
            "ink_color": "Amber",
            "rarity": "Common"
            }
        ])
        self.assertEqual(actual, expected)

    def test_search_cards_by_name_and_ink_color(self):
        CARD_NAME_SUBSTRING = "Ariel"
        INK_COLOR = InkColor.AMBER
        actual = search_cards(self._cards, CARD_NAME_SUBSTRING, None, None, INK_COLOR, None)
        expected = json_to_card([
            {
                "id": 1,
                "name": "Ariel - On Human Legs",
                "set_number": 1,
                "card_number": "1",
                "ink_color": "Amber",
                "rarity": "Uncommon"
            },
            {
                "id": 2,
                "name": "Ariel - Spectacular Singer",
                "set_number": 1,
                "card_number": "2",
                "ink_color": "Amber",
                "rarity": "Super Rare"
            },
            {
                "id": 662,
                "name": "Ariel - Singing Mermaid",
                "set_number": 4,
                "card_number": "3",
                "ink_color": "Amber",
                "rarity": "Rare"
            }
        ])
        self.assertEqual(actual, expected)

    def test_search_cards_by_name_and_rarity(self):
        CARD_NAME_SUBSTRING = "Ariel"
        RARITY = CardRarity.SUPER_RARE
        actual = search_cards(self._cards, CARD_NAME_SUBSTRING, None, None, None, RARITY)
        expected = json_to_card([
            {
                "id": 2,
                "name": "Ariel - Spectacular Singer",
                "set_number": 1,
                "card_number": "2",
                "ink_color": "Amber",
                "rarity": "Super Rare"
            },
            {
                "id": 539,
                "name": "Ariel - Adventurous Collector",
                "set_number": 3,
                "card_number": "103",
                "ink_color": "Ruby",
                "rarity": "Super Rare"
            },
            {
                "id": 798,
                "name": "Ariel - Treasure Collector",
                "set_number": 4,
                "card_number": "139",
                "ink_color": "Sapphire",
                "rarity": "Super Rare"
            },
            {
                "id": 834,
                "name": "Ariel - Sonic Warrior",
                "set_number": 4,
                "card_number": "175",
                "ink_color": "Steel",
                "rarity": "Super Rare"
            }
        ])
        self.assertEqual(actual, expected)

    def test_search_cards_ink_color_invalid_no_match(self):
        RARITY = "Invalid"
        actual = len(search_cards(self._cards, None, None, None, None, RARITY))
        expected = 0
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
