clear()
import Utils
count = 0
while count < get_world_size() * get_world_size():	
	count+=1
	till()
	plant(Entities.Carrot)
	Utils.move_next_tile()

while True:
	for i in range(get_world_size()): 	
		if( can_harvest() ):
			harvest()
			plant(Entities.Carrot)
	Utils.move_next_tile()