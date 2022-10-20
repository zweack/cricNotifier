# cricNotifier [![GitHub release (latest by date)](https://img.shields.io/github/v/release/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/releases) [![GitHub](https://img.shields.io/github/license/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/blob/main/LICENSE) [![GitHub last commit](https://img.shields.io/github/last-commit/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/commits/main) [![GitHub issues](https://img.shields.io/github/issues/zweack/cricNotifier?style=flat-square)](https://github.com/zweack/cricNotifier/issues) [![Build](https://github.com/zweack/cricNotifier/actions/workflows/python-package.yml/badge.svg?branch=dev)](https://github.com/zweack/cricNotifier/actions/workflows/python-package.yml)

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
list              List all available matches.
select            Select a match with an ID.
info              Fetch info for a match.
squad             Fetch players for each team in the match.
score             Fetch latest score for a match.
commentary        Fetch commentary for last few overs.
````

## Examples
#### Get list of currently available matches

```
$ cricnotifier list
┌────┬─────────────────────────────────────────────────────────────────────────┐
│  1 │ New Zealand v Pakistan                                                  │
├────┼─────────────────────────────────────────────────────────────────────────┤
│  2 │ Madhya Pradesh v Uttarakhand                                            │
├────┼─────────────────────────────────────────────────────────────────────────┤
│  3 │ Punjab v Tripura                                                        │
├────┼─────────────────────────────────────────────────────────────────────────┤
│  4 │ Karnataka v Meghalaya                                                   │
├────┼─────────────────────────────────────────────────────────────────────────┤
│  5 │ Nepal Police Club Women v Lumbini Province Women                        │
├────┼─────────────────────────────────────────────────────────────────────────┤
│  6 │ Sydney Thunder Women v Hobart Hurricanes Women                          │
├────┼─────────────────────────────────────────────────────────────────────────┤
│  7 │ BandeAmir Region v Speen Ghar Region                                    │
├────┼─────────────────────────────────────────────────────────────────────────┤
│  8 │ Boost Region v Mis Ainak Region                                         │
├────┼─────────────────────────────────────────────────────────────────────────┤
│  9 │ Burgher Recreation Club v Sebastianites Cricket and Athletic Club       │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 10 │ Galle Cricket Club v Moors Sports Club                                  │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 11 │ Kalutara Town Club v Ragama Cricket Club                                │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 12 │ Kandy Customs Cricket Club v Sinhalese Sports Club                      │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 13 │ Kurunegala Youth Cricket Club v Colts Cricket Club                      │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 14 │ Police Sports Club v Lankan Cricket Club                                │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 15 │ Ace Capital Cricket Club v Badureliya Sports Club                       │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 16 │ Bloomfield Cricket and Athletic Club v Tamil Union Cricket and Athletic │
│    │ Club                                                                    │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 17 │ Chilaw Marians Cricket Club v Sri Lanka Air Force Sports Club           │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 18 │ Negombo Cricket Club v Panadura Sports Club                             │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 19 │ Saracens Sports Club v Nugegoda Sports Welfare Club                     │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 20 │ Sri Lanka Navy Sports Club v Sri Lanka Army Sports Club                 │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 21 │ Assam v Mumbai                                                          │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 22 │ Delhi v Uttar Pradesh                                                   │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 23 │ Haryana v Kerala                                                        │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 24 │ Bihar v Himachal Pradesh                                                │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 25 │ Nagaland v Saurashtra                                                   │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 26 │ Chandigarh v Jharkhand                                                  │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 27 │ Sikkim v Tamil Nadu                                                     │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 28 │ Karnali Province Women v Province Number Women                          │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 29 │ Mizoram v Vidarbha                                                      │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 30 │ Manipur v Puducherry                                                    │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 31 │ Arunachal Pradesh v Services                                            │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 32 │ Australia v England                                                     │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 33 │ Railways v Rajasthan                                                    │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 34 │ Goa v Hyderabad India                                                   │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 35 │ Jammu Kashmir v Maharashtra                                             │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 36 │ Baroda v Gujarat                                                        │
├────┼─────────────────────────────────────────────────────────────────────────┤
│ 37 │ Bengal v Odisha                                                         │
└────┴─────────────────────────────────────────────────────────────────────────┘

Use select command to select a match.
e.g. for Bengal v Odisha, use
cricnotifier select 37
```

Too many matches? Filter them using `--filter`
```
$ cricnotifier list --filter aus
┌───┬─────────────────────┐
│ 1 │ Australia v England │
└───┴─────────────────────┘

Use select command to select a match.
e.g. for Australia v England , use
cricnotifier select 1
```

#### Select a match using ID
This will cache ID of the match so that you dont have to provide match ID with every command.
Alternatively you can always pass `--id` with any command which will have higher precedence.   

```
$ cricnotifier select 32
[Info] You have selected: Australia vs England
```

#### Get info about selected match
```
$ cricnotifier info
┌─────────────┬─────────────────────────────────────────────────────────────┐
│ Description │ England tour of Australia, 3rd T20I: Australia v England at │
│             │ Canberra, Oct 14, 2022                                      │
├─────────────┼─────────────────────────────────────────────────────────────┤
│ Series      │ England in Australia T20I Series                            │
├─────────────┼─────────────────────────────────────────────────────────────┤
│ Venue       │ Manuka Oval, Canberra                                       │
├─────────────┼─────────────────────────────────────────────────────────────┤
│ Summary     │ England 43/1 (5.2 ov, DJ Malan 16*, JC Buttler 20*, PJ      │
│             │ Cummins 0/14)                                               │
├─────────────┼─────────────────────────────────────────────────────────────┤
│ Toss        │ Australia won the toss and choose to field first.           │
└─────────────┴─────────────────────────────────────────────────────────────┘
```

Alternatively you can pass an ID which will override the preserved ID using select command.
```
$ cricnotifier info --id 28
┌─────────────┬──────────────────────────────────────────────────────────────┐
│ Description │ CAN National Women's Cricket Tournament, 12th Match, Group   │
│             │ B: Karnali Province Women v Province Number 1 Women at       │
│             │ Pokhara, Oct 14, 2022                                        │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Series      │ CAN National Women's Cricket Tournament                      │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Venue       │ Pokhara Rangasala                                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Summary     │ Karnali Province Women 53 (16.1 ov, AT Chetri 0*, A Khadiya  │
│             │ 3/6) - Innings break                                         │
├─────────────┼──────────────────────────────────────────────────────────────┤
│ Toss        │ Karnali Province Women won the toss and choose to bat first. │
└─────────────┴──────────────────────────────────────────────────────────────┘
```

#### Get squads for the match

```
$ cricnotifier squad
┌───────────────────┬──────────────────────┐
│ Australia         │ England              │
├───────────────────┼──────────────────────┤
│ Aaron Finch (c)   │ Jos Buttler (c) (wk) │
├───────────────────┼──────────────────────┤
│ Steven Smith      │ Alex Hales           │
├───────────────────┼──────────────────────┤
│ Mitchell Marsh    │ Dawid Malan          │
├───────────────────┼──────────────────────┤
│ Glenn Maxwell     │ Ben Stokes           │
├───────────────────┼──────────────────────┤
│ Marcus Stoinis    │ Harry Brook          │
├───────────────────┼──────────────────────┤
│ Tim David         │ Moeen Ali            │
├───────────────────┼──────────────────────┤
│ Matthew Wade (wk) │ Chris Woakes         │
├───────────────────┼──────────────────────┤
│ Pat Cummins       │ David Willey         │
├───────────────────┼──────────────────────┤
│ Mitchell Starc    │ Adil Rashid          │
├───────────────────┼──────────────────────┤
│ Adam Zampa        │ Mark Wood            │
├───────────────────┼──────────────────────┤
│ Josh Hazlewood    │ Reece Topley         │
└───────────────────┴──────────────────────┘
```

#### Get latest score

```
$ cricnotifier score --id 32
┌─────────────────────────────────────────────┐
│ England vs Australia                        │
├─────────────────────────────────────────────┤
│ England: 26/1                               │
│ Overs: 3.5                                  │
│ Dawid Malan 10(8)* Jos Buttler 10(13)       │
│ Australia won the toss and elected to field │
└─────────────────────────────────────────────┘
```

### Get text commentary of the match

```
$ cricnotifier commentary --id 32
[3.2]: Hazlewood to Buttler, 1 RUN
Good length, top of off, he defends to the right of cover and pinches a single.

[3.1]: Hazlewood to Buttler, FOUR
Lofted inside out over cover! Superb shot. Not a half volley, he opened up the chest and sliced 
it over cover with great timing.

[2.6]: Cummins to Malan, NO RUN
135kph, he plays and misses trying to glide one with the angle to third man.

[2.5]: Cummins to Malan, FOUR
Pulled over midwicket! A bouncer that got high outside off but he was equal to it, high hands 
and he pulled with ease over the infield.

[2.4]: Cummins to Malan, NO RUN
136kph, short and wide, he cracks a cut with outstanding timing straight to Maxwell at point.

[2.3]: Cummins to Malan, NO RUN
136kph, good length top of off, he defends from the crease.

[2.2]: Cummins to Malan, FOUR
Pinged off the pads! Half volley on middle, no swing and Malan clips this beautifully through 
midwicket. Wonderful timing.

[2.1]: Cummins to Buttler, 1 RUN
131kph, back of a length, nipping back, thick inside edge onto pad and it balloons into the leg 
side safely for one.

[1.6]: Hazlewood to Buttler, 1 RUN
138kph, fuller length, angled into off, he defends pushing it to mid off and runs with the shot.

[1.5]: Hazlewood to Buttler, NO RUN
138kph, good length, angled into off, he defends getting a thickish inside edge to mid on, they 
look at a single but Buttler sends
him back.

[1.4]: Hazlewood to Buttler, NO RUN
137kph, good length top of off, he defends from the crease.

[1.3]: Hazlewood to Malan, 1 RUN
143kph, good length, he defends firmly straight of mid off for a single.

[1.2]: Hazlewood to Hales, OUT
Nicked straight to slip! A beauty! Back of a length angled into middle, it leaves him as he's 
caught on the crease defending, gets a thick edge and it floats waist high to Finch who pouches 
it. Test match dismissal that. Amazing length and some late movement..

[1.1]: Hazlewood to Hales, NO RUN
136kph, good length, fifth stump channel, he leaves watchfully as it shapes away.
```


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
