from difflib import SequenceMatcher

def compare_map(first_id, second_id):
  return SequenceMatcher(None,first_id,second_id).ratio()

bunch = [ "abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

print(bunch)
print(sorted(bunch))