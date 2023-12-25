import re

def main(part):
  f = open("input.txt", "r")
  lines = f.readlines()
  calVal = 0
  for line in lines:
    if part == 1:
      lineDigitized = re.sub("[^0-9]", "", line)
      lineVal = int(lineDigitized[0]+lineDigitized[-1])
    elif part == 2:    
      if ((line[0]+line[-2]).isnumeric()):
        lineVal = (line[0]) + (line[-2])
      else:
        lineDigitized = convertToDigits(line)
        lineVal = (lineDigitized[0]) + (lineDigitized[-1])
    calVal += int(lineVal)
  return calVal

def convertToDigits(line):
  wordDigitMap = {
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9'
  }
  digitizedLine = ""
  newLine = ""
  for char in line:
    if char.isnumeric():
      digitizedLine += char
    else:
      newLine += char
      for word in wordDigitMap:
        if word in newLine:
          digitizedLine += wordDigitMap[word]
          newLine = char
  return digitizedLine

if __name__ == "__main__":
  # Either part 1 or 2 of the problem
  PART = 2
  print(main(PART))