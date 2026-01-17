
import Utils
count = 0
# dictionary to boolean indicating if the pumpkin at position has grown

# intended to be used by paralell drones, hence only farm max value sunflowers, if sunflower is not then replant
def makeSquareManager(xmin,ymin,steps, #type List[int]
				   ):
	quick_print('init for', xmin, ymin, steps )
	def manageSquare():
		isGrown = {}
		xmax = xmin + steps
		ymax = ymin + steps
		Utils.move_to(xmin,ymin)
		bottem = -1
		top = 1
		while True:
			x = get_pos_x()
			y = get_pos_y()
			entity = get_entity_type()
			if entity != Entities.Pumpkin:
				if(get_ground_type() != Grounds.Soil):
					till()
				if entity != None:
					harvest()
				plant(Entities.Pumpkin)
				isGrown[x,y] = False
				isGrown[x,y] = False
			if x==xmin and y == ymin:
				bottem = measure()
			if x == xmax and y == ymax:
				top = measure()
			if bottem != -1 and bottem == top:
				harvest()
			Utils.move_next_tile(xmin,ymin,xmax,ymax)
	return manageSquare

# main
worldSize = get_world_size()
maxDrones = max_drones()
stepsPerDrone = ((worldSize**2 / maxDrones)**0.5)// 1
quick_print(maxDrones)
quick_print(worldSize)
quick_print(stepsPerDrone)
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