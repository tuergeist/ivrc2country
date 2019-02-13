
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ivrc2country",
    version="0.1.2",
    author="Christoph Becker",
    author_email="tuergeist@gmail.com",
    description="Converts international vehicle license codes to 3-letter ISO3166-1 alpha-3 country codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuergeist/ivrc2country",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite="tests",
)
