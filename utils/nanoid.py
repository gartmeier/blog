from nanoid import generate as _generate

alphabet = "0123456789abcdefghijklmnopqrstuvwxyz"


def generate(size=12):
    return _generate(alphabet=alphabet, size=size)
