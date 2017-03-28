[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)


<!-- Communicate the problem, how you solved it, and the solution, within each of the following markdown files. (You can include code blocks and images within markdown.) -->

The problem asks how many men are within the height range of 5'10" to 6'1". It is known that the distribution of heights is approximately normal, with *µ* = 178 cm and *σ* = 7.7 cm. The solution follows from the included Jupyter notebook. A random variable ```dist``` is defined with ```scipy.stats.norm```. Accessing the ```cdf``` method on the random variable yields the percentage of people shorter than a given height. Finding the difference of the two values for the two bounds on the height range yields the total percentage of men in the acceptable range: 34%.

```
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

#dist.mean(), dist.std()

#dist.cdf(mu-sigma)

# Solution

low = dist.cdf(177.8)    # 5'10"
high = dist.cdf(185.4)   # 6'1"
#low, high
high-low

```