#!/usr/bin/env python3


import sys


print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")
deps_ok: bool = True
try:
    import pandas
    print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
except ImportError:
    print("[MISSING] pandas")
    deps_ok = False
try:
    import numpy
    print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
except ImportError:
    print("[MISSING] numpy")
    deps_ok = False
try:
    import matplotlib
    import matplotlib.pyplot as plt
    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
except ImportError:
    print("[MISSING] matplotlib")
    deps_ok = False

if not deps_ok:
    sys.exit(1)


def generate() -> numpy.ndarray:
    """Generate an 1D array with 1000 random numbers between 0 and 100."""
    ran_list: numpy.ndarray = numpy.random.randint(100, size=(1000))
    return ran_list


def analyze(
        ran_list: numpy.ndarray
        ) -> tuple[pandas.DataFrame, float, float, float]:
    """Analyze the data with the mean, max and min value."""
    data_frame = pandas.DataFrame(ran_list, columns=['signal'])
    mean = data_frame['signal'].mean()
    max_val = data_frame['signal'].max()
    min_val = data_frame['signal'].min()
    return data_frame, mean, max_val, min_val


def visualize(data: tuple[pandas.DataFrame, float, float, float]) -> None:
    """Visualize our data into a line chart."""
    plt.title("Matrix Signal Strength")
    plt.xlabel("Sample")
    plt.ylabel("Signal (%)")
    plt.plot(data[0]['signal'])
    plt.savefig('matrix_analysis.png')
    plt.close()


def show_package_versions() -> None:
    """Display installed package versions for comparison."""
    print("\nInstalled package versions:")
    print(f"  pandas:     {pandas.__version__}")
    print(f"  numpy:      {numpy.__version__}")
    print(f"  matplotlib: {matplotlib.__version__}")


if __name__ == "__main__":
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")
    visualize(analyze(generate()))
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png\n")
    show_package_versions()
    print("\n== Difference between pip and poetry ==")
    print("pip: installs dependencies from "
          "requirements.txt (pip install -r requirements.txt)")
    print("Poetry: installs dependencies from pyproject.toml (poetry install)")
    print("Poetry also automatically creates a virtual environment (venv)")
