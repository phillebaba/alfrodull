from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='alfrodull',
    version='0.1.0',
    author='Philip Laine',
    author_email='philip.laine@gmail.com',
    description='Alfrodull is a utility that controls lights based on the a computers events',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/phillebaba/alfrodull',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    entry_points='''
        [console_scripts]
        alfrodull=alfrodull.main:main
    '''
)
