def palindrome(s):
    cleaned = ''.join(s.split()).lower()
    if cleaned == cleaned[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"


print(palindrome("А роза упала на лапу Азора"))
