


T = int(input())
for t in range(T):
    a = input()
    if int(a) % 7 != 0:
        for i in range(1000):
            rev_a = a[::-1]
            a = str(int(a)+int(rev_a))
            if int(a) % 7 == 0: break
    if int(a) % 7 == 0: print(a)
    else: print(-1)
