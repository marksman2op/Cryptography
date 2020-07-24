# RSA attack: Small prime
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

def DecipherSmallPrime(ciphertext, modulo, exponent):
    if modulo % 2 == 0:
        small_prime = 2
        big_prime = modulo // 2
        return Decrypt(ciphertext, small_prime, big_prime, exponent)

    for i in range(3, 1000000, 2):
        if modulo % i == 0:
            small_prime = i
            big_prime = modulo // i
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
    return "don't know"

def ConvertToInt(str):
    res = 0
    for i in range(len(str)):
        res = res * 256 + ord(str[i])
    return res

def Encrypt(message, modulo, exponent):
    return pow(ConvertToInt(message), exponent, modulo)

modulo = 101 * 18298970732541109011012304219376080251334480295537316123696052970419466495220522723330315111017831737980079504337868198011077274303193766040393009648852841770668239779097280026631944319501437547002412556176186750790476901358334138818777298389724049250700606462316428106882097210008142941838672676714188593227684360287806974345181893018133710957167334490627178666071809992955566020058374505477745993383434501768887090900283569055646901291270870833498474402084748161755197005050874785474707550376333429671113753137201128897550014524209754619355308207537703754006699795711188492048286436285518105948050401762394690148387
exponent = 239
ciphertext = Encrypt("attack", modulo, exponent)
print(ciphertext)
print(DecipherSmallPrime(ciphertext, modulo, exponent))
