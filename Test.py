import Utils
positions = [[1,1],[2,2],[6,6],[5,5],[2,5],[3,7]]
for p in positions:
	print( 'going to', p )
	Utils.move_to(p[0],p[1])