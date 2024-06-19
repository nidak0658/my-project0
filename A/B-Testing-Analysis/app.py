import scipy.stats as stats

# Example data (replace with your actual data)
control_group = [10, 12, 15, 11, 9, 13, 8, 14, 12, 10]
variant_group = [15, 17, 18, 16, 14, 19, 13, 20, 17, 15]

# Perform t-test
t_stat, p_value = stats.ttest_ind(control_group, variant_group)
print(f'T-test: t-statistic = {t_stat}, p-value = {p_value}')

# Compare p-value with significance level (e.g., 0.05)
if p_value < 0.05:
    print("Result is statistically significant. Reject the null hypothesis.")
else:
    print("Result is not statistically significant. Fail to reject the null hypothesis.")
