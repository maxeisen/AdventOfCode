import math

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
    currentNodes = [node for node in nodeKeys if node[-1] == 'A']
    allNumSteps = []
    for node in currentNodes:
      currentNode = node
      while currentNode[-1] != 'Z':
        if stepNum == len(INSTRUCTS):
          stepNum = 0
        step = INSTRUCTS[stepNum]
        currentNode = NODES[currentNode][step]
        stepNum+=1
        numSteps+=1
      allNumSteps.append(numSteps)
      numSteps = 0

    return math.lcm(*allNumSteps)

  return numSteps

# Either part 1 or 2 of the problem
PART = 1
print(main(PART))