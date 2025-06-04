# 0. Use a built-in Python module to tell you the current date and time.
# 1. Research online, so you can print it in a readable manner.
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import datetime

current_date_time = datetime.datetime.now()
formatted_date = current_date_time.strftime("%A, %d %B %Y")
formatted_time = current_date_time.strftime("%H:%M:%S")

