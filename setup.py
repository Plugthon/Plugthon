from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "Plugthon",
    version = "0.2.0",
    packages = find_packages(),
    author = "iniridwanul",
    author_email = "iniridwanul@gmail.com",
    description = "Plugthon is a developer-friendly library for building modular and scalable Telegram bots.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Plugthon/Plugthon",
    license = "AGPL",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    keywords = ["Plugthon", "Python", "Telethon", "Telegram bots", "Userbot", "Telegram"],
    python_requires = ">=3.6",
    install_requires = ["Telethon"]
)