
# A dictionary to keep track of the count of each card
count = {'2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
         '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0,
         'Q': 0, 'K': 0, 'A': 0}

# A variable to keep track of the running count
RunningCount = 0

# A variable to keep track of the number of decks
decks = 1

# A function to update the count when a card is dealt
def count_cards(card, deck = 1):
    global RunningCount
    global decks
    if card in count:
        count[card] += 1
        if card in ['2','3','4','5','6']:
            RunningCount += 1
        elif card.upper() in ['10', 'J', 'Q', 'K', 'A']:
            RunningCount -= 1
    decks = deck

# A function to calculate the true count
def get_true_count():
    true_count = RunningCount / decks
    return true_count

# A function to retrieve the current count
def get_count():
    return count

def get_running_count():
    return RunningCount

# A function to determine the betting amount based on the true count
def get_bet(RunningCount):
    if RunningCount > 5:
        return 12
    elif RunningCount > 4:
        return RunningCount*2
    elif RunningCount >= 1:
        return RunningCount
    elif RunningCount < 0:
        return 1 # Change these values to change the bets as needed
    else:
        return "error"



def main(CardToCount,DeckValue):
    if isinstance (CardToCount,str) == True:
        CardToCount = CardToCount.upper()
    count_cards(CardToCount,DeckValue)
    print("Count: " +  str(get_count()))
    print("Running Count: " + str(get_running_count()))
    print("Bet: "+ str(get_bet(get_running_count())))

## Main ##
while True:
    main(input("Cards Value: "),1)
