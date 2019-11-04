import iteration_utilities
import more_itertools
import toolz
import cytoolz

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_roundrobin(iterables, func=iteration_utilities.roundrobin):
    iteration_utilities.consume(func(*iterables), None)


@b.add_function()
def more_itertools_roundrobin(iterables, func=more_itertools.roundrobin):
    iteration_utilities.consume(func(*iterables), None)


@b.add_function()
def toolz_interleave(iterables, func=toolz.interleave):
    iteration_utilities.consume(func(iterables), None)


@b.add_function()
def cytoolz_interleave(iterables, func=cytoolz.interleave):
    iteration_utilities.consume(func(iterables), None)


@b.add_arguments('length')
def argument_provider():
    for exponent in range(2, 18):
        size = 2**exponent
        yield size, [[0] * (size // 2), [1] * (size // 2)]


if __name__ == '__main__':
    print(__file__)
    r = b.run()
    r.plot()
    plt.savefig(__file__ + '.png')
