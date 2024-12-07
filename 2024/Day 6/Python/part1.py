# check if position is in bounds
def in_bounds(x, y, width, height):
  return x in range(width) and y in range(height)

# read input_data from file
with open("../input.txt", "r") as file:
  input_data = [list(line.strip()) for line in file.readlines()]

facility_map = input_data
facility_width = len(facility_map[0])
facility_height = len(facility_map)

# identify coordinates of obstacles and the guard
obstacles = []
guard_x = None
guard_y = None
for i in range(facility_height):
  for j in range(facility_width):
    if input_data[i][j] == "#":
      obstacles.append([i, j])
    if input_data[i][j] == "^":
      guard_x = j
      guard_y = i

# cycle of turn vectors
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
turn = 0

visited = [[guard_y, guard_x]]  # list of visited coordinates

current_x = guard_x
current_y = guard_y
while in_bounds(current_x, current_y, facility_width, facility_height):
  # next position based on direction vector cycle
  nextX = current_x + directions[turn % 4][1]
  nextY = current_y + directions[turn % 4][0]

  if in_bounds(nextX, nextY, facility_width, facility_height):
    if [nextY, nextX] in obstacles:
      turn = turn + 1  # turn right
    else:
      current_x = nextX  # move to next
      current_y = nextY
      if [current_y, current_x] not in visited:
        visited.append([current_y, current_x])  # record as visited
  else:
    break

print(len(visited))
