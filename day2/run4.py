box_ids = []
running = True

def compare_id(first_id, second_id, third_id):
  incor = [0,0]
  print("We have:\n{}\n{}\n{}".format(first_id,second_id,third_id))
  for windex, s in enumerate(first_id):
    print("{} has an index of {}".format(s,windex))
    print("{} has an index of {}".format(second_id[windex],windex))
    if s != second_id[windex]:
      incor[0] += 1
    if s != third_id[windex]:
      incor[1] += 1
  return incor

box_ids = open('input1.txt', 'r').readlines() 

sorted_box_ids = sorted(box_ids)

while running:
  for dindex, x in enumerate(sorted_box_ids):
    result = compare_id(x, sorted_box_ids[1 + dindex], sorted_box_ids[2 + dindex] )
    if result[0] == 1:
      print("We got {} and {}!".format(x,sorted_box_ids[dindex + 1]))
      running = False
    elif result[1] == 1:
      print("We got {} and {}!".format(x,sorted_box_ids[dindex + 2]))
      running = False