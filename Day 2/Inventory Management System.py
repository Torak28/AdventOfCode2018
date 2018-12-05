import requests
import config

input_str = requests.get('https://adventofcode.com/2018/day/2/input', cookies=dict(session=config.session)).text

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
