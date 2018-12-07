import requests
import config
import matplotlib.pyplot as plt
import numpy as np

input_str = requests.get('https://adventofcode.com/2018/day/2/input', cookies=dict(session=config.session)).text

word = ''
word_tab = []
twos = 0
threes = 0

for i in input_str:
	if i.isalpha():
		word = word + i
	else:
		word_tab.append(word)
		word = ''

iteration_part1 = 0
twos_tab = []
threes_tab = []
red_flag = False
for word in word_tab:
	it = 0
	two_flag = True
	three_flag = True
	while(len(word) is not 0):
		if word.count(word[it]) == 2 and two_flag is True:
			twos = twos + 1
			two_flag = False
		if word.count(word[it]) == 3 and three_flag is True:
			threes = threes + 1
			three_flag = False
		word = word.replace(word[it], '')
	if two_flag is False:
		twos_tab.append(2)
	else:
		twos_tab.append(0)
	if three_flag is False:
		threes_tab.append(3)
	else:
		threes_tab.append(0)	
	iteration_part1 += 1

def sub_strings(a: str, b: str) -> str:
	out = ''
	for i in list(zip(a, b)):
		if len(set(i)) is 1:
			out += i[0]
	return out

red_flag = False
iteration_part2 = 0
out_it = 0
for i in word_tab:
	for j in word_tab:
		out = sub_strings(i, j)
		if len(i) - len(out) == 1:
			red_flag = True
			break
	iteration_part2 += 1
	if red_flag:
		out_it = iteration_part2
		break


print(f'Part 1 - resulting frequency: {twos * threes}')
print(f'Part 2 - common letters between the two correct box IDs: {out}')

fig, ax = plt.subplots()
ax.plot(range(0, iteration_part1), twos_tab, 'o', label='twos')
ax.plot(range(0, iteration_part1), threes_tab, 'o', label='threes')
ax.legend(bbox_to_anchor=(0.90, 0.85))
plt.annotate('Part2: ' + out, xy=(iteration_part2, 1), arrowprops=dict(facecolor='black', shrink=0.05))
plt.title('Day 2 - Inventory Management System')
plt.xlabel('Iteration')
plt.ylabel('Twos or Threes')
plt.grid(True)
#plt.show()
plt.savefig('day2.png')
