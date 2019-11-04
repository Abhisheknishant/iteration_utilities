import iteration_utilities
import toolz
import cytoolz

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_all_distinct(iterable, func=iteration_utilities.all_distinct):
    return func(iterable)


@b.add_function()
def toolz_isdistinct(iterable, func=toolz.isdistinct):
    return func(iterable)


@b.add_function()
def cytoolz_isdistinct(iterable, func=cytoolz.isdistinct):
    return func(iterable)


@b.add_arguments('length')
def argument_provider():
    for exponent in range(2, 18):
        size = 2**exponent
        yield size, list(range(size))


if __name__ == '__main__':
    print(__file__)
    r = b.run()
    r.plot()
    plt.savefig(__file__ + '.png')
