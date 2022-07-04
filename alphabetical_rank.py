message = [5, 8, 23, 28, 32]


def rank():
    sum = message[0]
    for i in range(1, len(message)):
        message[i] = message[i] - sum
        sum += message[i]
    print(message)
