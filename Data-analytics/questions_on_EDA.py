import numpy as np
avg_weight = 50
collected_samples= 40
sample_weight = 49
pop_std = 5
    #z score
z = (sample_weight - avg_weight)/(pop_std/np.sqrt(collected_samples))
print(z)

#getting p valuse from z score
import scipy.stats as stats
p = 1 - stats.norm.cdf(z) #cdf means cumulative distribution function
print(p)
#probability of getting 49
p = stats.norm.cdf(z)
print(p)


