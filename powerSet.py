def generate_subsequences(self,s,idx,curr,result):
        if idx == len(s):
            if curr:
                result.append(curr)
            return
        
        self.generate_subsequences(s,idx+1,curr+s[idx],result)
        
        self.generate_subsequences(s,idx+1,curr,result)
        
def AllPossibleStrings(self, s):
	result =[]
	self.generate_subsequences(s,0,'',result)
	return sorted(result)