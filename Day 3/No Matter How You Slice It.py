import re

input_str = open('input', 'r').readlines()

id_re = r'^#\d*'
coord_re = r'\d*,\d*'
area_re = r'\d*x\d*'

size = 8
tab = [['.' for _ in range(size)] for _ in range(size)]


def draw_rect(tab, id, coord, area):
	for i in range(coord[0], coord[0] + area[0]):
		for j in range(coord[1], coord[1] + area[1]):
			print(f'I: {i}, J: {j}')
			print(f'tab[i - 1]pj - 1]: {tab[i - 1][j - 1]}')
			if tab[i - 1][j - 1].isdigit():
				tab[i - 1][j - 1] = 'X'
			else:
				tab[i - 1][j - 1] = str(id)
	return tab


def count_x(tab):
	count = 0
	for i in tab:
		count += i.count('X')
	return count

for line in input_str:
	id = int(re.search(id_re, line).group()[1:])
	coord_str = re.search(coord_re, line).group()
	coord = [int(coord_str[coord_str.index(',') + 1:]), int(coord_str[:coord_str.index(',')])]
	area_str = re.search(area_re, line).group()
	area = [int(area_str[:area_str.index('x')]), int(area_str[area_str.index('x') + 1:])]
	# print(f'Word: {line[0:-1]}, Id: {id}, Coord: {coord}, Area: {area}')
	tab = draw_rect(tab, id, coord, area)

# print(tab)
print(f'Part 1: {count_x(tab)}')