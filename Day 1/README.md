# Idea for this day

[Link to the puzzle][1]

I was trying to take advantage of how the input string was constructed. With every line I split chars into three categories:

* digit,
* operator,
* space,

For digit I use `string` type to contain whole number. Whit every iteration of for loop I add digit to `number` variable to then convert it to `int` when space occurs. `Operator` is first char of line and it task is to determine if we gonna add or subtract. That information is then used when the space occurs - the `number` is added to `output`.

:gift:

# Visualization

![alt text][2]

[1]: https://adventofcode.com/2018/day/1
[2]: https://raw.githubusercontent.com/Torak28/AdventOfCode2018/master/Day%201/day1.png