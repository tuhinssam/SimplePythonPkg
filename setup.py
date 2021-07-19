from setuptools import setup, find_packages

def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="simplepythonpkg",
    version="0.0.1",
    description="simple python package",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/tuhinssam/simplepythonpkg",
    author="RobertoPrevato",
    author_email="tuhinssam@gmail.com",
    keywords="simple python package",
    license="MIT",
    packages=["simplepythonpkg"],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
