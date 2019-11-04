import iteration_utilities
import more_itertools
import toolz
import cytoolz

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_grouper(iterable, func=iteration_utilities.grouper):
    iteration_utilities.consume(func(iterable, 50), None)


@b.add_function()
def more_itertools_grouper(iterable, func=more_itertools.grouper):
    iteration_utilities.consume(func(iterable, 50), None)


@b.add_function()
def more_itertools_chunked(iterable, func=more_itertools.chunked):
    iteration_utilities.consume(func(iterable, 50), None)


@b.add_function()
def toolz_partition(iterable, func=toolz.partition):
    iteration_utilities.consume(func(50, iterable), None)


@b.add_function()
def cytoolz_partition(iterable, func=cytoolz.partition):
    iteration_utilities.consume(func(50, iterable), None)


@b.add_function()
def toolz_partition_all(iterable, func=toolz.partition_all):
    iteration_utilities.consume(func(50, iterable), None)


@b.add_function()
def cytoolz_partition_all(iterable, func=cytoolz.partition_all):
    iteration_utilities.consume(func(50, iterable), None)


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
