class noalphabetException(Exception):
  # "Error on Ceasar_cipher"
  "your word contains not-a-alphabet"
  pass

word = 'a quick brown fox jumps over the lazy dog'
adjust = 5

def cipher(word,adjust=3):
  ciphered_word = ''
  try:
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
        raise noalphabetException
        break
      ciphered_word = ciphered_word + chr(ceasar_letter)
    #print(ciphered_word)
  except noalphabetException as e:
    print("your word contains not-a-alphabet")
    return None
  return ciphered_word

cipher(word,adjust)
