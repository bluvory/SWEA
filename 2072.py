T = int(input())
for t in range(T):
  ans = 0
  numlist = list(map(int, input().split()))
  for num in numlist:
    if num%2 == 1:
      ans += num
  print("#{} {}".format(t+1, ans))
