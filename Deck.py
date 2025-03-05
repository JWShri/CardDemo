class Deck:
    """A deck of playing cards"""
    
    def __init__(self):
        self.cards = self._generate_deck()
    
    def _generate_deck(self):
        """Generate a full deck of 52 playing cards"""
        return [PlayingCard(rank, suit) for suit in PlayingCard.SUITS for rank in PlayingCard.RANKS]
    
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
    
    def draw_card(self):
        """Draw a card from the deck. Returns None if the deck is empty."""
        return self.cards.pop() if self.cards else None
    
    def __str__(self):
        """Return a string representation of the deck"""
        return ', '.join(str(card) for card in self.cards)
