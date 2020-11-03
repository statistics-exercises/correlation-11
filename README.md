# Generating linearly correlated random variables

The difference that was introduced in the last exercise was that the y-intercept for the midpoint of the two lines was non-zero.  You thus had to generate each Y value using:

![](https://render.githubusercontent.com/render/math?math=Y=X%2B1%2B\delta)

 where X is a uniform random variable between 0 and 1 and ![](https://render.githubusercontent.com/render/math?math=\delta) here is a uniform random variable between -1 and -1.

You perhaps already know what I am going to ask you to do in this problem.  Once again if you press run you will see a graph with two lines on it and you must (as always) generated 100 random points that fall between these two lines.  Now the equations of the two lines are:

y = 4x - 5

y = 4x + 1

As always you should not need to use conditional (if) statements in order to achieve this.
