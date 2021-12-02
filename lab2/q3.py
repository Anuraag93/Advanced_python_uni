
time = int(input("time in mins "))
MINUTES_IN_DAY = 24 * 60
days = time / MINUTES_IN_DAY
time_Left = time % MINUTES_IN_DAY
hours = time_Left / 60
minutes = time_Left % 60

print("days: {}, hours: {}, minutes: {}".format(int(days),int(hours),minutes))