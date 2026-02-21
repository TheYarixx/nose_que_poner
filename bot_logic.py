import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emoji():
    emojis = ["😀", "🙂", "😆", "🤣", "😎", "🔥"]
    return random.choice(emojis)


def flip_coin():
    return random.choice(["Cara", "Cruz"])