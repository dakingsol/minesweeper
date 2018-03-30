import pygame
from pygame.locals import *
import random

pygame.init()
gameDisplay = pygame.display.set_mode((700,600))
pygame.display.set_caption("Minesweeper: An Oliver and Solomon Production")
begin = [True, "placeholder"]
weRolling = True


def initialHandler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
			pygame.quit()
			quit()
		if event.type == KEYDOWN and event.key == K_1:
			pygame.display.set_caption("Minesweeper: An Oliver and Solomon Production (Easy)")
			return [False, 1]
		elif event.type == KEYDOWN and event.key == K_2:
			pygame.display.set_caption("Minesweeper: An Oliver and Solomon Production (Medium)")
			return [False, 2]
		elif event.type == KEYDOWN and event.key == K_3:
			pygame.display.set_caption("Minesweeper: An Oliver and Solomon Production (Hard)")
			return [False, 3]
	return [True, "placeholder"]

def makeDisplay(level):
	if level == 1:
		dimension = 8
		mines = 10
	elif level == 2:
		dimension = 16
		mines = 40
	elif level == 3:
		dimension = 24
		mines = 99
	#varArray will make array of all potential coordinates
	varArray = []
	#array will make array to see what exists at each point, first is columns, second list is down column
	array = []
	#
	for i in range(dimension):
		#placeholder array to populate array with arrays of length 10
		small = []
		for j in range(dimension):
			varArray.append([i,j])
			small.append([])
		array.append(small)
	#mineArray takes mine# of unique random points (from all coords) to see where mines should go
	mineArray = random.sample(varArray, mines)
	for i in range(len(mineArray)):
		a = mineArray[i][0]
		b = mineArray[i][1]
		array[a][b] = "mine"
	#top left corner
	count = 0
	if array[0][0] != "mine":
		if array[0][1] == "mine":
			count += 1
		if array[1][0]  == "mine":
			count += 1
		if array[1][1] == "mine":
			count += 1
		array[0][0] = count
		count = 0
	#top right corner
	if array[dimension-1][0] != "mine":
		if array[dimension-2][0] == "mine":
			count += 1
		if array[dimension-1][1] == "mine":
			count += 1
		if array[dimension-2][1] == "mine":
			count += 1
		array[dimension-1][0] = count
		count = 0
	#bottom left corner
	if array[0][dimension-1] != "mine":
		if array[0][dimension-2] == "mine":
			count += 1
		if array[1][dimension-1] == "mine":
			count += 1
		if array[1][dimension-2] == "mine":
			count += 1
		array[0][dimension-1] == count
		count = 0
	#bottom right corner
	if array[dimension-1][dimension-1] != "mine":
		if array[dimension-1][dimension-2] == "mine":
			count += 1
		if array[dimension-2][dimension-1] == "mine":
			count += 1
		if array[dimension-2][dimension-2] == "mine":
			count += 1
		array[dimension-1][dimension-1] = count
		count = 0
	#edges
	for i in range(1, dimension-1):
		#top row
		if array[i][0] != "mine":
			if array[i-1][0] == "mine":
				count += 1
			if array[i+1][0] == "mine":
				count += 1
			if array[i-1][1] == "mine":
				count += 1
			if array[i][1] == "mine":
				count += 1
			if array[i+1][1] == "mine":
				count += 1
			array[i][0] = count
			count = 0
		#bottom row
		if array[i][dimension-1] != "mine":
			if array[i-1][dimension-1] == "mine":
				count += 1
			if array[i+1][dimension-1] == "mine":
				count += 1
			if array[i-1][dimension-2] == "mine":
				count += 1
			if array[i][dimension-2] == "mine":
				count += 1
			if array[i+1][dimension-2] == "mine":
				count += 1
			array[i][dimension-1] = count
			count = 0
		#left column
		if array[0][i] != "mine":
			if array[0][i-1] == "mine":
				count += 1
			if array[0][i+1] == "mine":
				count += 1
			if array[1][i-1] == "mine":
				count += 1
			if array[1][i] == "mine":
				count += 1
			if array[1][i+1] == "mine":
				count += 1
			array[0][i] = count
			count = 0
		#right column
		if array[dimension-1][i] != "mine":
			if array[dimension-1][i-1] == "mine":
				count += 1
			if array[dimension-1][i+1] == "mine":
				count += 1
			if array[dimension-2][i-1] == "mine":
				count += 1
			if array[dimension-2][i] == "mine":
				count += 1
			if array[dimension-2][i+1] == "mine":
				count += 1
			array[dimension-1][i] = count
			count = 0
	#the whole middle
	for i in range (1, dimension-1):
		for j in range(1, dimension-1):
			if array[i][j] != "mine":
				if array[i-1][j-1] == "mine":
					count += 1
				if array[i-1][j] == "mine":
					count += 1
				if array[i-1][j+1] == "mine":
					count += 1
				if array[i][j-1] == "mine":
					count += 1
				if array[i][j+1] == "mine":
					count += 1
				if array[i+1][j-1] == "mine":
					count += 1
				if array[i+1][j] == "mine":
					count += 1
				if array[i+1][j+1] == "mine":
					count += 1
				array[i][j] = count
				count = 0


def eventHandler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
			pygame.quit()
			quit()

# def letsPlay(event):
# 	if event.type == KEYDOWN and event.key == K_1:
# 		pygame.display.set_caption("Minesweeper: An Oliver and Solomon Production (Easy)")
# 	elif event.type == KEYDOWN and event.key == K_2:
# 		pygame.display.set_caption("Minesweeper: An Oliver and Solomon Production (Medium)")
# 	elif event.type == KEYDOWN and event.key == K_3:
# 		pygame.display.set_caption("Minesweeper: An Oliver and Solomon Production (Hard)")

while begin[0]:
	begin = initialHandler()
	pygame.display.update()

makeDisplay(begin[1])
pygame.display.update()

while weRolling:
	eventHandler()
	pygame.display.update()