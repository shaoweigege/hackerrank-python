n = int(input())
x = sorted(map(int, input().split()))

def median(median_v):
    median_n = len(median_v)
    if median_n % 2 == 0:
        return int((median_v[median_n // 2] + median_v[(median_n // 2) - 1]) / 2)
    else:
        return int(median_v[median_n // 2])
    
m = n // 2

l = x[:m]
u = x[m + (1 if n % 2 == 1 else 0):]

print(median(l))
print(median(x))
print(median(u))