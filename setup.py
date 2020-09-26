import setuptools

with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='CineLedgerPy',
    version='0.1',
    author='Shrijit Basak',
    author_email='shrijitbasak@tutanota.com',
    description='a small cli tool to manage watchedlist and wishlist for movies and tvshows',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT LICENSE',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6'
)