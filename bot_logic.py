import random
import time

def gen_pass(pass_length):
    character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password = ""

    for i in range(pass_length):
        password += random.choice(character)

    return password

def coins(second):
    face = random.randint(1, 2)
    if face == 1:
        time.sleep(second)
        return 'koin atas'
    else:
        time.sleep(second)
        return 'koin bawah'

print(gen_pass(10))