# command-line-game

A simple python RPG-style game that mainly relies on decisions being typed out in the command line. Also features some GUI elements.

## Game Overview

Simply follow the directions on screen to make decisions and survive. The game should be reasonably well explained during your playthrough.

## Installation Instructions

### Extra step for Windows Users

The default windows command prompt doesn't support text colours, which are somewhat important. Note that you can execute the game in the standard command prompt without crashes, but some text will have strange formatting and no colour.

To get around this, simply install the [windows terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701#activetab=pivot:overviewtab) from the Microsoft Store and run all commands from there instead.

### Installing Python

To run the game, you need python 3 (**not 2**) installed. Simply download the installer for your OS from python.org. Note that most instructions here are for Mac and Windows - if you are using linux I feel safe in assuming you can figure it out.

https://www.python.org/downloads/

### Installing Python Modules

The game is reliant on several third-party python modules. These are completely safe to install; simply run the following lines of code one after another in terminal.
```
python3 -m pip install -U pygame --user
python3 -m pip install colorama
python3 -m pip install -U deep_translator
```

### Running the Game

Download the .zip from the releases tab, and unzip the folder to a convenient location.
The unzipped folder, `command-line-game`, will contain another folder inside it, also called `command-line-game` . This is the folder you need. Ignore anything/everything else.

In the terminal or command prompt, type `python3` followed by a space, and then drag the `command-line-game` folder into the terminal. It should look something like the examples below.

#### Mac Example

`python3 /Users/peterthesalmon/Desktop/command-line-game`

#### Windows Example

`python3 C:\Users\peterthesalmon\Downloads\command-line-game\command-line-game`

Simply hit enter and the game will begin.
