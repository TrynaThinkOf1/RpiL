from setuptools import setup, find_packages

setup(
    name="RpiL",  # Package name
    version="0.1.0",  # Version
    packages=find_packages(where="src"),  # Automatically find packages in 'src'
    package_dir={"": "src"},  # Tell setuptools where your package is
    install_requires=["RPi.GPIO"],  # List of dependencies
    description="Library for controlling Raspberry Pi hardware.",
    author="Zevi Berlin",
    author_email="zeviberlin@gmail.com",
    license="MIT",  # Open source license
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
