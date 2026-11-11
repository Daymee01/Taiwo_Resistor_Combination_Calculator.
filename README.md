# Resistor Combination Calculator

## What it does
This program asks how many resistors you have and the value of each one in ohms. It then calculates and prints the total resistance in series and in parallel. It also checks for wrong input, such as letters or values of 0 or less.

## How to run it
Install Python 3, then run: python resistor_calculator.py

## Sample output
=== Resistor Combination Calculator ===
How many resistors do you have? 3
Enter resistor 1 value (ohms): abc
Invalid input. Please type a number (e.g. 10 or 4.7).
Enter resistor 1 value (ohms): 100
Enter resistor 2 value (ohms): -5
The value must be greater than 0.
Enter resistor 2 value (ohms): 220
Enter resistor 3 value (ohms): 330

--- Results ---
Resistors (ohms): [100.0, 220.0, 330.0]
Total resistance in series:   650.00 ohms
Total resistance in parallel: 56.90 ohms

Calculate current for a supply voltage? (y/n): y
Enter supply voltage (volts): 12
Series current:   0.018 A
Parallel current: 0.211 A
[Program finished]

## My own twist
After the results, the program can calculate the current in both circuits from a supply voltage you enter, using Ohm's law (I = V / R).

## What I learned
I learned that a program must handle wrong input without crashing. I also learned how functions and loops make code shorter and easier to reuse.

## Author
Osuolale Taiwo Emmanuel, ND2 Mechatronics Engineering, YabaTech

