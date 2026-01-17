import Utils
# store cactus measurements indexed by (x,y
def createRowsSorter(y, #type List[int]
					):
	def sortRows():
		# function walks over all points one by one, only harvests sunflowers with max value
		worldSize = get_world_size()
		swaps = 0
		swapsInIteration = 1
		while swapsInIteration > 0:
			swapsInIteration = 0
			positionY = y[0]

			Utils.move_to(0,positionY)
			for i in y:
				positionX = 0
				for j in range(worldSize):
					if get_ground_type() == Grounds.Grassland:
						till()
					if get_entity_type() != Entities.Cactus:
						if can_harvest():
							harvest()
						plant(Entities.Cactus)
					current = measure()
					south = measure(South)
					west = measure(West)
					# only needed to check two directions because another drone sorts the other directions
					# also no need to check sorting over boundries
					if(positionY != 0 and south != None and current != None and current < south):
						swap(South)
						swaps+=1
						swapsInIteration+=1
						current = south
					if( positionX != 0 and west != None and current != None and current < west):
						swap(West)
						swaps+=1
						swapsInIteration+=1
					if j == worldSize - 1:
						move(North)
						positionY += 1
					else:
						move(East)
						positionX += 1
			return swaps == 0
	return sortRows
WORLD_SIZE = get_world_size()
maxDrones = max_drones()
rowsPerDrone = WORLD_SIZE / maxDrones
otherDrones = {}
# initializes drones
Utils.move_to(0,0)
currentRow = 0
while True:
	rowsSorted = 0
# spawn other drones to sort
	for i in range(1,maxDrones):

		Utils.move_to(0,currentRow)
		otherDrones[i]=spawn_drone( createRowsSorter(range(currentRow,currentRow+rowsPerDrone)) )
		if otherDrones[i] == None:
			quick_print( 'just saved None FIRST for', i)
		currentRow += rowsPerDrone
	while rowsSorted < maxDrones:
	# sort own row
		a = createRowsSorter( range( 0, rowsPerDrone) )
		isSelfSorted = a()
		
		if isSelfSorted:
			rowsSorted = 1

		# check status of other drones, reschedule any that are finished, count amount of sorted rows
		for i in range(1,maxDrones):
			otherDrone = otherDrones[i]
			if has_finished(otherDrone):
				if wait_for(otherDrone):
					rowsSorted+=1
				otherDrones[i]=spawn_drone( createRowsSorter(range(i*rowsPerDrone,i*rowsPerDrone+rowsPerDrone)) )
				if otherDrones[i] == None:
					quick_print( 'just saved None for', i)
		# if sorted, wait for all other drones ( should be quick ) and restart
		if rowsSorted == maxDrones:
			for i in range(1,maxDrones):
				droneIndex = otherDrones[i]
				wait_for(droneIndex)
			harvest()









# # NOT PARALELL CODE
# import Utils
# # store cactus measurements indexed by (x,y)
# WORLD_SIZE = get_world_size()
# Cacti = {}
# def plantAll():
# 	Utils.move_to(0,0)
# 	count = 0
# 	while count < get_world_size() * get_world_size():
# 		count += 1
# 		x = get_pos_x()
# 		y = get_pos_y()
# 		if get_ground_type() == Grounds.Grassland:
# 			till()
# 		if get_entity_type() != Entities.Cactus:
# 			if can_harvest():
# 				harvest()
# 			plant(Entities.Cactus)
# 		Cacti[x, y] = measure()
# 		Utils.move_next_tile()

# def getMaxValue(dict):
# 	maxValue = 0
# 	for key in dict:
# 		maxValue = max(maxValue, dict[key])
# 	return maxValue

# # check if everything lower of the point is actually lower
# def isSorted(x, y):
# 	is_sorted = True
# 	for i in range(x-1, -1, -1):
# 		if Cacti[(i, y)] > Cacti[(x, y)]:
# 			is_sorted = False

# 	for i in range(y-1, -1, -1):
# 		if Cacti[(x, i)] > Cacti[(x, y)]:
# 			is_sorted = False

# 	return is_sorted

# # sorts the position at start of method call by moving it to the west and south if needed
# def sort():
# 	x = get_pos_x()
# 	y = get_pos_y()
# 	for i in range(x-1, -1, -1):
# 		if Cacti[(i, y)] > Cacti[(x, y)]:
# 			# swap
# 			swap(West)
# 			move(West)
# 			temp = Cacti[(i, y)]
# 			Cacti[(i, y)] = Cacti[(x, y)]
# 			Cacti[(x, y)] = temp
# 			x -=1
# 		else:
# 			break


# 	# sort column next
# 	for j in range(y-1, -1, -1):
# 		if Cacti[(x, j)] > Cacti[(x, y)]:
# 			# swap
# 			swap(South)
# 			move(South)
# 			temp = Cacti[(x, j)]
# 			Cacti[(x, j)] = Cacti[(x, y)]
# 			Cacti[(x, y)] = temp
# 			y -=1
# 		else:
# 			break

# # sufficient to check if aboundry entries (?)
# def isFullySorted():
# 	for i in range(WORLD_SIZE):
# 		if not isSorted(WORLD_SIZE-1,i) or not isSorted(i,WORLD_SIZE-1):
# 			return False
# 	return True

# # MAIN
# plantAll()
# while True:
# 	while not isFullySorted():
# 		# get first incorrect cactus and sort it first in its rows then in column ( greedily )
# 		for i in range(WORLD_SIZE):
# 			for j in range(WORLD_SIZE):
# 				if isSorted(i, j):
# 					continue
# 				else:
# 					Utils.move_to(i, j)
# 					sort()
# 					break
# 	harvest()
# 	plantAll()
