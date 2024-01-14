# I made the boilerplate smaller starting on day 6... no more "if __name__" shit and now processing the file in one line

def main(part):
  lines = open("input.txt", "r").readlines()
  allPossibleWins = 0
  if part == 1:
    times, distances = [el for el in lines[0].replace('\n','').split(':')[1].split(' ') if el != ''], [el for el in lines[1].replace('\n','').split(':')[1].split(' ') if el != '']
    for raceNum in range(len(times)):
      time, distance, possibleWins = int(times[raceNum]), int(distances[raceNum]), 0
      for holdTime in range(time):
        if calculatePotentialDistance(holdTime, time) > distance:
          possibleWins += 1
      allPossibleWins = possibleWins * allPossibleWins if allPossibleWins > 0 else possibleWins
    return(allPossibleWins)

  # Could definitely be much more efficient
  if part == 2:
    time, distance = int(lines[0].replace('\n','').replace(' ','').split(':')[1]), int(lines[1].replace('\n','').replace(' ','').split(':')[1])
    allPossibleWins = 0
    for holdTime in range(time):
      if calculatePotentialDistance(holdTime, time) > distance:
        allPossibleWins += 1
    return(allPossibleWins)

def calculatePotentialDistance(holdTime, raceTime):
  return holdTime * (raceTime - holdTime)

# Either part 1 or 2 of the problem
PART = 2
print(main(PART))