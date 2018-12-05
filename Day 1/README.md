# Idea for this day

[Link to the puzzle][1]

I was trying to take advantage of how the input string was constructed. With every line I split chars into three categories:

* digit,
* operator,
* space,

Digit I use `string` type to contain whole number. Whit every iteration of for loop I add digit to `number` variable to then convert it to `int` when space occure. `Operator` is first char of line and it just determine if when the space occure the `number` will be added to `output`.

:gift:

[1]: https://adventofcode.com/2018/day/1