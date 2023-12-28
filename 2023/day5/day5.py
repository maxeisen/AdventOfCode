def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  seeds = [int(seed) for seed in lines[0].replace('\n','').split(':')[1].split(' ')[1:]]
  rawMaps = [el for el in ('\n').join(lines[1:])[1:].split('\n') if el != '']
  cleanMaps = {}
  for el in rawMaps:
    if el[0].isalpha():
      mapTitle = el.split(' ')[0]
      cleanMaps[mapTitle] = []
    else:
      vals = el.split(' ')
      cleanMaps[mapTitle].append({'dest':int(vals[0]),'source':int(vals[1]),'range':int(vals[2])})

  locations = set()

  if part == 1:
    for seed in seeds:
      locations.add(seedToLocation(seed, cleanMaps))
  if part == 2:
      seeds = [seeds[i:i+2] for i in range(0,len(seeds),2)]
      for pairNum in range(len(seeds)):
        pair = seeds[pairNum]
        seeds[pairNum] = [pair[0],pair[0]+pair[1]-1]
        pair = seeds[pairNum]
        minLocation = seedToLocation(pair[0], cleanMaps)
        for seed in range(pair[0],pair[1]): # Although this is so incredibly inefficient, it did get me the correct solution after a long, long run - TODO: make it more efficient
          newLocation = seedToLocation(seed, cleanMaps)
          if newLocation < minLocation:
            minLocation = newLocation
        locations.add(minLocation)

  return min(locations)

def seedToLocation(seed, cleanMaps):
  trackedVal = seed
  for mapTitle in cleanMaps.keys():
    foundInMap = False
    for map in cleanMaps[mapTitle]:
      dest, source, valRange = map.values()
      if trackedVal in range(source, source+valRange):
        foundInMap = True
        trackedVal = dest+(trackedVal-source)
      if foundInMap:
        break
  if mapTitle == 'humidity-to-location':
    return trackedVal

if __name__ == "__main__":
  # Either part 1 or 2 of the problem
  PART = 2
  print(main(PART))