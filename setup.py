from setuptools import setup, find_namespace_packages


with open('README.md', "r", encoding='UTF-8') as readMeFile:
    readMe = readMeFile.read()

requirements = ['aiohttp', 'typing', 'pydantic']

setup(
    name="pykeksikapi",
    version="0.21",
    author="unneccessaryss",

    description="This library is needed for working with api.keksik.io. It provides convenient tools for processing the API of this website.",
    long_description=readMe,
    long_description_content_type="text/markdown",
    url="https://github.com/unnecessaryss/pykeksikapi",

    packages=find_namespace_packages(),
    install_requires=requirements,
    python_requires=">=3.9"
)
