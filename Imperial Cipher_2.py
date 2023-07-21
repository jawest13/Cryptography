LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def shift(k,s):
    k = k+s
    if (k == 26):
        k = 0
    elif (k == -1):
        k = 25
    return k

def encrypt(text,k,s):
    translated = ''
    # transverse the plain text
    for symbol in text:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num + k
            if num > 25:
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
            
            k = shift(k,s)
        else:
            translated = translated + symbol
    return translated

def decrypt(text,k,s):
    translated = ''
    # transverse the plain text
    for symbol in text:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - k
            if num > 25:
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
            
            k = shift(k,s)
        else:
            translated = translated + symbol
    return translated


#check the above function
#enter text to be encoded
text = "I WILL ALWAYS LOVE YOU AS I HAVE ALWAYS DECLARED"
#set the key value
k = 7
#set the step value
s = 1

print ("Key Pattern : " + str(k))
print ("Step Value : " + str(s))
print ("Plain Text  : " + text)
print ("Cipher Text : " + encrypt(text,k,s))
print ("De-crypted  : " + decrypt(encrypt(text,k,s),k,s))