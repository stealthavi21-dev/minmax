a=int(input())
while a>0:
  b=int(input())
  l1=list(map(int,input().split(' ')))
  print(min(l1),max(l1))
  a=a-1
