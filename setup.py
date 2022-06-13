from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python implementation of the quantum optimal control GOAT-algorithm'
LONG_DESCRIPTION = 'A package that allows you to use the GOAT-algorithm for the implementation of unitary gates' \
                   'in quantum systems.'

# Setting up
setup(
    name="goat-qcontrol-approx",
    version=VERSION,
    author="Markus Plautz",
    author_email="<markus.plautz@gmx.at>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url='https://github.com/pmarkus-github/goat-qcontrol',
    packages=find_packages(),
    install_requires=['numpy', 'time', 'scipy.integrate.solve_ivp', 'scipy.optimize'],
    keywords=['python', 'quantum-control', 'goat', 'quantum-gates', 'quantum-computer'],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)