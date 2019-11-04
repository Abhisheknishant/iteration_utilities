import iteration_utilities
import more_itertools
import toolz
import cytoolz
import heapq
import itertools

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_merge(iterables, func=iteration_utilities.merge):
    iteration_utilities.consume(func(*iterables), None)


@b.add_function()
def heapq_merge(iterables, func=heapq.merge):
    iteration_utilities.consume(func(*iterables), None)


@b.add_function()
def builtin_sorted(iterables, func=sorted):
    return func(itertools.chain.from_iterable(iterables))


@b.add_function()
def toolz_merge_sorted(iterables, func=toolz.merge_sorted):
    iteration_utilities.consume(func(*iterables), None)


@b.add_function()
def cytoolz_merge_sorted(iterables, func=cytoolz.merge_sorted):
    iteration_utilities.consume(func(*iterables), None)


@b.add_arguments('length')
def argument_provider():
    for exponent in range(2, 18):
        size = 2**exponent
        yield (size, [list(range(size // 2)), list(range(size // 2))])


if __name__ == '__main__':
    print(__file__)
    r = b.run()
    r.plot()
    plt.savefig(__file__ + '.png')
