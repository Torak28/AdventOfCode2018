# Idea for this day

[Link to the puzzle][1]

I'm just iterate over all word and then just count how many of the same letter are in word. I'm always checking first letter, because in the end I replace all letters that I'm considering in that point with ''.

```py
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
```

[1]: https://adventofcode.com/2018/day/2