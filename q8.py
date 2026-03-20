text = ("palindromemordnilap")
reversedtext = ("")
def check_palindrome():
    global text
    global reversedtext
    reversedtext = text[::-1] # Looked up online how to make a string reversed
    if reversedtext == text:
        return True
    else:
        return False
print(check_palindrome())

