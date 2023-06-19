def palindrome(s):
    return s[::-1] == s
    while True:
        s = input('Введите слово: ')
        if palindrome(s):
            print(f"{s} это слово палиндром")
        else:
            print ('Это слово не палиндром')