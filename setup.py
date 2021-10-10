import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='cricNotifier',
    version="2.0.1",
    description='Cross platform cricket score notifications',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/zweack/cricNotifier',
    author='Jeet Jain',
    author_email='jeet88833@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(
        include=['cricNotifier', 'utils', 'cricNotifier.*']),
    include_package_data=True,
    install_requires=[
        'requests',
        'beautifulsoup4',
        'plyer',
        'PyYAML',
        'lxml',
        'coloredlogs',
        'dbus-python; sys_platform == "linux"',
        'windows-curses; sys_platform == "Windows"',
        'win10toast; sys_platform == "Windows"'
    ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cricNotifier = cricNotifier.main:main'
        ]
    }
)

