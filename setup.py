from setuptools import setup, find_packages

setup(
    name="pyutils",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.7",
    description="A lightweight Python utility library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Python Community",
    author_email="your-email@example.com",
    url="https://github.com/your-organization/PyUtils",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
