# I abandoned this attempt when I realized it had gone awry and there was no saving it...
# Personally I think my method was cool, but keeping track of indices became too cumbersome...
# When I was in bed and thought of a way better method I decided to say f*** it and leave this one behind
# But I kept it to show that even a pro makes mistakes and has to go back to the drawing board once in a while
# ...
# Error: aforementioned 'pro' not found behind keyboard

import re

def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  partNumbers = []
  for lineNum in range(len(lines)):
    line = lines[lineNum]
    splitLine = line.split('.')
    print(splitLine)
    for tokenNum in range(len(splitLine)):
      token = splitLine[tokenNum]
      tokenIndex = line.find(token)
      if any(char.isdigit() for char in token):
        if token.isnumeric():
          partNumbers.append(analyzeToken(token, splitLine, lines, lineNum, tokenIndex))
        else:
          partNumbers.append(int(re.sub("\D", "", token)))
  return(partNumbers)
          
def analyzeToken(token, splitLine, lines, lineNum, tokenIndex):
  if lineNum > 0 and lineNum < len(lines)-1:
    adjChars = (lines[lineNum-1][tokenIndex-1:tokenIndex+len(token)+1]+lines[lineNum+1][tokenIndex-1:tokenIndex+len(token)+1])
    adjHalf = len(adjChars)//2
    # print(adjChars[:adjHalf])
    # print(' '+token+' ')
    # print(adjChars[adjHalf:])
  elif lineNum == 0:
    adjChars = (lines[lineNum+1][tokenIndex-1:tokenIndex+len(token)+1])
    # print(' '+token+' ')
    # print(adjChars)
  elif lineNum == len(lines)-1:
    adjChars = (lines[lineNum-1][tokenIndex-1:tokenIndex+len(token)+1])
    # print(adjChars)
    # print(' '+token+' ')
  print('\n')
  if any((char != '.') for char in adjChars):
    return int(token)
  else:
    return 0
    

if __name__ == "__main__":
  # Either part 1 or 2 of the problem
  PART = 1
  print(main(PART))