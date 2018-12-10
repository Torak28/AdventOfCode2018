import re

input_str = open('input', 'r').readlines()

id_re = r'^#\d*'
coord_re = r'\d*,\d*'
area_re = r'\d*x\d*'

size = 1000
tab = [['.' for _ in range(size)] for _ in range(size)]


def draw_rect(tab, id, coord, area, overlap_tab):
	for i in range(coord[0], coord[0] + area[0]):
		for j in range(coord[1], coord[1] + area[1]):
			if tab[i][j].isdigit():
				overlap_tab.append(int(tab[i][j]))
				overlap_tab.append(id)
				overlap_tab = list(set(overlap_tab))
				tab[i][j] = 'X'
			elif tab[i][j] is '.':
				tab[i][j] = str(id)
	return tab, overlap_tab


def count_x(tab):
	count = 0
	for i in tab:
		count += i.count('X')
	return count


def overlap_count(highest_id, tab):
	out = 0
	for i in range(1, highest_id + 1):
		if tab.count(i) == 0:
			out = i
			break
	return out


overlap_tab = []
highest_id = 0
for line in input_str:
	id = int(re.search(id_re, line).group()[1:])
	coord_str = re.search(coord_re, line).group()
	coord = [int(coord_str[coord_str.index(',') + 1:]), int(coord_str[:coord_str.index(',')])]
	area_str = re.search(area_re, line).group()
	area = [int(area_str[area_str.index('x') + 1:]), int(area_str[:area_str.index('x')])]
	highest_id = id
	tab, overlap_tab = draw_rect(tab, id, coord, area, overlap_tab)

print(f'Part 1: {count_x(tab)}')
print(f'Part 2: {overlap_count(highest_id, overlap_tab)}')
