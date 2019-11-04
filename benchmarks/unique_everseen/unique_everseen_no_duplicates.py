import iteration_utilities
import toolz
import cytoolz
import more_itertools

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_unique_everseen(iterable, func=iteration_utilities.unique_justseen):
    iteration_utilities.consume(func(iterable), None)


@b.add_function()
def more_itertools_unique_everseen(iterable, func=more_itertools.unique_everseen):
    iteration_utilities.consume(func(iterable), None)


@b.add_function()
def toolz_unique(iterable, func=toolz.unique):
    iteration_utilities.consume(func(iterable), None)


@b.add_function()
def cytoolz_unique(iterable, func=cytoolz.unique):
    iteration_utilities.consume(func(iterable), None)


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
