key = "EAFLES"
message = "TANYAMAN"
key = key.replace("J", "I")

messaged = "POGGQTDF"

dup = message

dup = dup.replace(" ", "")

if len(dup) % 2 != 0:
    message += "X"

list_1 = ["0" for i in range(len(dup))]

list_2 = ["0" for i in range(len(dup))]

print(dup)


alphabets = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
key_list = [
    [2, 4, 6, 8, 4],
    [1, 3, 5, 7, 3],
    [8, 6, 4, 2, 2],
    [7, 5, 3, 1, 4],
    [7, 5, 3, 1, 7],
]

for i in range(5):
    for j in range(5):
        key_list[i][j] = "0"
"""
for i in range(0, 4):w
    for j in range(5):
        print(key_list[i][j])
"""


def make_key():
    i = 0
    j = 0
    for k in key:
        if ord(k) > 74:
            shift = 66
        else:
            shift = 65
        if j > 4:
            i = i + 1
            j = 0
        else:
            if alphabets[ord(k) - shift] != "0":
                key_list[i][j] = alphabets[ord(k) - shift]
                alphabets[ord(k) - shift] = "0"
                j = j + 1
                if j > 4:
                    i = i + 1
                    j = 0
        # print(alphabets)
    k = 0

    for x in range(i, 5):
        for y in range(j, 5):
            if alphabets[k] != "0":
                key_list[x][y] = alphabets[k]
                k = k + 1
            else:
                key_list[x][y] = alphabets[k + 1]
                k = k + 2
    x = 0
    for a in message:
        for i in range(5):
            for j in range(5):
                if key_list[i][j] == a:
                    list_1[x] = i
                    list_2[x] = j
                    x = x + 1
    # print(list_1)
    # print(list_2)

    transform(key_list)


def transform(key_list):
    print(list_1)
    print(list_2)
    print(key_list)
    k = 0
    b = 1
    encrypt = ""
    encrypt1 = ""
    encrypt2 = ""
    for i in range(int(len(list_1) / 2)):
        j = list_1[k]
        l = list_1[b]
        print(l)
        encrypt1 += key_list[j][l]
        j = list_2[k]
        l = list_2[b]
        encrypt2 += key_list[j][l]
        k = k + 2
        b = b + 2
    encrypt = encrypt1 + encrypt2
    print(encrypt)


def decryption():
    # print(key_list)
    list_dec = ["0" for i in range(2 * len(dup))]
    list_dec1 = ["0" for i in range(len(dup))]
    list_dec2 = ["0" for i in range(len(dup))]
    x = 0
    for a in messaged:
        for i in range(5):
            for j in range(5):
                if key_list[i][j] == a:
                    if x < (len(messaged) / 2):
                        list_dec[x] = i
                        list_dec[x + 1] = j
                        x = x + 2
                    else:
                        list_dec[x] = i
                        list_dec[x + 1] = j
                        x = x + 2

    h = int(len(list_dec) / 2)

    for i in range(len(list_dec)):
        if i < h:
            list_dec1[i] = list_dec[i]
        else:
            list_dec2[i - h] = list_dec[i]

    print(list_dec)
    print(list_dec1)
    print(list_dec2)
    print(key_list)
    k = 0
    dencrypt1 = ""
    for i in range(len(list_1)):
        j = list_dec1[k]
        l = list_dec2[k]
        print(l)
        dencrypt1 += key_list[j][l]
        k = k + 1

    print(dencrypt1)


make_key()

decryption()
