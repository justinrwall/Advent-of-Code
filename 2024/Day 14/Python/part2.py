from re import findall
from PIL import Image

# build group starting at (i, j)
def get_group(grid, i, j, value):
  group = [(i, j)]

  # if cell outside grid bounds
  if i not in range(len(grid)):
    return []
  if j not in range(len(grid[0])):
    return []

  # if cell value not right
  if grid[i][j] != value:
    return []

  # if cell already in a group
  if visited[i][j]:
    return []

  visited[i][j] = True  # exclude cell from future groups

  group = group + get_group(grid, i + 1, j, value)  # cell below
  group = group + get_group(grid, i, j + 1, value)  # cell to right
  group = group + get_group(grid, i - 1, j, value)  # cell above
  group = group + get_group(grid, i, j - 1, value)  # cell to left

  return group

# convert map to image
def print_map(m):
  width = len(m[0])
  height = len(m)
  image = Image.new("1", (width, height))

  for x in range(width):
    for y in range(height):
      if m[y][x] == 0:
        image.putpixel((x, y), 0)
      else:
        image.putpixel((x, y), 1)

  image.save("tree.bmp")

# read input data from file
with open("../input.txt", "r") as file:
  robots = file.readlines()
robots = [list(map(int, findall(r"-?\d+", robot))) for robot in robots]

width = 101
height = 103
x_mid = width // 2
y_mid = height // 2

facility = [[0 for x in range(width)] for y in range(height)]

for robot in robots:
  p_x, p_y, v_x, v_y = robot
  facility[p_y][p_x] += 1

i = 1
while True:
  for j in range(len(robots)):
    p_x, p_y, v_x, v_y = robots[j]

    # remove current robot position
    facility[p_y][p_x] -= 1

    # calculate new robot position
    p_x = (p_x + v_x) % width
    p_y = (p_y + v_y) % height

    # update robot position
    robots[j] = [p_x, p_y, v_x, v_y]

    # record new robot position
    facility[p_y][p_x] += 1

  # all cells unvisited at start
  visited = [[False for j in range(width)] for i in range(height)]

  # build list of groups
  grid = [['#' if x != 0 else ' ' for x in row] for row in facility]
  groups = []
  for m in range(height):
    for n in range(width):
      if not visited[m][n] and grid[m][n] == '#':  # start of new group
        groups.append(get_group(grid, m, n, '#'))

  # if any group of size 100 or more exists, probably found the tree
  group_sizes = [len(group) for group in groups]
  if max(group_sizes) > 100:
    break

  i += 1

# create tree image file
print_map(facility)
print(i)  # print iteration count until tree