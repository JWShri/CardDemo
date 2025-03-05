class Hand:
    """A hand of playing cards"""
    
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        """Add a card to the hand"""
        if card:
            self.cards.append(card)
    
    def display(self):
        """Return a string representation of the hand"""
        return ', '.join(str(card) for card in self.cards) if self.cards else "Empty Hand"
    
    def card_count(self):
        """Return the number of cards in the hand"""
        return len(self.cards)
