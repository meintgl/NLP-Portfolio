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

## Word Guessing Game

This program is a word guessing game.
It begins by reading a .txt file then reads it as raw text. It calculates the lexical diversity of the tokenized text,
     then outputs it. Lexical diversity indicates uniqueness of a text.
More details can be found in the comments of the [code here](https://github.com/meintgl/NLP-Portfolio/blob/main/Homework%202_mdc190005/Homework2_mdc190005_2.py).

## Wordnet

WordNet is a hierarchal collection that contains the following: nouns, verbs, adjectives, and adverbs. It al contains glosses, which are short definitions, synsets, which are synonym sets, use examples, and relations to other words.

This program aims to demonstrate the use of WordNet and SentiWordNet.

You can see the [PDF here](https://github.com/meintgl/NLP-Portfolio/blob/main/MeinhardCapucao_WordNet.ipynb%20-%20Colaboratory.pdf)
and the [ipynb format here](https://github.com/meintgl/NLP-Portfolio/blob/main/MeinhardCapucao_WordNet.ipynb).
