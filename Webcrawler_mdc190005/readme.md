# Vicky Nguyen, vtn180004
# Meinhard C, mdc190005
# CS 4395.001


Make sure you have an empty folder named data created to host the urls

There are three important files:

main.py - Does parts 1 - 3 of the homework. 

1. Build a web crawler function that starts with a URL representing a topic (a sport, your
favorite film, a celebrity, a political issue, etc.) and outputs a list of at least 15 relevant
URLs. The URLs can be pages within the original domain but should have a few outside
the original domain.
2. Write a function to loop through your URLs and scrape all text off each page. Store each
page’s text in its own file.
3. Write a function to clean up the text from each file. You might need to delete newlines
and tabs first. Extract sentences with NLTK’s sentence tokenizer. Write the sentences for
each file to a new file. That is, if you have 15 files in, you have 15 files out. 

importantterms.py - does parts 4-6 of homework

4. Write a function to extract at least 25 important terms from the pages using an
importance measure such as term frequency, or tf-idf. First, it’s a good idea to lowercase everything, remove stopwords and punctuation. Print the top 25-40 terms.
5. Manually determine the top 10 terms from step 4, based on your domain knowledge.
6. Build a searchable knowledge base of facts that a chatbot (to be developed later) can
share related to the 10 terms. The “knowledge base” can be as simple as a Python dict
which you can pickle. More points for something more sophisticated like sql.

CS4395.001-Webcrawler.pdf - Does part 7 of the homework, text document that explains knowledge base, etc.

7. In a doc: (1) describe how you created your knowledge base, include screen shots of the
knowledge base, and indicate your top 10 terms; (2) write up a sample dialog you would
like to create with a chatbot based on your knowledge base

readme.md - markdown file that contains these instructions 


The next two files are knowledge bank files; outputted once main.py and importantterms.py are ran. We included them just in case any are needed or if one wants to view them:

facts.txt - a text document containing all facts for each of the 10 most important terms.


clean_terms_dicts.pickle - a pickled dictionary that contains 10 entries, with the key being each term and the value being the facts.


The code and documents can also be found here on both our portfolios:

Vicky: https://github.com/vickynguyen3/NLP_Portfolio/tree/main/WebCrawler

Meinhard: https://github.com/meintgl/NLP-Portfolio





