class Solution:
    def DivisibleByEight(self,s):
        #code here
        length = len(s)
        if length < 3:
            return 1 if int(s) % 8 == 0 else -1
        else:
            last_three_digits = int(s[-3:])
            return 1 if last_three_digits % 8 == 0 else -1


