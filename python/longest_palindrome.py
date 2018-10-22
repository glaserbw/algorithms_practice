# Check longest palindrome substring

# Test cases
str = 'abbaca'

# First we check if it's a palindrome
def check_pal(str):
	if len(str) <= 1:
		return True 
	if str[0] != str[-1]:
		return False
	else: 
		return check_pal(str[1:-1])

# Then we check if it's the longest
def longest_palindrome(str):
	longest = 1
	result = ''
	for i in range(len(str)-1):
		count = 1 
		for j in range(i+1, len(str)):
			if str[i] == str[j]:
				if check_pal(str[i:j+1]) and count > longest:
					result = str[i:j+1]
					longest = count
				break
			count += 1
	return result

print(longest_palindrome(str))

