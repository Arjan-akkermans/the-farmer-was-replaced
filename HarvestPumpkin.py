
import Utils
count = 0
# dictionary to boolean indicating if the pumpkin at position has grown
isGrown = {}

def harvest_all():
	harvest()
	for i in range(get_world_size() * get_world_size()): 	
		plant(Entities.Pumpkin)
		isGrown[i,j] = False 
		Utils.move_next_tile()
WORLD_SIZE=get_world_size()

# initi data and all pumpkins
for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			Utils.move_to(i,j)
			entity = get_entity_type()
			if(  entity != Entities.Pumpkin):
				if(get_ground_type() != Grounds.Soil):
					till()
				if entity != None:
					harvest()
				plant(Entities.Pumpkin)
			isGrown[i,j] = False

while True:
	allGrown = True
	for i in range(WORLD_SIZE):
		for j in range(WORLD_SIZE):
			if isGrown[i,j]:
				continue
			allGrown = False
			Utils.move_to(i, j)
			entity = get_entity_type()
			if entity != Entities.Pumpkin:
				plant(Entities.Pumpkin )
			elif can_harvest():
				isGrown[i,j] = True
	if allGrown:
		harvest_all()


