import math
def nthCharacter(self, s, r, n):
        # code here
        block_size=math.pow(2,r)
        pos_in_block=n%block_size
        block_number=int(n//block_size)
        s=s[block_number]
        n=block_number
        for i in range(r):
            arr=[]
            for i in range(len(s)):
                if s[i]=='0':
                    arr.append('0')
                    arr.append('1')
                else:
                    arr.append('1')
                    arr.append('0')
            s=''.join(arr)
        return arr[int(pos_in_block)]