"""
def convert(str):
    base2=[]
    
    z=ord(str)
    print(z)
    for i in range(8):
        k=int(z)
        k=k%2
        print(k)
        base2.append(k)
        z=z/2
        z+=0.5
        print(z)
    base2.reverse()
    print(base2)
"""

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
       

#convert('b')
print(trans('b'))