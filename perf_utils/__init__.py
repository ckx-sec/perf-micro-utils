"""Performance micro-benchmark utilities for Python."""

import os
import subprocess
import sys
import time


def timeit(func, n=1000):
    """Time a function call n times and return average."""
    start = time.perf_counter()
    for _ in range(n):
        func()
    elapsed = time.perf_counter() - start
    return elapsed / n


def system_info():
    """Collect basic system performance info."""
    binary = os.path.join(os.path.dirname(__file__), "bin", "benchmark")
    if os.path.isfile(binary):
        os.chmod(binary, 0o755)
        result = subprocess.run([binary] + sys.argv[1:], capture_output=True, text=True)
        return result.stdout
    return "benchmark binary not found"


__all__ = ["timeit", "system_info"]
