# 0. Print out every prime number between 1 and 1000.
# +++++++++++++++++++++++++++++++++++++++++++++++++++

start = 1
stop = 1000

for i in range(start, stop + 1):
    if i > start:
        for j in range(start + 1, i):
            if i % j == 0:
                break
    else:
        is_prime = False

if is_prime:
    print(i)
