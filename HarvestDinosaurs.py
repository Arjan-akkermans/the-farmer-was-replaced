clear()
import Utils

def move_next_tile():
	# top row and left column are left open to return, otherwise we do same zig-zag
	WORLD_SIZE = get_world_size() 
	direction = South
	end_y = 0

	x = get_pos_x()
	y = get_pos_y()

	if x == 0:
		if y == 0:
			# at (0,0) always move East
			return move( East )
			
		else:
			# left column always move South
			return move( South )
	if y == WORLD_SIZE-1:
		return move ( West )
	if x % 2 == 1: 
		direction = North
		end_y = WORLD_SIZE -2
		if( x == WORLD_SIZE -1 ):
			end_y +=1
	if y != end_y:
		return move(direction)
	else:
		return move( East )
		

# try to move in a direction, start from input index and try all possibilities
# returns TRUE if any move is made
def try_move_all_random(index):
	return not move( MOVE_OPTIONS[index % 4] ) and not move( MOVE_OPTIONS[(index + 1) % 4] ) and not move( MOVE_OPTIONS[(index +2) % 4] ) and not move( MOVE_OPTIONS[(index+3) % 4] )


change_hat(Hats.Sunflower_Hat)
change_hat(Hats.Dinosaur_Hat)
next_x,next_y = measure()
count =0
MOVE_OPTIONS = [North, South, East, West]


while True:
	# first do greedy go to neighbor, after a while switch to safe
	if( count < 25 ):
		count +=1
		maxIterarions=25
		iterations=1
		# greedy, will not move properly when collision, so try a few time to traverse the shortest path
		while( (get_pos_x() != next_x or get_pos_y() != next_y) and iterations < maxIterarions):
				iterations+=1
				Utils.move_to_respect_boundries( next_x, next_y )
				if get_pos_x() != next_x or get_pos_y() != next_y:
					# couldnt reach apple, try random move
					randomIndex = random() * len(MOVE_OPTIONS) // 1
					try_move_all_random(randomIndex)
		if( iterations >= maxIterarions):
			quick_print('failed to reach apple, aborting prematurely ')
			change_hat(Hats.Sunflower_Hat)
			change_hat(Hats.Dinosaur_Hat)
			count = 0
		next_x,next_y = measure()
	elif not move_next_tile():
		change_hat(Hats.Sunflower_Hat)
		change_hat(Hats.Dinosaur_Hat)
		count = 0
	
	
		