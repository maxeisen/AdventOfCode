import time

def main(part):
  lines = open("input.txt", "r").readlines()
  INSTRUCTS, nodeKeys, nodeVals = lines[0].replace('\n',''), [line.replace('\n','').replace(' ','').split('=')[0] for line in lines[2:]], [line.replace('\n','').replace(' ','').replace('(','').replace(')','').split('=')[1].split(',') for line in lines[2:]]
  NODES = {}
  for i in range(len(nodeKeys)):
    NODES[nodeKeys[i]] = {'L':nodeVals[i][0],'R':nodeVals[i][1]}
  currentNode = 'AAA'
  numSteps = 0
  stepNum = 0

  if part == 1:
    while currentNode != 'ZZZ':
      if stepNum == len(INSTRUCTS):
        stepNum = 0
      step = INSTRUCTS[stepNum]
      currentNode = NODES[currentNode][step]
      stepNum+=1
      numSteps+=1

  if part == 2:
    try:
      visitedNodes = []
      currentNodes = [node for node in nodeKeys if node[-1] == 'A']
      zNodesReached = False
      idealNodeEnds = len(currentNodes)*['Z']
      while not zNodesReached:
        if stepNum == len(INSTRUCTS):
          stepNum = 0
        step = INSTRUCTS[stepNum]
        currentNodes = [NODES[node][step] for node in currentNodes]
        zNodesReached = [node[-1] for node in currentNodes] == idealNodeEnds
        # if currentNodes in visitedNodes:
        #   print(currentNodes)
        # else:
        #   visitedNodes.append(currentNodes)
        stepNum+=1
        numSteps+=1
    except KeyboardInterrupt:
      print(numSteps)

  return numSteps

# Either part 1 or 2 of the problem
PART = 2
print(main(PART))