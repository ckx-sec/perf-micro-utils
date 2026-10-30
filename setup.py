from setuptools import setup, find_packages

setup(
    name="perf-micro-utils",
    version="1.0.2",
    description="Lightweight performance micro-benchmark utilities",
    author="benchmark-team",
    packages=find_packages(),
    package_data={
        "perf_utils": ["bin/*"],
    },
    include_package_data=True,
    python_requires=">=3.8",
)
