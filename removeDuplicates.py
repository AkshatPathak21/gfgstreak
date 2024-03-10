def removeDuplicates(self,str):
	ans=""
	for i in str:
		if i not in ans:
			ans+=i
	return ans