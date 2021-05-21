import setuptools

def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='cricNotifier',
    version="1.0.3",
    description='Cross platform cricket score notifications',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/zweack/cricNotifier',
    author='Jeet Jain',
    author_email='jeet88833@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(include=['app', 'app.*']),
    include_package_data=True,
    install_requires=[
        'requests',
        'beautifulsoup4',
        'plyer',
        'PyYAML',
        'lxml'
    ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cricNotifier = app.main:main'
        ]
    }
)
