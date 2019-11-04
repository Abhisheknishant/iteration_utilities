import iteration_utilities
import toolz
import cytoolz
import more_itertools

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_successive(iterable, func=iteration_utilities.successive):
    iteration_utilities.consume(func(iterable, 50), None)


@b.add_function()
def toolz_sliding_window(iterable, func=toolz.sliding_window):
    iteration_utilities.consume(func(50, iterable), None)


@b.add_function()
def cytoolz_sliding_window(iterable, func=cytoolz.sliding_window):
    iteration_utilities.consume(func(50, iterable), None)


@b.add_function()
def more_itertools_windowed(iterable, func=more_itertools.windowed):
    iteration_utilities.consume(func(iterable, 50), None)


@b.add_arguments(name='length')
def argument_provider():
    for exponent in range(2, 18):
        size = 2**exponent
        yield size, [0] * size


if __name__ == '__main__':
    print(__file__)
    r = b.run()
    r.plot()
    plt.savefig(__file__ + '.png')
