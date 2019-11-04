from operator import add

import iteration_utilities
import itertools
import toolz
import cytoolz

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_accumulate(iterable, func=iteration_utilities.accumulate):
    iteration_utilities.consume(func(iterable, add), None)


@b.add_function()
def itertools_accumulate(iterable, func=itertools.accumulate):
    iteration_utilities.consume(func(iterable, add), None)


@b.add_function()
def toolz_accumulate(iterable, func=toolz.accumulate):
    iteration_utilities.consume(func(add, iterable), None)


@b.add_function()
def cytoolz_accumulate(iterable, func=cytoolz.accumulate):
    iteration_utilities.consume(func(add, iterable), None)


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
