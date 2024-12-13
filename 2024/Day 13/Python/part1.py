import re

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = file.read().split('\n\n')

total = 0
for machine in input_data:
  a_button, b_button, prize = [line.strip() for line in machine.split('\n')]

  # extract numbers from data lines
  a = re.match(r"^Button A: X\+(?P<x>\d+), Y\+(?P<y>\d+)$", a_button)
  b = re.match(r"^Button B: X\+(?P<x>\d+), Y\+(?P<y>\d+)$", b_button)
  p = re.match(r"^Prize: X=(?P<x>\d+), Y=(?P<y>\d+)$", prize)

  # convert captured groups to integers
  a_x = int(a['x'])
  a_y = int(a['y'])
  b_x = int(b['x'])
  b_y = int(b['y'])
  p_x = int(p['x'])
  p_y = int(p['y'])

  n_a = 0              # number of a presses
  n_b = 0              # number of b presses
  min_tokens = 999999  # minimum cost

  # possible presses is 0-100 of each
  for i in range(101):
    for j in range(101):
      # if i and j solve the equations
      if a_x * i + b_x * j == p_x and a_y * i + b_y * j == p_y:
        tokens = 3 * i + j  # calculate cost

        # if this solution is cheaper, keep it
        if tokens < min_tokens:
          n_a = i
          n_b = j
          min_tokens = tokens

  # if valid solution exists, add minimum token requirement to total
  if min_tokens != 999999:
    total += min_tokens

print(total)