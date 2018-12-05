import requests
import config

input_str = requests.get('https://adventofcode.com/2018/day/2/input', cookies=dict(session=config.session)).text

# Part 1
word = ''
twos = 0
threes = 0

for i in input_str:
	if i.isalpha():
		word = word + i
	else:
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
		word = ''

print(f'Part 1 - resulting frequency: {twos * threes}')

# Part 2
word = ''
word_tab = []


def sub_strings(a: str, b: str) -> str:
	out = ''
	for i in list(zip(a, b)):
		if len(set(i)) is 1:
			out += i[0]
	return out

for i in input_str:
	if i.isalpha():
		word = word + i
	else:
		word_tab.append(word)
		word = ''

red_flag = False
for i in word_tab:
	for j in word_tab:
		out = sub_strings(i, j)
		if len(i) - len(out) == 1:
			red_flag = True
			break
	if red_flag:
		break

print(f'Part 2 - common letters between the two correct box IDs: {out}')
