#Q3
# convert time in minutes to days, hours and minutes

# Part A
# Use interactive shell to convert 173420  minutes into days,
# hours and minutes

time = 173420

MINUTES_IN_DAY = 24 * 60

days = time // MINUTES_IN_DAY
timeLeft = time % MINUTES_IN_DAY

hours = timeLeft // 60
minutes = timeLeft % 60

print("time in minutes:", time)
print("days:", days, "hour:", hours, "minutes:", minutes)
