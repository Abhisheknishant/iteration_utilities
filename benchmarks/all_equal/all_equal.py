import iteration_utilities
import more_itertools

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_all_equal(iterable, func=iteration_utilities.all_equal):
    return func(iterable)


@b.add_function()
def more_itertools_all_equal(iterable, func=more_itertools.all_equal):
    return func(iterable)


@b.add_arguments('length')
def argument_provider():
    for exponent in range(2, 18):
        size = 2**exponent
        yield size, [1] * size


if __name__ == '__main__':
    print(__file__)
    r = b.run()
    r.plot()
    plt.savefig(__file__ + '.png')
