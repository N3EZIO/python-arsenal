def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    for i in range(7-len(s)%6):
            result.append(0)
            i=i+1
    print(len(result))
    convert(result)
    #print(result)



def convert(s):
    sum=0
    cipher=[]
    fc=''
    j=5
    for i in s:
            if j == 0:
                j=5
                sum+=int(i)
                cipher.append(sum)
                sum=0
            else:
                sum+=int(i)*(2**j)
                j=j-1
            
    for i in cipher:
        if i < 26 :
            fc+=chr(i + 65)
        elif 25< i < 52 :
            fc+=chr(i + 71)
        elif 51 < i < 62 :
            fc+=chr(i-4)
       
   
   
    print(fc)        






tobits('nitin')
#binary_convert('hello')