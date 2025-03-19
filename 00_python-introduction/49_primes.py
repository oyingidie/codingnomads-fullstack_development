# 0. Print out every prime number between 1 and 1000.
# +++++++++++++++++++++++++++++++++++++++++++++++++++

start = 1
stop = 1000
is_prime = True

for num in range(start, stop + 1):
    if i > start:
        is_prime = True

        for j in range(start + 1, int(i ** 0.5) + 1):
                if (i % j) == 0:
                    is_prime = False
                    break
        
        if is_prime:
            print(num)
