# 0. Print out every prime number between 1 and 1000.
# +++++++++++++++++++++++++++++++++++++++++++++++++++

start = 1
stop = 1000
is_prime = False

for num in range(start, stop + 1):
    if num > start:
        is_prime = True

        for i in range(start + 1, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    is_prime = False
                    break
        
        if is_prime:
            print(num)
