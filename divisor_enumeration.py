N = 1000

sq_N = int(N**0.5)
lower_divisor = []
upper_divisor = []

for i in range(1, sq_N+1):
    print("i", i)
    if N % i == 0:
        lower_divisor.append(i)
        if N//i != i:
            upper_divisor.append(N//i)

divisor = lower_divisor + upper_divisor[::-1]
print(divisor)
