from setuptools import find_packages, setup

setup(name="plex_schema",
      version="1.0.2",
      author="Alice Media",
      url="https://git.joshuaavalon.io/alice/plex-schema",
      python_requires=">=3.7",
      packages=find_packages(),
      install_requires=["marshmallow==3.0.0b12"])
