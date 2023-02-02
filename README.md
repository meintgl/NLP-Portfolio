# NLP-Portfolio

## Overview of NLP

This document serves as an introduction to NLP (Natural Language Processing). It defines key terms in NLP and explores various questions and applications.

You can read the [document here](https://github.com/meintgl/NLP-Portfolio/blob/main/Meinhard%20Benedict%20Capucao%20-%20NLP.pdf).

## Text Processing with Python

This program reads a .csv file line by line. The heading is ignored. Each line represents an employee that has the five
parameters:
    'Last', 'First', 'Middle Initial', 'ID', and 'Office Phone'.
Employees fall under the Person class with fields that correspond to the .csv file:
    'last', 'first', 'mi', id, and 'phone'

The program also processes and standardizes the text. It then saves the results it into a dictionary with 'ID' as the key.
The dictionary is saved as pickle file, then is printed using the display() method in the Person class.

You can see the [code here](https://github.com/meintgl/NLP-Portfolio/blob/main/Homework1_mdc190005/Homework_mdc190005.py).
