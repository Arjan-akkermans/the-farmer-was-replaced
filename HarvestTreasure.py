
import Utils

def startMaze():
	if(get_ground_type() != Grounds.Grassland):
		till()
	if get_entity_type() != Entities.Bush:
		harvest()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

# intended to be used by paralell drones, hence only farm max value sunflowers, if sunflower is not then replant
def makeMazeSolver(goRight):
	def solveMaze():
		directions = [North, East, South, West]
		# index indicating which direction currently the drone is moving
		index = 0
		while True:
			if get_entity_type() == Entities.Treasure:
				harvest()
				startMaze()
			else:
				if goRight:
					# assuming no loops, follow wall, e.g. keep right hand on the wall
					if move(directions[(index + 1) % 4]):
						index = (index + 1) % 4
					elif move(directions[index]):
						pass
					elif move(directions[(index + 3) % 4]):
						index = (index + 3) % 4
					elif move(directions[(index + 2) % 4]):
						index = (index + 2) % 4
					else:
						quick_print('no valid move in maze, should be unreachable')
				else:
					# assuming no loops, follow wall, e.g. keep right hand on the wall
					if move(directions[(index - 1) % 4]):
						index = (index - 1) % 4
					elif move(directions[index]):
						pass
					elif move(directions[(index - 3) % 4]):
						index = (index - 3) % 4
					elif move(directions[(index - 2) % 4]):
						index = (index - 2) % 4
					else:
						quick_print('no valid move in maze, should be unreachable')
	return solveMaze
clear()
# initialize paralize drones
# spawn them as spread out as possible? ( currently on diagonal ) then start and solve maze
Utils.move_to( 0,0 )
currentX = 0
currentY = 0
worldSize = get_world_size()  
squares = worldSize**2
maxDrones = max_drones()
stepCount = worldSize / maxDrones
goRight = True
for i in range(1,maxDrones ):
	task = makeMazeSolver(goRight)
	if not spawn_drone(task):
		task()
	goRight = not goRight
	currentX+=stepCount
	currentY+=stepCount
	Utils.move_to(currentX,currentY)
startMaze()
task = makeMazeSolver(goRight)
if not spawn_drone(task):
	task()