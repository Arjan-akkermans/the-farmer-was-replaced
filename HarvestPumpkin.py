clear()
import Utils
count = 0
while count < get_world_size() * get_world_size():	
	count+=1
	till()
	plant(Entities.Pumpkin)
	Utils.move_next_tile()

def harvest_all():
	harvest()
	for i in range(get_world_size() * get_world_size()): 	
		plant(Entities.Pumpkin)
		Utils.move_next_tile()



grownPumpkins = 0
TOTAL_SQUARES = get_world_size() * get_world_size()
while True:
	for i in range( TOTAL_SQUARES): 
		if( can_harvest() ):
			grownPumpkins +=1
		else:
			plant(Entities.Pumpkin)
		Utils.move_next_tile()
	if grownPumpkins >= TOTAL_SQUARES:
		harvest_all()
	grownPumpkins = 0


