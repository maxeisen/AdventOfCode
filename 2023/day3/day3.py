def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  partNumbers = []
  partsAndPositions = []
  gearRatiosSum = 0
  for lineNum in range(len(lines)):
    line = lines[lineNum]
    charNum = 0
    while charNum <= len(line)-1:
      char = line[charNum]
      if char.isnumeric():
        numLength = 1 # We already know that the number is at least 1 digit long, so let's initialize to that
        currNum = char
        # Giving a buffer to ensure end of number is reached (if there were numbers >4 digits in length, this would break my whole solution and result in an infinite loop!)
        for digit in line[charNum+1:charNum+4]:
          if digit.isnumeric():
            currNum += digit
            numLength += 1
          else:
            if part == 1:
              partNumbers.append(analyzeNumber(currNum, charNum, numLength, line, lines, lineNum, part))
            elif part == 2:
              partNumber, position = analyzeNumber(currNum, charNum, numLength, line, lines, lineNum, part)
              if partNumber:
                partsAndPositions.append({'partNumber': partNumber, 'position': position})
            charNum += numLength
            break
      else:
        charNum += 1
  if part == 1:
    return(sum(partNumbers))
  if part == 2:
    gearRatioDictionary = {}
    for entry in partsAndPositions:
      if entry['position'] in gearRatioDictionary:
        gearRatiosSum += gearRatioDictionary[entry['position']]*entry['partNumber']
      else:
        gearRatioDictionary[entry['position']] = entry['partNumber']
    return(gearRatiosSum)

def analyzeNumber(currNum, charNum, numLength, line, lines, lineNum, part):
  # Handling [literal] edge case where number starts at zeroth index of line
  # Duplicates first digit for slicing purposes... doesn't affect value but does affect printed version of adjacent chars
  if charNum == 0:
    startNum = charNum
  else:
    startNum = charNum - 1

  aboveChars = []
  sameChars = line[startNum]+line[charNum+numLength]
  belowChars = []
  asteriskId = None
  adjChars = sameChars
  if lineNum == 0:
    belowChars = lines[lineNum+1][startNum:charNum+numLength+1]
    adjChars += belowChars
  elif lineNum == len(lines)-1:
    aboveChars = lines[lineNum-1][startNum:charNum+numLength+1]
    adjChars += aboveChars
  else:
    aboveChars = lines[lineNum-1][startNum:charNum+numLength+1]
    belowChars = lines[lineNum+1][startNum:charNum+numLength+1]
    adjChars += belowChars + aboveChars
  adjChars = adjChars.replace('\n','')
  if part == 1:
    if any((char != '.' and not char.isnumeric()) for char in adjChars):
      return int(currNum)
    else:
      return 0
  if part == 2:
    if '*' in adjChars:
      line = line.replace('\n','') # Removing all newline characters for part 2 as it messed with the asterisk ID'ing
      if sameChars.find('*') == 0:
        asteriskId = (lineNum*len(line))+(startNum)
      elif sameChars.find('*') == 1:
        asteriskId = (lineNum*len(line))+(charNum+numLength)
      elif '*' in aboveChars:
        asteriskId = ((lineNum-1)*len(line))+(startNum+aboveChars.find('*'))
      elif '*' in belowChars:
        asteriskId = ((lineNum+1)*len(line))+(startNum+belowChars.find('*'))
    if asteriskId:
      return (int(currNum), str(asteriskId))
    else:
      return (None, None)

if __name__ == "__main__":
  # Either part 1 or 2 of the problem
  PART = 2
  print(main(PART))