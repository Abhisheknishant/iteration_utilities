import iteration_utilities
import more_itertools

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_unique_justseen(iterable, func=iteration_utilities.unique_justseen):
    iteration_utilities.consume(func(iterable), None)


@b.add_function()
def more_itertools_unique_justseen(iterable, func=more_itertools.unique_justseen):
    iteration_utilities.consume(func(iterable), None)


@b.add_arguments('length')
def argument_provider():
    for exponent in range(2, 18):
        size = 2**exponent
        yield size, sorted(range(size))


if __name__ == '__main__':
    print(__file__)
    r = b.run()
    r.plot()
    plt.savefig(__file__ + '.png')
