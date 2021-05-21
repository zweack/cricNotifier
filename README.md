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
- Popular tweets related to selected match [coming soon]


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
Or install the package
```
python setup.py install
```

#### For Linux:
```
pip install -r requirements/requirements_other.txt
```
Or install the package
```
sudo python3 setup.py install
```

### Running the Application 

Run the application directly

#### For Windows:
```
python app/main.py
```

#### For Linux:
```
python3 app/main.py
```
Or run below command if you have installed it as package
```
cricNotifier
```

### Logging Configuration
Coming soon!

### Match Tweets
Coming soon!
