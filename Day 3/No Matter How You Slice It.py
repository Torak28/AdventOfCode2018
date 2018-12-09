import re

input_str = open('input', 'r').readlines()

id_re = r'^#\d*'
coord_re = r'\d*,\d*'
area_re = r'\d*x\d*'

size = 10
tab = [['.' for _ in range(size)] for _ in range(size)]


def draw_rect(tab, id, coord, area):
	tab

for line in input_str:
	id = int(re.search(id_re, line).group()[1:])
	coord_str = re.search(coord_re, line).group()
	coord = [int(coord_str[coord_str.index(',') + 1:]), int(coord_str[:coord_str.index(',')])]
	area_str = re.search(area_re, line).group()
	area = [int(area_str[:area_str.index('x')]), int(area_str[area_str.index('x') + 1:])]
	print(f'Word: {line[0:-1]}, Id: {id}, Coord: {coord}, Area: {area}')
