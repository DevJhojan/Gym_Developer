def is_palindromo(text):
    text = text.replace(" ", "").lower()
    start = 0
    end = len(text) - 1
    while start < end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    return True
print(is_palindromo("oso"))
print(is_palindromo("Python"))
print(is_palindromo("Anita lava la tina"))

