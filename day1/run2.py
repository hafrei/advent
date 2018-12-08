selection = []
times = 0
value = 0
gotIt = True

def countX(list, x):
  return list.count(x)

def ending(value, times):
  the_end = open("result.txt", 'a')
  the_end.writelines("There are two of {} after {} times ".format(value, times))
  the_end.close()
  print("There are two of {} after {} times ".format(value, times))

copy_file = open("input1.txt", 'r')
the_in = copy_file.readlines()
copy_file.close()

while gotIt:
  for x in the_in:
    if x[0] == '-':
      value -= int(x[1:])
    else:
      value += int(x[1:])
    if value in selection:
      ending(value, times)
      gotIt = False
    selection.append(value)

  times += 1
  print(times, "through...")