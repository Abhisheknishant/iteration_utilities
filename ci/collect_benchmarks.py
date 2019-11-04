import pathlib
import shutil
import subprocess

if __name__ == '__main__':
    benchmark_paths = pathlib.Path('./benchmarks/').glob('**/*.py')
    for path in benchmark_paths:
        subprocess.call(['python', str(path)])

    for path in pathlib.Path('./.benchmark_results/').glob('**/*.png'):
        path.unlink()

    pathlib.Path('./.benchmark_results/').mkdir(exist_ok=True)

    result_paths = pathlib.Path('./benchmarks/').glob('**/*.png')
    for path in result_paths:
        shutil.move(str(path), './.benchmark_results/')
