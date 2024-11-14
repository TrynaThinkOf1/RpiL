from setuptools import setup, find_packages

# Define Raspberry Pi-specific dependencies
raspberry_pi_deps = [
    "RPi.GPIO",
    "Adafruit_DHT"
]

setup(
    name="RpiL",
    version="0.2.2",
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
    long_description="""
    RpiL is a Python library for controlling Raspberry Pi hardware.

    For detailed documentation, visit:
    `Documentation <https://rpil.readthedocs.io>`_

    The source code is available on GitHub:
    `GitHub Repository <https://github.com/TrynaThinkOf1/RpiL>`_
    """,
    long_description_content_type="text/x-rst",  # Use reStructuredText
    url="https://rpil.readthedocs.io",  # This sets the URL field for the package
)
