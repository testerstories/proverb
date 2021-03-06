from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='proverb',
    version='0.1',
    description='Statement to Live By',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Linguistic',
      ],
    keywords='bible proverbs',
    url='http://github.com/testerstories/proverb',
    author='Jeff Nyman',
    author_email='jeffnyman@gmail.com',
    license='MIT',
    packages=['proverb'],
    install_requires=['markdown'],
    tests_require=['nose'],
    test_suite='nose.collector',
    entry_points = {
        'console_scripts': ['proverb-saying=proverb.command_line:main'],
    },
    include_package_data=True,
    zip_safe=False
)
