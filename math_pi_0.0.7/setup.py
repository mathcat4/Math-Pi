from setuptools import *
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="math_pi",
    version="0.0.7",
    author="Tanmay Earappa",
    author_email="Tams.Mathe@gmail.com",
    description="Has Up to 1 Million digits of pi!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = "MIT",
    packages= ["math_pi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url = "https://github.com/Tams-Tams/pi/blob/master/math_pi_0.0.7",
    install_requires = ["pi-1mp"],
    zip_safe = False,
)
