class Solution:
    def CombinationSum2(self, arr, n, k):
        # code here
        ans = []
        arr.sort()
        def fun(idx, comb, s):
            if idx == n or s > k:
                if s == k:
                    ans.append(comb)
                return
            
            if s == k:
                ans.append(comb)
                return
            
            for i in range(idx, n):
                if i > idx and arr[i - 1] == arr[i]:
                    continue
                s += arr[i]
                fun(i + 1, comb + [arr[i]], s)
                s -= arr[i]
        fun(0, [], 0)
        return ans