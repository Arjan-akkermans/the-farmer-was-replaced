clear()
goNorth=True
import Utils
while True:
	if( can_harvest() ):
		harvest()
		plant(Entities.Grass)
	Utils.move_next_tile()


	
	
		