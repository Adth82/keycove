from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="keycove",
    version="0.3.5",
    description="An API authentication library. Create, verify, and securely store API keys.",
    packages=find_packages(),
    install_requires=[
        "cryptography>=42.0.3",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keycove/keycove",
    author="Jaz Allibhai",
    author_email="jaz.allibhai@gmail.com",
    license="MIT",
0x493d492961b89b5c0e04f86341825ae37ba3b500)
