selection = []
iterate = 0
times = 0
value = 0
gotIt = True

def countX(list, x):
  return list.count(x)

copy_file = open("input1.txt", 'r')
the_in = copy_file.readlines()
copy_file.close()

while gotIt:
  for x in the_in:
    if x[0] == '-':
      value -= int(x[1:])
    else:
      value += int(x[1:])
    selection.append(value)
    
  for x in selection: 
    fuh = 0
    iterate = countX(selection, selection[fuh])
	
    if iterate > 1:
      the_end = open("result.txt", 'a')
      the_end.writelines("There are {} of {} after {} times ".format(iterate, selection[fuh], times))
      the_end.close()
      print("There are {} of {} after {} times ".format(iterate, selection[fuh], times))
      gotIt = False
    fuh += 1

  times += 1
  print(times, "through...")