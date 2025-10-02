from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'A Python package to create and visualize atomic orbitals and more'
LONG_DESCRIPTION = 'A Python package to create and visualize atomic orbitals and more'

# Setting up
setup(
    name="atomictools",
    version=VERSION,
    author="Jaime Rosado, Villar Alejandro, Iris Madrigal",
    author_email="jaime_ros@fis.ucm.es",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=['scipy', 'numpy', 'matplotlib', 'plotly', 'IPython', 'ipywidgets', 'nbformat'],
    keywords=['python', 'physics', 'numeric', 'graphing'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "Framework :: Jupyter",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

