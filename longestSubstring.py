def longestSubstring(n, s):
    if n <= 1:
        return "-1"
    
    # Create a 2D array to store the lengths of longest repeating non-overlapping substrings
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the result and ending index of the longest repeating non-overlapping substring
    max_length = 0
    end_index = 0
    
    # Iterate over the string and fill the dp array
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if s[i - 1] == s[j - 1] and dp[i - 1][j - 1] < (j - i):
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0
    
    # If no repeating non-overlapping substring found, return -1
    if max_length == 0:
        return "-1"
    
    # Return the longest repeating non-overlapping substring
    return s[end_index - max_length + 1:end_index + 1]

# Example usage:
n = 9
s = "acdcdacdc"
print(longestSubstring(n, s))  # Output: "acd"

n = 7
s = "heheheh"
print(longestSubstring(n, s))  # Output: "heh"
