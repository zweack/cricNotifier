# cricNotifier [![GitHub release (latest by date)](https://img.shields.io/github/v/release/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/releases) [![GitHub](https://img.shields.io/github/license/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/blob/main/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/commits/main) [![GitHub issues](https://img.shields.io/github/issues/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/issues) [![Build Status](https://img.shields.io/travis/zweack/cricNotifier?style=flat-square)](https://travis-ci.org/zweack/cricNotifier)

A python application for real time cricket match notifications on Windows and Linux


## Features
- Rich command line UI
- Choose among multiple live matches
- Cross platform, works on Windows and Linux systems


## Installation 

Make sure you have python > 3.5 and pip installed, you can install it from [here](https://www.python.org/downloads/ "here")

For Linux systems, install dependencies for dbus-python as per specifications from your distro, e.g. for Ubuntu based distros, install following:
```
sudo apt-get -y install libglib2.0-dev libdbus-1-3 libdbus-1-dev
```
### Install using pip
```
pip3 install cricNotifier
```
### Build and Install
#### Clone the Repository

```
git clone https://github.com/zweack/cricNotifier.git && cd cricNotifier
```

#### Install Dependencies
```
pip install -r requirements.txt
```

## Running the Application 

Run following command on your terminal
```
cricNotifier [argument]
```
Arguments:
```
commentary        Fetch commentary for last few overs.
info              Fetch info for a match.
list              List all available matches.
score             Fetch latest score for a match.
select            Select a match with an ID.
````
## Contributing
This project welcomes contributions and suggestions. Please feel free to create a PR, report an issue or put up a feature request.

## License
cricNotifier is licensed under the [MIT License](https://github.com/zweack/cricNotifier/blob/dev/LICENSE).