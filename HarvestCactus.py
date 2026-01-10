import Utils
# store cactus measurements indexed by (x,y)
WORLD_SIZE = get_world_size()
Cacti = {}

def plantAll():
	Utils.move_to(0,0)
	count = 0
	while count < get_world_size() * get_world_size():
		count += 1
		x = get_pos_x()
		y = get_pos_y()
		if get_ground_type() == Grounds.Grassland:
			till()
		if get_entity_type() != Entities.Cactus:
			plant(Entities.Cactus)
		Cacti[x, y] = measure()
		Utils.move_next_tile()

def getMaxValue(dict):
	maxValue = 0
	for key in dict:
		maxValue = max(maxValue, dict[key])
	return maxValue

# check if everything lower of the point is actually lower
def isSorted(x, y):
	is_sorted = True
	for i in range(x-1, -1, -1):
		if Cacti[(i, y)] > Cacti[(x, y)]:
			is_sorted = False

	for i in range(y-1, -1, -1):
		if Cacti[(x, i)] > Cacti[(x, y)]:
			is_sorted = False

	return is_sorted

# sorts the position at start of method call by moving it to the west and south if needed
def sort():
	x = get_pos_x()
	y = get_pos_y()
	for i in range(x-1, -1, -1):
		if Cacti[(i, y)] > Cacti[(x, y)]:
			# swap
			swap(West)
			move(West)
			temp = Cacti[(i, y)]
			Cacti[(i, y)] = Cacti[(x, y)]
			Cacti[(x, y)] = temp
			x -=1
		else:
			break


	# sort column next
	for j in range(y-1, -1, -1):
		if Cacti[(x, j)] > Cacti[(x, y)]:
			# swap
			swap(South)
			move(South)
			temp = Cacti[(x, j)]
			Cacti[(x, j)] = Cacti[(x, y)]
			Cacti[(x, y)] = temp
			y -=1
		else:
			break

# sufficient to check if aboundry entries (?)
def isFullySorted():
	for i in range(WORLD_SIZE):
		if not isSorted(WORLD_SIZE-1,i) or not isSorted(i,WORLD_SIZE-1):
			return False
	return True

# MAIN
plantAll()
while True:
	while not isFullySorted():
		# get first incorrect cactus and sort it first in its rows then in column ( greedily )
		for i in range(WORLD_SIZE):
			for j in range(WORLD_SIZE):
				if isSorted(i, j):
					continue
				else:
					Utils.move_to(i, j)
					sort()
					break
	harvest()
	plantAll()
