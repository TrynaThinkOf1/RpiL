from setuptools import setup, find_packages

# Define Raspberry Pi-specific dependencies
raspberry_pi_deps = [
    "RPi.GPIO",
    "Adafruit_DHT"
]

setup(
    name="RpiL",
    version="0.1.6",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pigpio",
        "gpiozero"
    ],
    extras_require={
        "rpi": raspberry_pi_deps  # Raspberry Pi-specific dependencies
    },
    description="Library for controlling Raspberry Pi hardware.",
    author="Zevi Berlin",
    author_email="zeviberlin@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
