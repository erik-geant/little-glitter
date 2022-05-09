from primePy import primes


def find_primes(input_values):
    for x in input_values:
        if primes.check(x):
            yield x


def test():
    sample_data = range(100)
    for p in find_primes(sample_data):
        print(f'found prime: {p}')


if __name__ == '__main__':
    test()
