# plants and harvests greedily the plants with companion bonus

clear()
import Utils

# stores the plant which is the last encountered companion for another tile
companions = {}
count = 0

# store sunflower measurements indexed by (x,y)
# intended to be used by paralell drones, hence only farm max value sunflowers, if sunflower is not then replant
def makeSquareManager(xmin,ymin,steps, #type List[int]
				   ):
	def manageSquare():
		# function walks over all points one by one, only harvests sunflowers with max value
		xmax = xmin + steps
		ymax = ymin + steps
		companions = {}
		Utils.move_to(xmin,ymin)
		while True:
			x = get_pos_x()
			y = get_pos_y()
			if(x,y) not in companions:
				companions[x,y] = None
			if( can_harvest() ):
				harvest()
			if get_entity_type() == None or get_entity_type() == Entities.Grass:
				plantAndUpdateCompanion(companions[x,y], companions)
			Utils.move_next_tile(xmin,ymin,xmax,ymax)
	return manageSquare

def getRandomPlant():
	possibilities = [ Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]
	return possibilities[ random() * len(possibilities) // 1]

def plantAndUpdateCompanion( type = None, companions = {}):
	# get random plant 
	if type == None:
		type = Entities.Tree
		# type = getRandomPlant()
	# ensure soil
	if type == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()
	elif get_ground_type() != Grounds.Grassland:
		till()
	plant(type)
	companion = get_companion()
	if(companion != None):
		plant_type, (x, y) = companion
		companions[x,y]=plant_type

# main
worldSize = get_world_size()
maxDrones = max_drones()
stepsPerDrone = ((worldSize**2 / maxDrones)**0.5)// 1

# initializes drones
Utils.move_to(0,0)
ymin = 0
currentRow = 0
for _ in range(stepsPerDrone):
	xmin = 0
	Utils.move_to(0,ymin)
	for _ in range(stepsPerDrone):
		task = makeSquareManager(xmin,ymin,stepsPerDrone)
		if not spawn_drone(task):
			task()
		xmin += stepsPerDrone + 1
	ymin+=stepsPerDrone + 1





	