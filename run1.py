selection = []
iterate = 0
times = 0
value = 0
gotIt = True

def countX(list, x):
  return list.count(x)

while gotIt:
  file = open("input1.txt")
  for x in file:
    if x[0] == '-':
      value -= int(x[1:])
    else:
      value += int(x[1:])
    selection.append(value)
  file.close()
    
  fuh = 0
  for x in selection: 
    iterate = countX(selection, selection[fuh])
	
    if iterate > 1:
      print("There are ", iterate, "of", selection[fuh])
      gotIt = False
    fuh += 1
	
  times += 1
  print(times, "through...")