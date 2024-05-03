day = input()
n = int(input())

# arr = ["sun"]

# a = n-arr[day]

# z = (a//7)+1
# print(z)
if day=='sun':
    print(round(n/7)+1)
else:
    print(round(n/7))