import Utils
# store sunflower measurements indexed by (x,y)
# intended to be used by paralell drones, hence only farm max value sunflowers, if sunflower is not then replant
def makeRowsManager(y, #type List[int]
				   ):
	def manageRows():
		# function walks over all points one by one, only harvests sunflowers with max value
		worldSize = get_world_size()
		sunFlowers={}
		maxValue = 15
		while True:
			positionY = y[0]
			Utils.move_to(0,positionY)
			for i in y:
				for j in range(worldSize):
					if get_ground_type() != Grounds.Soil:
							till()
					if get_entity_type() != Entities.Sunflower:
						plant(Entities.Sunflower)
					if measure()==maxValue:
						if can_harvest():
							harvest()
					else:
						harvest()
						plant(Entities.Sunflower)
					if j == worldSize - 1:
						move(North)
					else:
						move(East)
	return manageRows


worldSize = get_world_size()
def getMaxValue( dict):
	maxValue = 0
	for key in dict:
		maxValue = max( maxValue, dict[key] )
	return maxValue
maxDrones = max_drones()
rowsPerDrone = worldSize / maxDrones
# initializes drones
Utils.move_to(0,0)
currentRow = 0
for i in range(maxDrones):
	Utils.move_to(0,currentRow)
	task = makeRowsManager(range(currentRow,currentRow+rowsPerDrone))
	if not spawn_drone(task):
		task()
	currentRow += rowsPerDrone

