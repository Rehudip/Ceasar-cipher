
word = 'a quick brown fox jumps over the lazy dog'
adjust = 3
ciphered_word = ''

for a in word:
  ceasar_letter = ord(a)
  if ceasar_letter == 32:
    pass
  #IF UPPERCASE
  elif 65 <= ceasar_letter < 91:
    ceasar_letter = ((ceasar_letter - 65 + adjust) % 26) + 65
  #if lowercase
  elif 97 <= ceasar_letter < 123:
    ceasar_letter = ((ceasar_letter - 97 + adjust) % 26) + 97
  else:
    break
  ciphered_word = ciphered_word + chr(ceasar_letter)
print(ciphered_word)
