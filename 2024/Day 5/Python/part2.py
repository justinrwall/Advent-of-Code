# check if order of a follows rules in ref
def check_order(a, ref):
  while len(a) > 0:
    x = a.pop(-1)  # remove last element

    # if any remaining values in a should come after x
    if len([y for y in a if y in ref[x]]) > 0:
      return False
  return True

# rearrange order of a according to rules in ref
def correct_order(a, ref, result):
  x = a[-1]                          # last element in a
  y = [n for n in a if n in ref[x]]  # elements in a that should be after x

  # case 1 - at least one element in a should be after x but isn't
  for z in y:
    a.remove(z)
    a.append(z)

  # case 2 - no elements in a should be after x - shrink problem size
  if y == []:
    a.remove(x)
    result.insert(0, x)

  while len(a) > 0:
    correct_order(a, ref, result)

  return result

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
rule_dict = {}
for rule in rules:
  k, v = rule
  if k not in rule_dict.keys():
    rule_dict[k] = [v]
  else:
    rule_dict[k].append(v)
  if v not in rule_dict.keys():
    rule_dict[v] = []

total = 0
for pageset in pagesets:
  if not check_order(pageset[:], rule_dict):            # if order is incorrect
    pageset = correct_order(pageset[:], rule_dict, [])  # correct the order
    total += int(pageset[len(pageset) // 2])            # add middle page

print(total)