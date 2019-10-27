from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="moviefetcher",
    version="2.1.0",
    description="This Library allows Developers to Get all top 100 Movies with Rating in JSON and CSV File",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/weatherUSA",
    author="Soumil Nitin Shah",
    author_email="soushah@my.bridgeport.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["moviefetcher"],
    include_package_data=True,
    install_requires=["requests","pandas==0.24.0", ""]
)