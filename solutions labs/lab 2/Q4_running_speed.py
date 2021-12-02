# Question 4

# You run 10 kms in 40 mins and 39 secs
# How many miles you can run in an hour?
# 1 mile is 1,609 kms

# time in second to run 10 kms
time = 40 * 60 + 39

# number of kms run in 1 hour
kmsPerHour = (10 / time) * 3600

# number of miles run in 1 hour
milesPerHour = kmsPerHour / 1.609

print("speed (in miles per hour):", milesPerHour)
