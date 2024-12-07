# check if position is in bounds
def in_bounds(x, y, map):
  if (x > -1 and x < len(map[0])) and (y > -1 and y < len(map)):
    return True
  return False

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = [list(line.strip()) for line in file.readlines()]

# identify coordinates of obstacles and the guard
obstacles = []
guardX = None
guardY = None
for i in range(len(input_data)):
  for j in range(len(input_data[0])):
    if input_data[i][j] == "#":
      obstacles.append([i, j])
    if input_data[i][j] == "^":
      guardX = j
      guardY = i

# cycle of turn vectors
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
turn = 0

visited = [[guardY, guardX]]  # list of visited coordinates

currentX = guardX
currentY = guardY
while in_bounds(currentX, currentY, input_data):
  # next position based on direction vector cycle
  nextX = currentX + directions[turn % 4][1]
  nextY = currentY + directions[turn % 4][0]

  if in_bounds(nextX, nextY, input_data):
    if [nextY, nextX] in obstacles:
      turn = turn + 1  # turn right
    else:
      currentX = nextX  # move to next
      currentY = nextY
      if [currentY, currentX] not in visited:
        visited.append([currentY, currentX])  # record as visited
  else:
    break

print(len(visited))
