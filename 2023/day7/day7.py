CARDS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
HANDS = ['5','14','23','113','122','1112','11111']

def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  handData = {}
  for line in lines:
    hand, bet = line.replace('\n','').split(' ')
    cardsInHand = {}
    for card in hand:
      if card in cardsInHand.keys():
        cardsInHand[card] += 1
      else:
        cardsInHand[card] = 1
    cardsInHand = list(cardsInHand.values())
    cardsInHand.sort()
    cardsInHand = [str(i) for i in cardsInHand]
    handID = ('').join(cardsInHand)
    if handID in handData.keys():
      handData[handID].append({"hand":hand,"bet":int(bet)})
    else:
      handData[handID] = [{"hand":hand,"bet":int(bet)}]
  totalWinnings = 0
  sortedHands = []
  for handType in HANDS:
    if handType in handData.keys():
      sortedHands += (sorted(handData[handType], key=placeHand, reverse=True))
  print(sortedHands)
  for rank in range(len(sortedHands),0,-1):
    hand = sortedHands[len(sortedHands)-rank]
    bet = hand['bet']
    print(hand, rank*bet)
    totalWinnings += rank*bet
  return totalWinnings


def placeHand(hand):
  # TODO: Implement hand scoring function to allow hands to be sorted
  return []

# Either part 1 or 2 of the problem
PART = 1
print(main(PART))