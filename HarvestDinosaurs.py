clear()
import Utils

# list storing where the snake is
WORLD_SIZE = get_world_size()

def can_move(direction, snake):
	x = snake[0][0]
	y = snake[0][1]
	if ( ( direction == North and y == WORLD_SIZE-1 )
		or ( direction == South and y == 0 )
		or ( direction == East and x == WORLD_SIZE - 1 ) 
		or ( direction == West and x == 0 ) ):
		return False


	if direction == North:
		y +=1
	elif direction == South:
		y-=1
	elif direction == East:
		x += 1
	elif direction == West:
		x -=1
	
	for s in snake:
		if s[0] == x and s[1] == y:
			return False
	return True
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
			return East
			
		else:
			# left column always move South
			return South
	if y == WORLD_SIZE-1:
		return West
	if x % 2 == 1: 
		direction = North
		end_y = WORLD_SIZE -2
		if( x == WORLD_SIZE -1 ):
			end_y +=1
	if y != end_y:
		return direction
	else:
		return East

#snake = [] ,# type = list[][]
def copySnakeAndRemoveTail(snake):
	snakeCopy = []
	for i in range(len(snake)-1):
		snakeCopy.append([snake[i][0],snake[i][1]])
	return snakeCopy

def copyPath(path):
	pathCopy = []
	for i in path:
		pathCopy.append(i)
	return pathCopy


# try to move in a direction, start from input index and try all possibilities
# returns TRUE if any move is made
def try_move_all_random(index):
	return not move( MOVE_OPTIONS[index % 4] ) and not move( MOVE_OPTIONS[(index + 1) % 4] ) and not move( MOVE_OPTIONS[(index +2) % 4] ) and not move( MOVE_OPTIONS[(index+3) % 4] )

# returns type [Boolean,snake,path] not sure how to enforce, if false snake and path are empty
def canReach(snake, path,targetX,targetY, depth = 0):
	currentX = snake[0][0]
	currentY = snake[0][1]
	if depth > WORLD_SIZE **2:
		return  [False,[],[]]
	canNorth = can_move(North,snake)
	canEast = can_move(East,snake)
	canSouth = can_move(South,snake)
	canWest = can_move(West,snake)
	# check if one step reaches apple, needs separate handling because then the snake should be increased in size
	if(canNorth and currentX == targetX and currentY+1 == targetY):
		return [True,[[currentX,currentY+1]]+snake,path+[North]]
	if(canEast and currentX+1 == targetX and currentY == targetY):
		return [True,[[currentX+1,currentY]]+snake,path+[East] ]
	if(canSouth and currentX == targetX and currentY-1 == targetY):
		return [True,[[currentX,currentY-1]]+snake,path + [South]]
	if(canWest and currentX-1 == targetX and currentY == targetY):
		return [True,[[currentX-1,currentY]]+snake,path+[West] ] 
	
	snakeNorth = [[currentX,currentY+1]] + copySnakeAndRemoveTail(snake) 
	pathNorth = copyPath(path) + [North]
	resultNorth = canNorth and canReach(snakeNorth,pathNorth,targetX,targetY,depth+1)
	if resultNorth != False and len(resultNorth) == 3 and resultNorth[0] == True:
		return resultNorth
	else:
		snakeEast = [[currentX+1,currentY]] + copySnakeAndRemoveTail(snake) 
		pathEast = copyPath(path) + [East]
		resultEast =  canEast and canReach(snakeEast,pathEast,targetX,targetY,depth+1)
		if resultEast != False and len(resultEast) == 3 and resultEast[0] == True:
			return resultEast
		else:
			snakeSouth = [[currentX,currentY-1]] + copySnakeAndRemoveTail(snake) 
			pathSouth = copyPath(path) + [South]
			resultSouth =  canSouth and canReach(snakeSouth,pathSouth,targetX,targetY,depth+1)
			if resultSouth != False and len(resultSouth) == 3 and resultSouth[0] == True:
				return resultSouth
			else:
				snakeWest = [[currentX-1,currentY]] + copySnakeAndRemoveTail(snake) 
				pathWest = copyPath(path) + [West]
				resultWest =  canWest and canReach(snakeWest,pathWest,targetX,targetY,depth+1)
				if resultWest != False and len(resultWest) == 3 and resultWest[0] == True:
					return resultWest
				else:
					return [False,[],[]]



# Code kinda works, but it kinda gets stuck in loops trying to find a path
# That can be partly worked around, by adding the counter to break
# Then it works ( slowly ) but issue is still that the snake gets stuck
# 
while True:
	change_hat(Hats.Sunflower_Hat)
	change_hat(Hats.Dinosaur_Hat)
	canMove=True
	snake = [[get_pos_x(),get_pos_y()]]
	while canMove:
		next_x,next_y = measure()
		count =0
		MOVE_OPTIONS = [North, South, East, West]
		result = canReach(snake,[],next_x,next_y)
		if(not result[0]):
			canMove = False
		else:
			snake = result[1]
			path = result[2]
			for i in range(len(path)):
				move(path[i])






# while True:
# 	# first do greedy go to neighbor, after a while switch to safe
# 	if count < 25:
# 		count +=1
# 		maxIterarions=25
# 		iterations=1
# 		# greedy, will not move properly when collision, so try a few time to traverse the shortest path
# 		while( (get_pos_x() != next_x or get_pos_y() != next_y) and iterations < maxIterarions):
# 				iterations+=1
# 				Utils.move_to_respect_boundries( next_x, next_y )
# 				if get_pos_x() != next_x or get_pos_y() != next_y:
# 					# couldnt reach apple, try random move
# 					randomIndex = random() * len(MOVE_OPTIONS) // 1
# 					try_move_all_random(randomIndex)
# 		if( iterations >= maxIterarions):
# 			quick_print('failed to reach apple, aborting prematurely ')
# 			change_hat(Hats.Sunflower_Hat)
# 			change_hat(Hats.Dinosaur_Hat)
# 			count = 0
# 		next_x,next_y = measure()
# 	direction = move_next_tile():
# 	if can_move(direction):
# 		move(direction)
# 		x = get_pos_x()
# 		y = get_pos_y()
# 		if isOnApple:
# 			next_x,next_y = measure()
		
# 	else:
# 		change_hat(Hats.Sunflower_Hat)
# 		change_hat(Hats.Dinosaur_Hat)
# 		count = 0
	
	
		