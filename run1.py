selection = []
iterate = 0
times = 0
value = 0
gotIt = True

def countX(list, x):
  return list.count(x)

while gotIt:
  the_in = open("input1.txt", 'r')
  the_out = open("output.txt", 'a')
  for x in the_in:
    if x[0] == '-':
      value -= int(x[1:])
    else:
      value += int(x[1:])
    the_out.writelines("%s\n" % value)
    selection.append(value)
	
  the_in.close()
  the_out.close()
  #the_out = open("output.txt", 'r')
    
  for x in selection: 
    fuh = 0
    iterate = countX(selection, selection[fuh])
	
    if iterate > 1:
      print("There are ", iterate, "of", selection[fuh])
      gotIt = False
    fuh += 1
  
  #the_out.close()

  times += 1
  print(times, "through...")