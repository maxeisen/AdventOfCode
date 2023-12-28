import math

def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  
  if part == 1:
    return calculateWinnings(lines, 0)

    # Non-recursive approach for part 1! (boooorrrrrinnnnnggg)
    '''
    winnings = 0
    for line in lines:
      winningNums = [el for el in line.replace('\n','').split(':')[1].split('|')[0].split(' ') if el != '']
      myNums = [el for el in line.replace('\n','').split(':')[1].split('|')[1].split(' ') if el != '']
      cardWinnings = 2**(len([num for num in myNums if num in winningNums])-1)
      winnings += cardWinnings if cardWinnings >= 1 else 0
    return(winnings)
    '''
    
  # I won't lie... I compacted this one a lot too
  # but it should still be somewhat readable/unpackable
  if part == 2:
    cardCopies = {i:1 for i in range(1,len(lines)+1)}
    for line in lines:
      cardNum = int(''.join([el for el in line.replace('\n','').split(':')[0] if el.isnumeric()]))
      numMatches = len([num for num in [el for el in line.replace('\n','').split(':')[1].split('|')[1].split(' ') if el != ''] if num in [el for el in line.replace('\n','').split(':')[1].split('|')[0].split(' ') if el != '']])
      for num in range(cardNum+1, cardNum+1+numMatches):
        cardCopies[num] += 1*cardCopies[cardNum]
    return sum(cardCopies.values())

# Recursive, one-liner approach for part 1!
def calculateWinnings(lines, winnings):
  if len(lines) == 0:
    return winnings
  return(calculateWinnings(lines[1:], winnings+math.floor(2**(len([num for num in [el for el in lines[0].replace('\n','').split(':')[1].split('|')[1].split(' ') if el != ''] if num in [el for el in lines[0].replace('\n','').split(':')[1].split('|')[0].split(' ') if el != '']])-1))))

if __name__ == "__main__":
  # Either part 1 or 2 of the problem
  PART = 1
  print(main(PART))