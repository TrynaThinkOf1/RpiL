from setuptools import setup, find_packages

setup(
    name="RpiL",  # Package name
    version="0.1.5",  # Version
    packages=find_packages(where="src"),  # Automatically find packages in 'src'
    package_dir={"": "src"},  # Tell setuptools where your package is
    install_requires=["RPi.GPIO", "Adafruit_DHT", "pigpio"],  # List of dependencies (only external packages)
    description="Library for controlling Raspberry Pi hardware. CAN ONLY BE INSTALLED ON RASPBERRY PI (due to dependancies).",
    author="Zevi Berlin",
    author_email="zeviberlin@gmail.com",
    license="MIT",  # Open source license
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
