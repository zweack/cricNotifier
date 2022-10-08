# cricNotifier [![GitHub release (latest by date)](https://img.shields.io/github/v/release/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/releases) [![GitHub](https://img.shields.io/github/license/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/blob/main/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/commits/main) [![GitHub issues](https://img.shields.io/github/issues/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/issues) [![Build Status](https://img.shields.io/travis/zweack/cricNotifier?style=flat-square)](https://travis-ci.org/zweack/cricNotifier)

A CLI based application for real time cricket score updates. 


## Features
- Rich command line interface
- Choose among multiple live matches
- Cross platform notifications, works on Windows and Linux systems


## Installation 

Make sure you have python > 3.5 and pip installed, you can install it from [here](https://www.python.org/downloads/ "here")

For Linux systems, if you want to enable notifications, install dependencies for dbus-python as per specifications from your distro, e.g. for Ubuntu based distros, install following:
```
sudo apt-get -y install libglib2.0-dev libdbus-1-3 libdbus-1-dev
```
### Install using pip
```
pip install cricNotifier
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

## Examples
### Get list of currently available matches

![image](https://user-images.githubusercontent.com/15276039/194712651-3bcb3358-53b2-445c-8b3f-e59e072611b4.png)

### Select a match using ID

![image](https://user-images.githubusercontent.com/15276039/194712851-5c77d88a-ac4d-48d6-9d7e-07940074cb26.png)

### Get info about selected match

![image](https://user-images.githubusercontent.com/15276039/194713000-6c258b95-f044-42a4-9934-6b044e4b1cbf.png)

Alternatively you can pass an ID which will override the preserved ID using select (for current command only).

![image](https://user-images.githubusercontent.com/15276039/194713095-e7b9aebd-d65f-4a71-9e6e-6b44ddde8dfb.png)

### Get squads for the match

![image](https://user-images.githubusercontent.com/15276039/194713131-393c6651-d3e6-46e7-9fac-9c60ea70bcbf.png)

### Get latest score

![image](https://user-images.githubusercontent.com/15276039/194713334-3894e4b1-e64c-45e0-82f3-540cde082e59.png)

### Get text commentary of the match

![image](https://user-images.githubusercontent.com/15276039/194713428-1ac34fc1-1334-4662-82ea-91fb2b1bd04d.png)


## Contributing
This project welcomes contributions and suggestions. Please feel free to create a PR, report an issue or put up a feature request.

### Build cricNotifier locally
#### Clone the Repository
```
git clone https://github.com/zweack/cricNotifier.git && cd cricNotifier
```
#### Install Dependencies
Install [poetry](https://python-poetry.org/docs/#installation) for dependency management and run
```
poetry install
```
Alternatively, you can use pip 
```
pip install -r requirements.txt
```
You are ready to roll!

## License
cricNotifier is licensed under the [MIT License](https://github.com/zweack/cricNotifier/blob/dev/LICENSE).
