import iteration_utilities
import toolz
import cytoolz
import more_itertools

from simple_benchmark import BenchmarkBuilder
import matplotlib.pyplot as plt

b = BenchmarkBuilder()


@b.add_function()
def iu_applyfunc(n, func=iteration_utilities.applyfunc):
    iteration_utilities.consume(func(iteration_utilities.return_True, 1), n)


@b.add_function()
def more_itertools_iterate(n, func=more_itertools.iterate):
    iteration_utilities.consume(func(iteration_utilities.return_True, 1), n)


@b.add_function()
def toolz_iterate(n, func=toolz.iterate):
    iteration_utilities.consume(func(iteration_utilities.return_True, 1), n)


@b.add_function()
def cytoolz_iterate(n, func=cytoolz.iterate):
    iteration_utilities.consume(func(iteration_utilities.return_True, 1), n)


@b.add_arguments('length')
def argument_provider():
    for exponent in range(2, 18):
        size = 2**exponent
        yield size, size


if __name__ == '__main__':
    print(__file__)
    r = b.run()
    r.plot()
    plt.savefig(__file__ + '.png')
