# Moves to a next file in the grid
# Will traverse all tiles in a zig-zag pattern

def move_next_tile(xmin = 0, ymin = 0,xmax = get_world_size()-1,ymax=get_world_size()-1): 
	direction = South
	end_y = ymin
	positionX = get_pos_x()
	positionY = get_pos_y()  
	if positionX % 2 == 0: 
		direction = North
		end_y = ymax
	if positionY != end_y:
		return move(direction)
	else:
		xTarget = positionX + 1
		if xTarget > xmax:
			xTarget = xmin
		move_to(xTarget,positionY)
		

		
def move_to(x, y):
	worldSize = get_world_size()
	if worldSize <= 1:
		return  # nothing to do

	currentX = get_pos_x()
	currentY = get_pos_y()

	# X axis (East/West, wrapping)
	if currentX != x:
		east_steps = (x - currentX) % worldSize
		west_steps = (currentX - x) % worldSize
		if east_steps <= west_steps:
			for _ in range(east_steps):
				move(East)
		else:
			for _ in range(west_steps):
				move(West)

	# Y axis (North/South, wrapping)
	if currentY != y:
		north_steps = (y - currentY) % worldSize
		south_steps = (currentY - y) % worldSize
		if north_steps <= south_steps:
			for _ in range(north_steps):
				move(North)
		else:
			for _ in range(south_steps):
				move(South)

def move_to_respect_boundries(x, y):
	worldSize = get_world_size()
	if worldSize <= 1:
		return  # nothing to do

	currentX = get_pos_x()
	currentY = get_pos_y()

	# X axis (East/West, wrapping)
	if currentX > x:
		for _ in range( currentX- x):
			move(West)
	else:
		for _ in range( x - currentX):
			move(East)
		# X axis (East/West, wrapping)
	if currentY > y:
		for _ in range( currentY- y):
			move(South)
	else:
		for _ in range( y - currentY):
			move(North)

def numberToCoordinates(number, size):
	x = number % size
	y = number // size
	return (x, y)

def coordinatesToNumber(x, y, size):
	return y * size + x
