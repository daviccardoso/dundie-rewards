from setuptools import setup, find_packages
import os


def read(*paths):
    root = os.path.dirname(__file__)
    filepath = os.path.join(root, *paths)

    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    return [
        line.strip()
        for line in read(path)
        if not line.startswith("#", "git+", '"', "-")
    ]


setup(
    name="dundie",
    version="0.1.0",
    description="Reward system for employees of Dunder Mifflin Paper Company",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Davi Cardoso",
    packages=find_packages(),
    entry_points={"console_scripts": ["dundie = dundie.__main__:main"]},
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt"),
    },
)
