from setuptools import find_packages, setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(name="plex_schema",
      version="2.3.2",
      author="Alice",
      url="https://git.joshuaavalon.io/alice/plex-schema",
      description="Schema library for Plex",
      long_description=long_description,
      long_description_content_type="text/markdown",
      python_requires=">=3.7",
      packages=find_packages(exclude=["tests"]),
      install_requires=["marshmallow==3.0.0b13"],
      classifiers=(
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3 :: Only",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent"
      ))
