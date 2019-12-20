from setuptools import find_packages, setup

setup(
    name="dht22-python",
    version="0.0.1",
    description="Collector of data from dht22 sensor",
    author="Jesse Collis",
    author_email="jesse@jcmultimedia.com.au",
    url="https://github.com/jessedc/dht22-python",
    packages=find_packages(exclude=["*.tests"]),
    test_suite="dht22.tests",
    install_requires=[
        "influxdb>=5.2",
        "Adafruit-DHT>=1.4"
    ],
    setup_requires=[
    ],
    tests_require=[
    ],
    entry_points={
        "console_scripts": [
            "dht22 = dht22.__main__:main",
        ],
    },
)
