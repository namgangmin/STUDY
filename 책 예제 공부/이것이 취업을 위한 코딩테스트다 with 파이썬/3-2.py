n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[n-1]
second = data[n-2]

sumd = 0
count = 0

for _ in range(m):
  if count < k:
    sumd += first
    count += 1
  elif count >= k:
    sumd += second
    count = 0
print(sumd)
