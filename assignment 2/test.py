## test  
# 3 * 3 grid :  board
grid = ['*','*','*','*','*','*','*','*','*']
# we have two players denoted as "X" and "O"

play=True 
count=0
# print the grid
print(grid[0:3])
print(grid[3:6])
print(grid[6:9])
print("\n")
# main loop for 9 times
while play:
	win=False
	
	# add the first player
	add_x=True
	# loop to add a player X
	while add_x:
		# at which position you would like to add the player 
		player_postion_x=int(input ("Enter position for player X: "))
		## add X player into the board 
		if grid[player_postion_x-1]!="X" and grid[player_postion_x-1]!="O":
			grid[player_postion_x-1]="X"
			add_x=False
			#to count the number of added players
			count=count+1				
		else: 
			print (str(player_postion_x) + " " + "position has been taken by Player " + grid[player_postion_x-1])
			
		if grid[0]=="X" and grid[1]=="X" and grid[2]=="X":
			print ("Player X win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		elif grid[3]=="X" and grid[4]=="X" and grid[5]=="X":
			print ("Player X win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		elif grid[6]=="X" and grid[7]=="X" and grid[7]=="X":
			print ("Player X win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		elif grid[0]=="X" and grid[3]=="X" and grid[6]=="X":
			print ("Player X win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		elif grid[1]=="X" and grid[4]=="X" and grid[7]=="X":
			print ("Player X win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		elif grid[2]=="X" and grid[5]=="X" and grid[8]=="X":
			print ("Player X win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		elif grid[0]=="X" and grid[4]=="X" and grid[8]=="X":
			print ("Player X win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		elif grid[2]=="X" and grid[4]=="X" and grid[6]=="X":
			print ("Player X win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		if count==9:			
			play=False			
			break
		print(grid[0:3])
		print(grid[3:6])
		print(grid[6:9])
	if win==True:
		print ("Game Over")
		break
	if play==False:
		print ("Game Over but no winner")
		break

	add_o=True

	## look to add a player O
	while add_o:
		# at which position you would like to add the player 
		player_postion_O=int(input ("Enter position for player O: "))
		## add O player into the board
		if grid[player_postion_O-1]!="X" and grid[player_postion_O-1]!="O":
			grid[player_postion_O-1]="O"
			add_o=False
			#to count the number of added players
			count=count+1				
		else:
			print (str(player_postion_O) + " " + "position has been taken by Player " + grid[player_postion_O-1])
		
		if grid[0]=="O" and grid[1]=="O" and grid[2]=="O":
			print ("Player O win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True
			break
		elif grid[3]=="O" and grid[4]=="O" and grid[5]=="O":
			print ("Player O win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		elif grid[6]=="O" and grid[7]=="O" and grid[7]=="O":
			print ("Player O win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")
			win=True			
			break
		elif grid[0]=="O" and grid[3]=="O" and grid[6]=="O":
			print ("Player O win")
			print ("-------------")
			print(grid[0:3])
			print(grid[3:6])
			print(grid[6:9])
			print ("-------------")			
			break
		elif grid[1]=="O" and grid[4]=="O" and grid[7]=="O":
 			print ("Player O win")
 			print ("-------------")
 			print(grid[0:3])
 			print(grid[3:6])
 			print(grid[6:9])
 			win=True			
 			break
		elif grid[2]=="O" and grid[5]=="O" and grid[8]=="O":
 			print ("Player O win")
 			print(grid[0:3])
 			print(grid[3:6])
 			print(grid[6:9])
 			print ("-------------")
 			win=True			
 			break
		elif grid[0]=="O" and grid[4]=="O" and grid[8]=="O":
 			print ("Player O win")
 			print ("-------------")
 			print(grid[0:3])
 			print(grid[3:6])
 			print(grid[6:9])
 			print ("-------------")
 			win=True			
 			break
		elif grid[2]=="O" and grid[4]=="O" and grid[6]=="O":
 			print ("Player O win")
 			print ("-------------")
 			print(grid[0:3])
 			print(grid[3:6])
 			print(grid[6:9])
 			print ("-------------")
 			win=True			
 			break
		if count==9:			
			play=False			
			break			
		print(grid[0:3])
		print(grid[3:6])
		print(grid[6:9])
	if win==True: 
		print ("Game Over")
		break
	if play==False:
		print ("Game Over but no winner")
		break
	