import random

class Game:
	def __init__(self):
		self.board = 	[[4, 2, 3, 1],
						[123, 23, 41, 1443],
						[32, 4, 0, 2222],
						[44, 323, 124325, 12]]
		self.score = 0

	def getColumnAsList(self, idx):
		result = [self.board[x][idx] for x in range(len(self.board))]
		return result

	def setListAsColumn(self, list, idx):
		if len(list) > len(self.board):
			print("ERROR: wrong list length")
			return
		for x in range(len(list)):
			self.board[x][idx] = list[x]

	def move(self, direction):
		xComponent, yComponent = direction
		if xComponent != 0:
			for row in self.board:
				combineRow(row, xComponent)
				moveRow(row, xComponent)
		elif yComponent != 0:
			for x in range(len(self.board)):
				temp = self.getColumnAsList(x)
				combineRow(temp, yComponent)
				moveRow(temp, yComponent)
				self.setListAsColumn(temp, x)
	
	def spawnNewSquare(self):
		validLocations = []
		for i, row in enumerate(self.board):
			for j, cell in enumerate(row):
				if cell == 0:
					validLocations.append((i, j))

		print(validLocations)
		locationx, locationy = random.choice(validLocations)
		self.board[locationx][locationy] = 2 if random.randint(0,9) >= 1 else 4

	def validMoveExists(self):
		for i, row in enumerate(self.board):
			for j, cell in enumerate(row):
				if cell == 0 or \
				(j-1 > 0 and row[j-1] == cell) or \
				(j+1 < len(row) and row[j+1] == cell) or \
				(i-1 > 0 and self.board[i-1][j] == cell) or \
				(i+1 > len(self.board) and self.board[i+1][j] == cell):
					return True
		return False
				
	def __repr__(self):
		s = ""
		for line in self.board:
			s += str(line) + "\n"
		return s

def main():
	game = Game()
	while game.validMoveExists():
		direction = input("Choose WASD")
		if direction == "w":
			game.move((0,-1))
		if direction == "a":
			game.move((-1,0))
		if direction == "s":
			game.move((0,1))
		if direction == "d":
			game.move((1,0))
		game.spawnNewSquare()
		print(game)

def combineRow(row, dir):
	if dir > 0:
		steps = range(len(row)-1, -1, -1)
	else: 
		steps = range(len(row))
	for cellidx in steps:
		if row[cellidx] != 0:
			j = cellidx + dir
			while j < len(row)-1 and j > 0 and row[j] == 0:
				j += dir
			if j < len(row) and j >= 0 and row[cellidx] == row[j]:
				row[cellidx] = 0
				row[j] *= 2

def moveRow(row, dir):
	if dir > 0:
		steps = range(len(row)-1, -1, -1)
	else: 
		steps = range(len(row))
	for idx in steps:
		j = idx
		while (j + dir) >= 0 and (j + dir) < len(row) and row[j] != 0 and row[j + dir] == 0:
			temp = row[j]
			row[j] = row[j+dir]
			row[j+dir] = temp
			j += dir


if __name__ == '__main__':
	main()