def isPalindromeNumber(num):
    if num < 0:
        return False
    original_num = num
    rev_num = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        rev_num = rev_num*10 + last_digit
    return original_num == rev_num
	