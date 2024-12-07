import itertools

# check if expr evaluates to r
def expression_valid(r, expr):
  result = expr[0]
  expr = expr[1:]
  while len(expr) > 0:
    if expr[0] == '+':
      result = result + expr[1]
    else:
      result = result * expr[1]
    expr = expr[2:]

  return result == r

# read input_data from file
with open("../input.txt") as file:
  input_data = file.readlines()

# build set of all possible equations
equations = []
for line in input_data:
  left, right = line.split(': ')

  result = int(left)
  operands = list(map(int, right.split()))
  ops = ['+', '*']
  base_case = list(itertools.product(ops, ops))

  op_sets = None

  if len(operands) == 2:
    op_sets = [[x] for x in ops]
  elif len(operands) == 3:
    op_sets = [list(x) for x in base_case]
  else:
    for i in range(len(operands) - 3):
      if op_sets == None:
        op_sets = list(itertools.product(base_case, ops))
      else:
        op_sets = list(itertools.product(op_sets, ops))

      for i in range(len(op_sets)):
        if type(op_sets[i]) is tuple:
          op_sets[i] = [x for y in op_sets[i] for x in y]

  # assemble all possible sequences of operands and operators
  for op_set in op_sets:
    op_set.append('')
    expression = [combo[i] for i in range(len(op_set)) for combo in [operands, op_set]][:-1]
    equations.append([result, expression])

# collect list of unique results with valid expressions
valid_results = []
for result, expression in equations:
  if result not in valid_results:
    if expression_valid(result, expression):  # expression evaluates to result
      valid_results.append(result)            # add result to valid results list

print(sum(valid_results))