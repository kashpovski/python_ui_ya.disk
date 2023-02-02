import random
import string


def get_content_name(long=10, letters=True, digits=False, simbols=False):
    strings = (string.ascii_letters if letters else "") + \
              (string.digits if digits else "") + \
              (string.punctuation if simbols else "")
    return "".join(random.choice(strings) for x in range(long))

