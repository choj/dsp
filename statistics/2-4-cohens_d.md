[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)


<!---

Communicate the problem, how you solved it, and the solution, within each of the following

-->

Using the recorded weights of newborns, we can determine whether first-born babies tend to weigh more or less than babies which are not first-born. 

I calculated the effect size via Cohen's d, which was found to be -0.089, indicating that first borns weigh slightly less than non-first borns. The magnitude of this value indicates a small effect size, and may be specific to the sample population.

I solved it using pieces of code from Think Stats by Allen Downey, shown below.

```
# this code must be run from ThinkStats2/code

import first, thinkstats2

live, firsts, others = first.MakeFrames()

d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print('Cohen d, first births minus others', d)
```

