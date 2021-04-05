def trans(ctr):
    x=ord(ctr)
    bit=[]
    if x == 0: 
        bit.append(0)
        return bit
    while x:
        bit.append(x % 2)
        x >>= 1
    bit.reverse()

    return bit

def decode(str):
    bits=[]
    for i in str:
        bits+=trans(i)
    print(bits)
        
decode('bml0aW4')