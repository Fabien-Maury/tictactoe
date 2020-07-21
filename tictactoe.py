import sys

def turn(x):
	t=0
	while (['1','2','3','4','5','6','7','8','9'].count(t)==0 or slots[int(t)]!=' '):
		if slots[int(t)]!=' ' and t!=0:
			print('This place is already used, choose another one ')
		t=input('Player '+str(x)+", it's your turn : ")
	return(t,x)

def draw():
	extr1=' '+slots[7]+'|'+slots[8]+'|'+slots[9]+'  '
	inter='--|-|--'
	extr2=' '+slots[4]+'|'+slots[5]+'|'+slots[6]+'  '
	extr3=' '+slots[1]+'|'+slots[2]+'|'+slots[3]+'  '
	print(extr1+'\n'+inter+'\n'+extr2+'\n'+inter+'\n'+extr3)
	return()

def update(slots,p):
	s=None
	if p[1]==1:
		s='O'
	else:
		s='X'
	slots[int(p[0])]=s
	draw()
	return()

def checkwin():
	check=False
	total=0
	for slot in slots:
			if slot!=' ':
				total=total+1
	if (slots[7]==slots[8]==slots[9]!=' ') or (slots[4]==slots[5]==slots[6]!=' ') or (slots[1]==slots[2]==slots[3]!=' ') or (slots[7]==slots[4]==slots[1]!=' ') or (slots[8]==slots[5]==slots[2]!=' ') or (slots[9]==slots[6]==slots[3]!=' ') or (slots[7]==slots[5]==slots[3]!=' ') or (slots[1]==slots[5]==slots[9]!=' '):
		check=True
	elif total==9:
		check='draw'
	return(check)

input('TIC-TAC-TOE \nPress enter to start')
while True:
	
	slots=[None,' ',' ',' ',' ',' ',' ',' ',' ',' ']

	win=False
	draw()
	while win is False:
		p1=turn(1)
		update(slots,p1)
		win=checkwin()
		if win is True:
			print('Player 1 (O) wins ! ')
		elif win=='draw':
			print("It's a draw !")
		if win is False:
			p2=turn(2)
			update(slots,p2)
			win=checkwin()
			if win is True:
				print('Player 2 (X) wins ! ')
			elif win=='draw':
				print("It's a draw !")




	play=None
	while play!='y' and play!='n' and play!='N' and play!='Y':
		play=input('Play again (y/n) ? : ')
	if play=='y' or play=='Y':
		print('New game starting')
	elif play=='n' or play=='N':
		sys.exit()