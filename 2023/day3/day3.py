import re

def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  partNumbers = []
  for lineNum in range(len(lines)):
    line = lines[lineNum]
    splitLine = line.split('.')
    for tokenNum in range(len(splitLine)):
      token = splitLine[tokenNum]
      tokenIndex = line.find(token)
      if any(char.isdigit() for char in token):
        if token.isnumeric():
          partNumbers.append(analyzeToken(token, splitLine, lines, lineNum, tokenIndex))
        else:
          partNumbers.append(int(re.sub("\D", "", token)))
  return(sum(partNumbers))
          
def analyzeToken(token, splitLine, lines, lineNum, tokenIndex):
  if lineNum > 0 and lineNum < len(lines)-1:
    adjChars = (lines[lineNum-1][tokenIndex-1:tokenIndex+len(token)+1]+lines[lineNum+1][tokenIndex-1:tokenIndex+len(token)+1])
  elif lineNum == 0:
    adjChars = (lines[lineNum+1][tokenIndex-1:tokenIndex+len(token)+1])
  elif lineNum == len(lines)-1:
    adjChars = (lines[lineNum-1][tokenIndex-1:tokenIndex+len(token)+1])
  if any((char != '.') for char in adjChars):
    return int(token)
  else:
    return 0
    

if __name__ == "__main__":
  # Either part 1 or 2 of the problem
  PART = 2
  print(main(PART))