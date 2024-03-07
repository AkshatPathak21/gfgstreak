def sumBitDifferences(self,arr, n):
    	# code here
        bit_diff_sum = 0


        for i in range(32):

            set_bit_count = 0
            for num in arr:
                if num & (1 << i):
                    set_bit_count += 1
    
            clear_bit_count = n - set_bit_count
    
           
            bit_diff_sum += set_bit_count * clear_bit_count * 2  
    
        return bit_diff_sum