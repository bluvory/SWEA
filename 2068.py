T = int(input())
for t in range(T):
  numlist = list(map(int, input().split()))
  print("#{} {}".format(t+1, max(numlist)))
