import numpy as np

# Generate a random dataset of 100 data points
data = np.random.randn(100)  # 100 random points from a normal distribution

# Compute basic statistics
mean_value = np.mean(data)
median_value = np.median(data)
variance_value = np.var(data)
std_dev_value = np.std(data)
percentile_25 = np.percentile(data, 25)  # 25th percentile, or 1st quartile
percentile_50 = np.percentile(data, 50)  # 50th percentile, same as median
percentile_75 = np.percentile(data, 75)  # 75th percentile, or 3rd quartile

# Print the results
print("Agrima Gupta - 11501012021")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value}")
print(f"25th Percentile: {percentile_25}")
print(f"50th Percentile (Median): {percentile_50}")
print(f"75th Percentile: {percentile_75}")
