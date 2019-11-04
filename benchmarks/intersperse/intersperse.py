import iteration_utilities
import more_itertools
import toolz
import cytoolz

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_intersperse(iterable, func=iteration_utilities.intersperse):
    iteration_utilities.consume(func(iterable, 2), None)


@b.add_function()
def more_itertools_intersperse(iterable, func=more_itertools.intersperse):
    iteration_utilities.consume(func(2, iterable), None)


@b.add_function()
def toolz_interpose(iterable, func=toolz.interpose):
    iteration_utilities.consume(func(2, iterable), None)


@b.add_function()
def cytoolz_interpose(iterable, func=cytoolz.interpose):
    iteration_utilities.consume(func(2, iterable), None)


@b.add_arguments('length')
def argument_provider():
    for exponent in range(2, 18):
        size = 2**exponent
        yield size, [i % 10 for i in range(size)]


if __name__ == '__main__':
    print(__file__)
    r = b.run()
    r.plot()
    plt.savefig(__file__ + '.png')
