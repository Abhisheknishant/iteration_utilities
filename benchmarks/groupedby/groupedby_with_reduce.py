import operator

import iteration_utilities
import toolz
import cytoolz

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_groupedby(iterable, func=iteration_utilities.groupedby):
    return func(iterable, iteration_utilities.return_identity, reduce=operator.add)


@b.add_function()
def toolz_reduceby(iterable, func=toolz.reduceby):
    return func(iteration_utilities.return_identity, operator.add, iterable)


@b.add_function()
def cytoolz_reduceby(iterable, func=cytoolz.reduceby):
    return func(iteration_utilities.return_identity, operator.add, iterable)


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
