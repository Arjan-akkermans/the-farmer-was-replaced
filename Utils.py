# Moves to a next file in the grid
# Will traverse all tiles in a zig-zag pattern

def move_next_tile():
	WORLD_SIZE = get_world_size() 
	direction = South
	end_y = 0
	if get_pos_x() % 2 == 0: 
		direction = North
		end_y = WORLD_SIZE -1
	if get_pos_y() != end_y:
		move(direction)
	else:
		move( East )
		
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
	currentY = get_pos_y()  # refresh after X moves
	if currentY != y:
		north_steps = (y - currentY) % worldSize
		south_steps = (currentY - y) % worldSize
		if north_steps <= south_steps:
			for _ in range(north_steps):
				move(North)
		else:
			for _ in range(south_steps):
				move(South)