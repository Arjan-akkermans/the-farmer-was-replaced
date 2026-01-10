clear()
import Utils
# store sunflower measurements indexed by (x,y)

sunFlowers = {}
count = 0
while count < get_world_size() * get_world_size():	
	count+=1
	x = get_pos_x()
	y = get_pos_y()

	till()
	plant(Entities.Sunflower)
	sunFlowers[x,y]=measure()
	Utils.move_next_tile()

TOTAL_SQUARES = get_world_size() * get_world_size()

def getMaxValue( dict):
	maxValue = 0
	for key in dict:
		maxValue = max( maxValue, dict[key] )
	return maxValue

while True:
	maxValue = getMaxValue( sunFlowers )
	
	for i in range( TOTAL_SQUARES): 
		x = get_pos_x()
		y = get_pos_y()

		if sunFlowers[x,y]==maxValue:
			harvest()
			plant(Entities.Sunflower)
			maxValue = getMaxValue( sunFlowers )
		Utils.move_next_tile()