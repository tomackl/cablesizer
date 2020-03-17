from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cablesizer',
    version='2020.3.2',
    author='Tom Ackland',
    author_email='ackland.thomas@gmail.com',
    url='https://github.com/tomackl/cablesizer',
    description='Auto-unit electrical cables.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[

    ],
    # entry_points={
    #     'console_scripts': [
    #         'laundry = laundry.laundry_cli:cli',
    #     ],
    # },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: MacOS :: MacOS X',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
)