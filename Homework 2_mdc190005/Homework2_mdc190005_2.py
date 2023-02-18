# mdc190005 / Homework 2 / 2.17.23
# Meinhard Benedict Capucao
"""
This program is a word guessing game.
It begins by reading a .txt file then reads it as raw text. It calculates the lexical diversity of the tokenized text,
     then outputs it. Lexical diversity indicates uniqueness of a text.
There are four functions (explained in greater detail later):

"""
import re
import sys
import pathlib
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import random


"""
    def print_text(text):
    Prints text
    Args:
        text: a string of text
    Returns:
        n/a
    Example:
        >>> (input): text: "Hello"
        >>>  (output): hello
"""

def print_text(text):
    print(text)

"""
    def tokenize(text):

    Takes text and turns it all into lowercase.
    Then, splits up a large body of text into smaller ones separated by text.
    Args:
         text: a string of text
     Returns:
         tokens: a list of strings with individual words or symbols, which is the tokenized text.
     Example:
         >>> (input): text: "The quick brown fox, jumped over the lazy dog."
        >>>  (output): 
                      tokens: ['the', 'quick', 'brown', 'fox', ',', 'jumped', 'over', 'the', 'lazy', 'dog']
"""

def tokenize(text):
    lowercase = text.lower()
    tokens = nltk.word_tokenize(lowercase)
    return tokens

"""
    def preprocess_text(tokens):

    Processes tokens by getting ones that are alphabetical, not a stop word, and has a length greater than 5.
    Step by step, prints various data about the text fed into it.
    Prints, in order:
        number of unique words in text
        first 10 unique words in text
        first 10 unique lemmas in text
        first 10 unique lemmas with tag in text
        total number of initial tokens
        total number of lemmas that are nouns
    
    Args:
         tokens: a list of strings, each one being tokens
     Returns:
        processed_tokens: a list of processed tokens with specifications stated above.
        nouns: a dictionary of noun lemmas, with key (noun): value (noun counts)
     Example:
         >>> (input): text: "Processes tokens by getting ones that are alphabetical, not a stop word, and has a 
              length greater than 5"
        >>>  (output): 
                      processed_tokens: ['processes', 'tokens', 'getting', 'alphabetical', 'length', 'greater']
                      nouns: ['processes': 1, 'tokens': 1, 'length': 1, 
"""

def preprocess_text(tokens):
    # processes tokens by getting ones that are alphabetical, not a stop word, and has a length greater than 5.
    processed_tokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english') and len(t) > 5]

    #STEP 1: processes tokens by getting ones that are alphabetical, not a stop word, and has a length greater than 5.
    print("\nThe number of unique important words in text:", len(processed_tokens))
    print("The first 10 unique important words in text:", processed_tokens[:10])

    # STEP 2: lemmatize the tokens, use set to make a list of unique lemmas
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in processed_tokens]
    lemmas_unique = list(set(lemmas))
    print("\nThe number of unique lemmas in text: ", len(lemmas_unique))

    # STEP 3: pos tag the unique lemmas, print the first 20 tagged
    tags = nltk.pos_tag(lemmas_unique)
    print("The first 10 unique lemmas with tags in text:", tags[:10])

    # STEP 4: Create a list of only those lemmas that are nouns
    nouns = [lemma for lemma, tag in tags if tag.startswith('NN')]
    print("\nNumber of tokens: ", len(tokens))
    print("Number of nouns: ", len(nouns))

    return processed_tokens, nouns


"""
    def guessing_game(words):
    
    Sets up a guessing game for the user to play with in a terminal!
    Prints, in order: (TAKEN DIRECTLY FROM ASSIGNMENT SPECIFICATIONS)
        give the user 5 points to start with; the game ends when their total score is negative, or
            they guess ‘!’ as a letter
        randomly choose one of the 50 words in the top 50 list (See the random numbers
            notebook in the Xtras folder of the GitHub)
        output to console an “underscore space” for each letter in the word
            ask the user for a letter
        if the letter is in the word, print ‘Right!’, fill in all matching letter _ with the letter and
            add 1 point to their score
        if the letter is not in the word, subtract 1 from their score, print ‘Sorry, guess again’
        guessing for a word ends if the user guesses the word or has a negative score
         keep a cumulative total score and end the game if it is negative (or the user entered ‘!’)
        for a guess right or wrong, give user feedback on their score for this word after each guess
        
    Args:
         words: a processed string of 50 most common nouns given from a text.
     Returns:
        N/A (only outputs a guessing game)
     Example:
         >>> (input): text: "muscle: 75, contraction: 70, ventricular: 54, coronary: 48"
        >>>  (sample output): 
                      _ _ _ _ _ _
            Guess a letter: m
            Right! Score is 6
            m _ _ _ _ _
            
            Guess a letter: f
            
            Sorry, guess again. Score is 5
            m _ _ _ _ _
            
 
           Right! Score is 3
           m u s c l e
           You solved it!

"""

def guessing_game(words):
    print("Let's play a word guessing game!")
    user_score = 5            # sets user score to 5.

    while True:
        word_to_guess = random.choice(words)            # chooses a random word out of the 50 to be the one to guessed
        current_word = ["_"] * len(word_to_guess)       # sets current word to only underscores
        print(" ".join(current_word))
        guessed = set()                                 # makes a tuple named set to store guessed letters
        while True:
            guess = input("Guess a letter: ")
            if guess == "!":                            # exits if ! is guessed
                print("Your final score is", user_score)
                return
            if guess in guessed:                         # if user inputs duplicate letter
                print("You already guessed that letter. Try again.")
                continue
            guessed.add(guess)                          # adds guessed letter to guess
            if guess in word_to_guess:                  # if the guessed letter is in the word, add a score then
                user_score += 1                             # prints newly updated current word.
                print("Right! Score is", user_score)
                for i in range(len(word_to_guess)):
                    if word_to_guess[i] == guess:
                        current_word[i] = guess
                print(" ".join(current_word))
                if "_" not in current_word:         # if no underscores, indicated current word is solved!
                    user_score += 1
                    print("You solved it!")
                    print("Current score:", user_score)
                    break
            else:                                   # user missed a word
                user_score -= 1

                if user_score > 0:                  # indicator for last life, when score is 0
                    print("Sorry, guess again. Score is", user_score)
                if user_score == 0:
                    print("Sorry, guess again. Your on your last life! Score is", user_score)
                print(" ".join(current_word))

                if user_score < 0:                  # game over
                    print("Game over. Your final score is 0.")
                    return
            print("Guessed letters:", " ".join(sorted(list(guessed))))      # prints all guessed letter

# Main function
if __name__ == '__main__':
    file = open("anat19.txt", "r")
    text = file.read()

    tokens = tokenize(text)
    setTokens = set(tokens)

    print("----------- TEXT INFORMATION ------------")
    print("The number of tokens in text: ", len(tokens))
    print("The number of unique tokens in text:", len(setTokens))
    print("The lexicographical diversity of the text: {:.2f}".format(len(setTokens)/len(tokens)))

    # preprocesses text
    tokens, nouns = preprocess_text(tokens)

    #prints the list of 50 most common nouns from text
    noun = {noun: tokens.count(noun) for noun in nouns}
    noun_counts = sorted(noun.items(), key=lambda x: x[1], reverse=True)
    common_words = []
    print("Top 50 most common words:")
    for noun, count in noun_counts[:50]:
        print(f"{noun}: {count}")
        common_words.append(noun)

    print("\n ----------- GUESSING GAME ------------")
    guessing_game(common_words)
    file.close()


