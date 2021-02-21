# cricNotifier ![version](https://img.shields.io/badge/version-1.0.0.0-brightgreen.svg) [![Build Status](https://travis-ci.org/zweack/cricNotifier.svg?branch=main)](https://travis-ci.org/zweack/cricNotifier)

A python application for real time cricket match notifications on Windows and Linux

### Menu for available matches
![alt text](https://github.com/zweack/cricNotifier/blob/main/static/screenshots/menu.png?raw=true)

### Notifications on KDE Neon 5.20
![alt text](https://github.com/zweack/cricNotifier/blob/main/static/screenshots/linux.png?raw=true)

### Notifications on Windows 10 20H2
![alt text](https://github.com/zweack/cricNotifier/blob/main/static/screenshots/windows.png?raw=true)


### Features
- Rich command line UI
- Choose among multiple live matches
- Cross platform, works on Windows and Linux systems
- Rich logging configuration
- User defined notification timeout


### Installation 

Make sure you have python 3 installed, you can install it from [here](https://www.python.org/downloads/ "here")
#### Clone the Repository

```
git clone https://github.com/zweack/cricNotifier.git && cd cricNotifier
```

#### For Windows:
```
pip install -r requirements/requirements_win.txt
```

#### For Linux:
```
pip install -r requirements/requirements_other.txt
```

### Running the Application 

#### For Windows:
```
python app/main.py
```

#### For Linux:
```
python3 app/main.py
```

### Logging Configuration
Coming soon!
