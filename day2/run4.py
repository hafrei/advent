from difflib import get_close_matches, Differ
box_ids = []

with open('input.txt') as f:
  box_ids = f.read().splitlines()

for x in box_ids:
  countem = get_close_matches(x,box_ids,cutoff=0.95)
  if len(countem) > 1:
    print(countem)