import math

def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  return calculateWinnings(lines, 0, 0)

  # Non-recursive approach! (boooorrrrrinnnnnggg)
  '''
  winnings = 0
  for line in lines:
    winningNums = [el for el in line.replace('\n','').split(':')[1].split('|')[0].split(' ') if el != '']
    myNums = [el for el in line.replace('\n','').split(':')[1].split('|')[1].split(' ') if el != '']
    cardWinnings = 2**(len([num for num in myNums if num in winningNums])-1)
    winnings += cardWinnings if cardWinnings >= 1 else 0
  return(winnings)
  '''

# Recursive, one-liner approach!
def calculateWinnings(lines, currLine, winnings):
  while currLine < len(lines):
    return(calculateWinnings(lines, currLine+1, winnings+math.floor(2**(len([num for num in [el for el in lines[currLine].replace('\n','').split(':')[1].split('|')[1].split(' ') if el != ''] if num in [el for el in lines[currLine].replace('\n','').split(':')[1].split('|')[0].split(' ') if el != '']])-1))))
  return winnings

if __name__ == "__main__":
  # Either part 1 or 2 of the problem
  PART = 1
  print(main(PART))