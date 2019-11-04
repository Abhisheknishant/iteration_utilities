import iteration_utilities
import more_itertools

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_split(iterable, func=iteration_utilities.split):
    iteration_utilities.consume(func(iterable, lambda x: x % 5 == 0), None)


@b.add_function()
def more_itertools_split_at(iterable, func=more_itertools.split_at):
    iteration_utilities.consume(func(iterable, lambda x: x % 5 == 0), None)


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
