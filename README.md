# Loose Change Calculator
> A program that calculates the total change the user has in GBP.

## General info
This program was written to make summing large amounts of change faster and easier.


<!-- Screenshots -->
## Screenshots
| On start-up | After calculating |
| --- | --- |
| ![LCC](https://user-images.githubusercontent.com/44094740/98406966-c2b00280-2066-11eb-8773-5f855aa8fdbf.png) | ![LCC filled in](https://user-images.githubusercontent.com/44094740/98407627-e4f65000-2067-11eb-89a2-cabf69c21466.png) |


<!-- How to install the program -->
## Installation (on Windows)
From the command line, run the following set of instructions:
1. `git clone https://github.com/Jamnic98/loose-change-calculator.git`
2. `cd ./loose-change-calculator`
3. `python -m venv ./`
4. `cd Scripts && activate`
5. `cd ../ && python loose_change_calc.py`

Remember to deactivate the virtual environment when finished by running the command:
`cd Scripts && deactivate`


<!-- Usage examples -->
## Usage
To use the app, type in the number of each denomination of coin and then press the button labeled 'CALCULATE' to get the total.
If there are zero of any coin, the amount does not have to be input for the program to work. Also, the tab key can be used to switch between inputs.


<!-- Technologies used in development -->
## Built with
* Python 3.8
* Tkinter 8.6
