from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Alpha',
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='FEM2',
    version='0.0.1',
    description='FEM software',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author='Andreas Nyborg',
    author_email='andreas.uis@icloud.com',
    license='MIT',
    classifiers=classifiers,
    keywords='FEM',
    packages=find_packages(),
    install_requires=[]
)