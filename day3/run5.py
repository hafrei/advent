# from # to @ 
# from @ to ,
# from , to :
# from : to x
# from x to end
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
  bluh = "bluh"
  return bluh

plan = []
fabric = [1000,1000]

with open('input.txt') as f:
  claims = f.read().splitlines()

for x in claims:
  plan.append(get_specs(x))

# 0   1       2       3       4
#elf, x axis, y axis, length, width
for idea in plan:
  owner = idea[0]
  print("idea[4] is {}, idea[5] is {}".format(idea[3],idea[4]))
  #if fabric[int(idea[4]),int(idea[5])]:
  #  owner = "X"
  #stake_claim(idea,owner)
