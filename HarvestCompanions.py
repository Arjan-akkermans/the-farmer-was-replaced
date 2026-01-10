# plants and harvests greedily the plants with companion bonus

clear()
import Utils

# stores the plant which is the last encountered companion for another tile
companions = {}
count = 0

def getRandomPlant():
	possibilities = [ Entities.Grass, Entities.Bush, Entities.Tree, Entities.Carrot]
	return possibilities[ random() * len(possibilities) // 1]

def plantAndUpdateCompanion( type = None):
	# get random plant 
	if type == None:
		type = getRandomPlant()
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

while True:
	x = get_pos_x()
	y = get_pos_y()
	if(x,y) not in companions:
		companions[x,y] = None
	if( can_harvest() ):
		harvest()
	if get_entity_type() == None or get_entity_type() == Entities.Grass:
		plantAndUpdateCompanion(companions[x,y])
	Utils.move_next_tile()






	