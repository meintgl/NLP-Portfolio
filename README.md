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

## Sentence Parsing

This document explores three methods of sentence parsing: PSG Trees, Dependency Parses, and SRL Parses.
Check it out, it comes with the use of a unique sentence!

You can see the [PDF here](https://github.com/meintgl/NLP-Portfolio/blob/main/Capucao_Meinhard_Portfolio%20Assignment_%20Sentence%20Parsing.pdf).

## N Grams

N Grams is a text window that slides N Words over time. This project creates bigram and unigram dictionaries for English, French, and Italian texts.
A dictionary is created where the key is the unigram or bigram text, and the value is the count of that unigram or bigram in the data. For the test data, calculate probabilities are calculated for  each language and compare against the true labels.

The first program creates the unigram and bigram dictionaries. 
You can see the [Python Code here](https://github.com/meintgl/NLP-Portfolio/blob/main/main.py)

The second program calculates the probability for lines of text of the three langauges, and returns the most likely language for the text to be
You can see the [Python Code here](https://github.com/meintgl/NLP-Portfolio/blob/main/calculate.py)

The narrative can be [read here](https://github.com/meintgl/NLP-Portfolio/blob/main/N-GramsNarrative.pdf)

## Webcrawler Project - Hayao Miyazaki

Simply put, web crawlers browse the web. With libraries like BeautifulSoup to extract data from the web, and the concept of tf-idf's to output important terms from extracted url's, this project gets facts from 10 important terms retrieved from 20 url's that come from Hayao Miyazaki's Wikipedia page. These terms are generated based on metrics such as tf-idf scores. The program importantterms.py pickles facts to a dictionary and a text file.


The readme can be [found here](https://github.com/meintgl/NLP-Portfolio/blob/main/Webcrawler_mdc190005/readme.md)
Here are the two programs, [webcrawl.py](https://github.com/meintgl/NLP-Portfolio/tree/main/Webcrawler_mdc190005) and [importantterms.py](https://github.com/meintgl/NLP-Portfolio/blob/main/Webcrawler_mdc190005/importantterms.py).

The list of facts can be [found here](https://github.com/meintgl/NLP-Portfolio/blob/main/Webcrawler_mdc190005/facts.txt).


