# RSA encryption and decryption
def ConvertToInt(str):
    res = 0
    for i in range(len(str)):
        res = res * 256 + ord(str[i])
    return res

def Encrypt(message, modulo, exponent):
    return pow(ConvertToInt(message), exponent, modulo)

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    b = (b % n + n) % n
    return b

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

def Decrypt(ciphertext, p, q, exponent):
    n = (p - 1) * (q - 1)
    d = InvertModulo(exponent, n)
    return ConvertToStr(pow(ciphertext, d, p * q))

a = 3
b = 7
c = InvertModulo(a, b)
print(c)

p = 1000000007
q = 1000000009
exponent = 23917
modulo = p * q
ciphertext = Encrypt("attack", modulo, exponent)
message = Decrypt(ciphertext, p, q, exponent)
print(message)
