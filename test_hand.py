import unittest

from hand import Hand

class TestHand(unittest.TestCase):
    def setUp(self):
        self.hand = Hand()
        self.card1 = PlayingCard("A", "Spades")
        self.card2 = PlayingCard("10", "Hearts")
    
    def test_add_card(self):
        self.hand.add_card(self.card1)
        self.assertEqual(len(self.hand.cards), 1, "Hand should have 1 card after adding a card")
    
    def test_display(self):
        self.assertEqual(self.hand.display(), "Empty Hand", "New hand should be empty")
        self.hand.add_card(self.card1)
        self.hand.add_card(self.card2)
        self.assertEqual(self.hand.display(), "A of Spades, 10 of Hearts", "Display should show correct cards")
    
    def test_card_count(self):
        self.assertEqual(self.hand.card_count(), 0, "New hand should have 0 cards")
        self.hand.add_card(self.card1)
        self.assertEqual(self.hand.card_count(), 1, "Hand should have 1 card after adding a card")
        self.hand.add_card(self.card2)
        self.assertEqual(self.hand.card_count(), 2, "Hand should have 2 cards after adding another card")

if __name__ == "__main__":
    unittest.main()
