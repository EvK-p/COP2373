import random

class Deck:
    def __init__(self):
        self.cards = [
            f"{rank} of {suit}"
            for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
            for rank in [
                "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
            ]
        ]
        random.shuffle(self.cards)
    
    def deal(self, num_cards):
        """Deal a specified number of cards."""
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards left in the deck")
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards
    
    def draw(self):
        """Draw a single card from the deck."""
        if not self.cards:
            raise ValueError("No cards left in the deck")
        return self.cards.pop()

def display_hand(hand):
    """Display the user's hand in a readable format."""
    return ', '.join([f"{i+1}: {card}" for i, card in enumerate(hand)])

def main():
    # Initialize the deck and deal a hand of five cards
    deck = Deck()
    hand = deck.deal(5)
    
    print("Your initial hand:")
    print(display_hand(hand))
    
    # Prompt user to enter cards to replace
    replace_indices = input(
        "Enter the numbers of the cards to replace (comma-separated), or press Enter to keep your hand: "
    )
    
    if replace_indices.strip():
        replace_indices = [int(x.strip()) - 1 for x in replace_indices.split(",")]
        if any(index < 0 or index >= len(hand) for index in replace_indices):
            print("Invalid selection. No cards were replaced.")
        else:
            for index in replace_indices:
                hand[index] = deck.draw()
    
    print("\nYour final hand:")
    print(display_hand(hand))

if __name__ == "__main__":
    main()
