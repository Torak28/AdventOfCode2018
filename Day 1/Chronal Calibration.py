import requests
import config

input_str = requests.get('https://adventofcode.com/2018/day/1/input', cookies=dict(session=config.session)).text

out = 0
number = ''

# Part 1
for i in input_str:
	if i.isdigit():
		number = number + i
	elif i is '+' or i is '-':
		operator = True if i is '+' else False
	else:
		out = out + int(number) if operator else out - int(number)
		number = ''

print(f'Part 1 - resulting frequency: {out}')

# Part 2
out = 0
out_tab = [out]
number = ''
unique = None

while unique is None:
	for i in input_str:
		if i.isdigit():
			number = number + i
		elif i is '+' or i is '-':
			operator = True if i is '+' else False
		else:
			out = out + int(number) if operator else out - int(number)
			number = ''
			if out in out_tab:
				unique = out
				break
			out_tab.append(out)

print(f'Part 2 - first frequency my device reaches twice: {unique}')
