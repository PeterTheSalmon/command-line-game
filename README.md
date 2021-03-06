# command-line-game

A simple python choose-your-own-adventure-style game that mainly relies on decisions being typed out in the command line. Also features some GUI elements.

<img width="1440" alt="Screen Shot 2021-07-17 at 3 02 35 PM" src="https://user-images.githubusercontent.com/87033324/126050234-d7860385-9edf-421c-a9c1-e19eeb8ed103.png">


## Game Overview

Simply follow the directions on screen to make decisions and survive. The game is currently in a _very_ beta state and most certainly contains copious amounts of bugs, glitches, and broken features. See below for where you can report said issues.

## Installation Instructions

### Extra step for Windows Users

The default windows command prompt doesn't support text colours, which are somewhat important. Note that you _technically_ can execute the game in the standard command prompt without crashes, but some text will have strange formatting and no colour.

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

## Running the Game

First, download the latest .zip from the [releases](https://github.com/PeterTheSalmon/command-line-game/releases) tab, and unzip the folder to a convenient location.

### Mac Instructions

In the terminal or command prompt, type `python3` followed by a space, and then drag the unzipped `command-line-game` folder into the terminal. It should look something like the example below.

`python3 /Users/peterthesalmon/Desktop/command-line-game`

Simply hit enter and the game will begin.

### Windows Intructions

The unzipped folder, `command-line-game`, will contain another folder inside it, also called `command-line-game` . This is the folder you need. Ignore anything/everything else.

In the terminal or command prompt, type `python3` followed by a space, and then drag the `command-line-game` folder into the terminal. It should look something like the example below.

`python3 C:\Users\peterthesalmon\Downloads\command-line-game\command-line-game`

Simply hit enter and the game will begin.

## Bugs, Crashes, Questions, Support, Guides

All questions, bug reports, and crashes can be addresed in the Discord Server (coming soon)!
