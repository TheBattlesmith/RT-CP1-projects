#Nesting: placing one control structure (an if or a loop) inside another one

#Nested if statement: an if inside another if. The inner one is only checked when the outer condition is True.

#Nested loop: a loop inside another loop

#Outer loop / inner loop: the outer loop is the one on the outside. For every single pass of the outer loop, the inner loop runs all the way through.

#Counting runs: the body of the inner loop runs (outer times) × (inner times). An outer loop of 3 and an inner loop of 4 runs the inner body 12 times.

#You can mix them: an if can sit inside a loop, and a loop can sit inside an if

#Indentation shows ownership: every level of nesting is indented one more step. The indentation tells Python (and you) which block each line belongs to.

#Break: a break only exits the loop it is directly inside. In a nested loop, it ends the inner loop and the outer loop keeps going.

#Tip: to understand nested code, trace it by hand. Write down the value of each variable on every pass.

multiplier = 0

for i in range(1, 13):
    multiplier += 1
    for i in range(multiplier, 13 * multiplier + 1, multiplier):
        print(i, end = "\t")
    print("\n")



