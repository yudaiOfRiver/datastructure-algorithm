N = 50

is_prime = [True] * (N+1)
is_prime[0] = False
is_prime[1] = False

sq_N = int(N**0.5) # ここまで調べれば十分
for i in range(1, sq_N+1):
    if not is_prime[i]:
        continue
    for j in range(i**2, N+1, i):
        is_prime[j] = False

for i, is_primei in enumerate(is_prime):
    print(i, is_primei)
