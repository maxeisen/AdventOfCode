def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  CARDS = {'A','K','Q','J','T','9','8','7','6','5','4','3','2'}
  HANDS = {'5','14','23','113','122','1112','11111'}
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
    if handData[handID]:
      handData[handID].append({"hand":hand,"bet":int(bet)})
  print(handData)
  # handData = rankHands(handData)

# def rankHands(handData):
#   for hand in handData.keys():
#     if handData[hand]['type'] == '5OAK':
#       handData[hand]['rank'] == 1

# Either part 1 or 2 of the problem
PART = 1
print(main(PART))