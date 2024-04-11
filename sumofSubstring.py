#Sum of all possible substring of an int

s = str(int(input()))
arr = []
for j in range(0,len(s)):
    for i in range(0,len(s)-j):
        arr.append(int(s[i:i+j+1]))

print("The sum of all possible substrings is",sum(arr))

