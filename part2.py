def yield_primes(input_values):
    # TODO
    pass


def test():
    sample_data = range(100)
    for p in yield_primes(sample_data):
        print(f'found prime: {p}')


if __name__ == '__main__':
    test()
