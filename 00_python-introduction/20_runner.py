# 0. If a runner runs 10 miles in 30 minutes and 30 seconds,
#    what is their average speed in kilometers per hour?
#    (Tip: 1 mile = 1.6 km)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

miles_ran = 10
kilometers_ran = miles_ran * 1.6 # 1 mile = 1.6 km
time_in_minutes = 30 + (30 / 60) # 60 secs = 1 minute
time_in_hours = time_in_minutes / 60 # 60 mins = 1 hour

# average_speed = distance / time
average_speed = kilometers_ran / time_in_hours # km/h
