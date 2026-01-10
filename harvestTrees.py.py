clear()

import Utils
while True:
	# only plant on non-adjacent spaces (adajcent spaces give growth penalty)
	if ( get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0 ) or ( get_pos_x() % 2 == 1 and get_pos_y() % 2 == 1 ):
		if( can_harvest() ):
			harvest()
			plant(Entities.Tree)
			if get_water() < 0.2:
				use_item(Items.Water)  
	Utils.move_next_tile()


	
	
