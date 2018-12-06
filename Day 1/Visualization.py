import requests
import config
import matplotlib.pyplot as plt
import numpy as np

input_str = requests.get('https://adventofcode.com/2018/day/1/input', cookies=dict(session=config.session)).text

out = 0
part_1 = 0
part_2 = None
out_tab = [out]
number = ''
iteration_for = 0
iteration_while = 0

# Part 1 and 2
while part_2 is None:
	for i in input_str:
		if i.isdigit():
			number = number + i
		elif i is '+' or i is '-':
			operator = True if i is '+' else False
		else:
			out = out + int(number) if operator else out - int(number)
			number = ''
			if out in out_tab:
				part_2 = out
				it_p2 = len(out_tab)
				out_tab.append(out)
				break
			out_tab.append(out)
		iteration_for += 1
	if iteration_while is 0:
		part_1 = out
		it_p1 = len(out_tab)
	iteration_while += 1

print(f'Part 1 - resulting frequency: {part_1}')
print(f'Part 2 - first frequency my device reaches twice: {part_2}')

plt.plot(range(0, len(out_tab)), out_tab, 'r')
plt.annotate('Resulting frequency', xy=(it_p1, part_1), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('First frequency reaches twice', xy=(it_p2, part_2), arrowprops=dict(facecolor='black', shrink=0.05))
plt.title('Day 1 - Chronal Calibration')
plt.xlabel('Iteration')
plt.ylabel('Frequency value')
plt.grid(True)
plt.savefig('day1.png')
plt.show()