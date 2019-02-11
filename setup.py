
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ivrc2country",
    version="0.0.1",
    author="Christoph Becker",
    author_email="mail@ch-becker.de",
    description="Converts international vehicle license codes to 2-letter ISO3166 country codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuergeist/ivrc2country",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
