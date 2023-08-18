from setuptools import setup, find_packages

setup(
    name='abkpyutils',
    version='0.1.0',
    description='A collection of utility functions by Ali Burak Kulakli',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ali Burak Kulakli',
    author_email='kulakli@gmail.com',
    url='https://github.com/abkulakli/abkpyutils',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
