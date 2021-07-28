import random
import string


def make_vin():
    vin = ''.join(random.sample(string.ascii_uppercase + string.digits, 17))
    return vin

