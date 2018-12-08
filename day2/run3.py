box_ids = []
has_two = 0
has_three = 0

def find_two(current_box):
  yeppers = 0
  for s in current_box:
    if current_box.count(s) == 2:
      yeppers = 1
  return yeppers

def find_three(current_box):
  fo_sure = 0
  for s in current_box:
    if current_box.count(s) == 3:
      fo_sure = 1
  return fo_sure

box_ids = open('input.txt', 'r').readlines()

for x in box_ids:
  has_two += find_two(x)
  has_three += find_three(x)
print("We have {} for two and {} for three".format(has_two, has_three))
print("That's {}!".format(has_three*has_two))