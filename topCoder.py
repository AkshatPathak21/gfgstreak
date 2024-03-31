n = int(input())

arr = []
for i in range(n):
    arr.append(int(input()))

count = {}

for i in arr:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
ans = 0
for i in count:
    if count[i] %2 != 0:
        ans = i
temp =True
for i in range(1,len(arr)):
    if arr[i-1] == arr[i] == arr[i+1]:
        temp = False
if ans and temp:
    print(ans)
else:
    print(-1)