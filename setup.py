# Import the version string from the Plugthon module
from Plugthon import __version__

# Import necessary functions from setuptools
from setuptools import setup, find_packages

# Open the README file for reading
with open("README.md", "r") as fh:
    # Read the contents of the README file, which will be used as the long description
    long_description = fh.read()

# Call the setup function to configure the package
setup(
    # Set the package name
    name = "Plugthon",

    # Set the package version, using the imported version string
    version = __version__,

    # Automatically find all packages within the project
    packages = find_packages(),

    # Set the author's name
    author = "iniridwanul",

    # Set the author's email address
    author_email = "iniridwanul@gmail.com",

    # Set a short description of the package
    description = "Plugthon is a developer-friendly library for building modular and scalable Telegram bots.",

    # Set the long description, using the contents of the README file
    long_description = long_description,

    # Specify the format of the long description (Markdown)
    long_description_content_type = "text/markdown",

    # Set the URL of the project's repository
    url = "https://github.com/Plugthon/Plugthon",

    # Set the license of the package (AGPL)
    license = "AGPL",

    # Set a list of classifiers to categorize the package
    classifiers = [
        # Indicate that the package is written in Python 3
        "Programming Language :: Python :: 3",

        # Indicate that the package is operating system independent
        "Operating System :: OS Independent"
    ],

    # Set a list of keywords to help users find the package
    keywords = ["Plugthon", "Python", "Telethon", "Telegram bots", "Userbot", "Telegram"],

    # Specify the minimum Python version required
    python_requires = ">=3.6",

    # Specify the package's dependencies (Telethon)
    install_requires = ["Telethon"]
)