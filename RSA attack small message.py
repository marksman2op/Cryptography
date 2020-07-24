# RSA attack: Small message
def ConvertToInt(str):
    res = 0
    for i in range(len(str)):
        res = res * 256 + ord(str[i])
    return res

def Encrypt(message, modulo, exponent):
    return pow(ConvertToInt(message), exponent, modulo)

def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
  for i in range(len(potential_messages)):
    if ciphertext == Encrypt(potential_messages[i], modulo, exponent):
      return potential_messages[i]
  return "don't know"

modulo = 101
exponent = 12
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSimple(ciphertext, modulo, exponent, ["attack", "don't attack", "wait"]))
