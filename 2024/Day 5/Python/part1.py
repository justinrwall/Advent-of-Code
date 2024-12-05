# check if order of a follows rules in ref
def check_order(a, ref):
  while len(a) > 0:
    x = a.pop(-1)  # remove last element

    # if any remaining values in a should come after x
    if len([y for y in a if y in ref[x]]) > 0:
      return False
  return True

# read input_data from file
rules = []
pagesets = []
switch = False
with open("../input.txt", "r") as file:
  for line in file.readlines():
    line = line.strip()
    if line == "":
      switch = True                     # line break in file
      continue
    if not switch:
      rules.append(line.split('|'))     # first section
    else:
      pagesets.append(line.split(','))  # second section

# create dictionary where k=page and v=list of pages that come after k
rule_tree = {}
for rule in rules:
  k, v = rule
  if k not in rule_tree.keys():
    rule_tree[k] = [v]
  else:
    rule_tree[k].append(v)
  if v not in rule_tree.keys():
    rule_tree[v] = []

total = 0
for pageset in pagesets:
  if check_order(pageset[:], rule_tree):      # if order is correct
    total += int(pageset[len(pageset) // 2])  # add middle page

print(total)