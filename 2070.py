T = int(input())
for t in range(T):
  a, b = map(int, input().split())
  if a>b:
    print('#{} >'.format(t+1))
  elif a<b:
    print('#{} <'.format(t+1))
  else:
    print('#{} ='.format(t+1))
