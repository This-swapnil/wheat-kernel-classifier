from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="swapnil",
    description="Wheat Kernel Classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/This-swapnil/wheat-kernel-classifier",
    author_email="sswapnil0098@gmail.com",
    packages=["src"],
    python_requires=">=3.9",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)