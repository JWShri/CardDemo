import unittest
class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    
    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52, "Deck should contain 52 cards initially")
    
    def test_shuffle(self):
        original_order = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards, "Deck should be shuffled")
    
    def test_draw_card(self):
        card = self.deck.draw_card()
        self.assertIsInstance(card, PlayingCard, "Drawn card should be an instance of PlayingCard")
        self.assertEqual(len(self.deck.cards), 51, "Deck should have 51 cards after drawing one")
    
    def test_draw_card_empty_deck(self):
        for _ in range(52):
            self.deck.draw_card()
        self.assertIsNone(self.deck.draw_card(), "Drawing from an empty deck should return None")

if __name__ == "__main__":
    unittest.main()
