phrase = input ("Please enter your phrase to test if it is a palindrome. ")

phrase = phrase.lower()

phrase = phrase.replace('!', '').replace('?', '').replace(',', '').replace('"', '').replace("'","").replace(':', '').replace(' ', '').strip('.')

print(phrase)

if phrase == phrase[::-1]:
    print('Yay! Your phrase is a palindrome!')

else: print('The given phrase is NOT a palindrome')

