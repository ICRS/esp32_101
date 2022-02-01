from setuptools import find_packages, setup
import sdist_upip

setup(    
    name='drivelib',
    packages=find_packages(include=['drive']),
    version='0.1.0',
    description='esp32 micropython drivebase library',
    author='Haotian',
    cmdclass={'sdist': sdist_upip.sdist}

    )
