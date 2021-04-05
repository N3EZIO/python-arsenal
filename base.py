def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    for i in range(7-len(s)%6):
            result.append(0)
            i=i+1
    print(result)


def convert(s):
    






tobits('hello')