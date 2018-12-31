# elf: ?, x:y, top_left: top_right, bottom_left: bottom_right
def get_specs(deets):
  elf = deets[deets.find("#")+1 : deets.find("@")].strip()
  x_axis = deets[deets.find("@")+1 : deets.find(",")].strip()
  y_axis = deets[deets.find(",")+1 : deets.find(":")].strip()
  length = deets[deets.find(":")+1 : deets.find("x")].strip()
  width = deets[deets.find("x")+1:].strip()
  specs = [elf, x_axis, y_axis, length, width]
  return specs

def stake_claim(idea,owner):
  #if owner is not int:
  bluh = ''
  return bluh

plan = []
fabric = [['' for x in range(1000)] for y in range(1000)]

with open('input.txt') as f:
  claims = f.read().splitlines()

plan = [get_specs(x) for x in claims]

# 0   1       2       3       4
#elf, x axis, y axis, wide, tall
for idea in plan:
  owner = idea[0]
  stop_x = idea[1] + idea[3]
  stop_y = idea[2] + idea[4]
  #for x in range(idea[1],idea[i])
  print("idea[3] is {}, idea[4] is {}".format(idea[3],idea[4]))
  fabric[int(idea[3])][int(idea[4])] = owner
  #if fabric[int(idea[4]),int(idea[5])]:
  #  owner = "X"
  #stake_claim(idea,owner)
