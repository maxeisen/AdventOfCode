def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  gameData = {}
  possibleGames = 0
  if part == 1:
    for line in lines:
      possibleLine,gameId,lineData = preprocessLine(line, part)
      if possibleLine:
        possibleGames += int(gameId)
      gameData[gameId] = lineData
    return possibleGames
  elif part == 2:
    powerSum = 0
    for line in lines:
      lineData = preprocessLine(line, part)
      gamePower = lineData[0]
      for val in lineData[1:3]:
        gamePower *= val
      powerSum += gamePower
    return powerSum

def preprocessLine(line, part):
  splitLine = line.split(" ")
  MAX_VALS = {"red":12,"green":13,"blue":14}
  possibleLine = True
  if part == 1:
    lineData = {}
    for colour in MAX_VALS.keys():
      lineData[colour] = [int(splitLine[i-1]) for i, element in enumerate(splitLine) if colour in element]
      for val in lineData[colour]:
        if val > MAX_VALS[colour]:
          possibleLine = False
    return (possibleLine, splitLine[1].replace(':',''), lineData)
  elif part == 2:
    lineData = []
    for colour in MAX_VALS.keys():
      lineData.append(max([int(splitLine[i-1]) for i, element in enumerate(splitLine) if colour in element]))
    return lineData
  
if __name__ == "__main__":
  # Either part 1 or 2 of the problem
  PART = 2
  print(main(PART))