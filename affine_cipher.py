def encrypt(ch):
    a=24
    b=8
    f=ord(ch)*a + b
    new = capitalize(f)
    return new

def capitalize(x):
    """
    x=x-26
    if x < 27:
        return x
    else:
        capitalize(x)
    """
    while x>26:
        x=x-26
    return x


def affine(str):
    ciph=''
    for i in str:
        z=encrypt(i)
        ciph+=chr(z+65)
    print(ciph)



affine('youtube.com')