# mdc190005 / Homework 1 / 1.29.23
# Meinhard Benedict Capucao
"""
This program reads a .csv file line by line. The heading is ignored. Each line represents an employee that has the five
parameters:
    'Last', 'First', 'Middle Initial', 'ID', and 'Office Phone'.
Employees fall under the Person class with fields that correspond to the .csv file:
    'last', 'first', 'mi', id, and 'phone'

The program also processes and standardizes the text. It then saves the results it into a dictionary with 'ID' as the key.
The dictionary is saved as pickle file, then is printed using the display() method in the Person class.
"""
import re
import sys

import pathlib
import pickle



"""
    def process_employee(employee_text):
    
    Processes a list of strings and splits on the comma to get fields as text variables.
    Modifies last and first name to be capital case, middle initial to be single upper case, and substitutes middle 
        initial for 'X' if the initial is missing.
    Modifies ID if necessary with correct format being 2 letters followed by 4 digits. Validates and asks for re-input 
        if needed.
    Modifies phone if necessary with correct format being integers in form "xxx-xxx-xxxx".
    Creates a person object and saves it to a dict of persons, with ID being the key. Duplicates are checked and asks 
        for re-input if one is found.
    Args:
         employees_text:  a list of strings, with each string being a line of employee data from data.csv.
     Returns:
         persons: a dict of persons with id as the key.
     Example:
         >>> (input): CAPUCAO,MEIN,D,MD2720,444-333-4545
                      ISLAM,TAUS,K,TS4346, 454-342.2222      
        >>>  (output): 
                      persons: ['MD2720:CAPUCAO',TS4346:ISLAM]    
     """

def process_employee(employee_text):
    persons = {}                         # Creates a dictionary named persons
    for line in employee_text[1:]:       # Goes line by line, ignores the header by ignoring the first element.
        last, first, mi, id, phone = line.split(',')

        # Check and format first and last names. Make sure first and last is only alphabets, and capitalized.
        while not last.isalpha():
            print(f"Last name invalid: {last}")
            last = input("Please enter a valid last name:").capitalize()     # Makes sure that first letter is capital
        last = last.capitalize()

        while not first.isalpha():
            print(f"First name invalid: {first}")
            first = input("Please enter a valid first name:").capitalize()    # Makes sure that first letter is capital
        first = first.capitalize()

        # Ensure middle initial is single upper case. IF nothing is inputted for middle initial, then it is replaced
        # by 'x'.

        if not mi:                  # If middle initial is empty
            mi = "X"
        elif mi:
            mi = mi.capitalize()    # Makes sure initial name is capitalized
            while len(mi) != 1 or not mi.isalpha():         # Makes sure middle initial is only one alphabetical char
                print(f"Middle initial initial: {middle_initial}")
                middle_initial = input("Please enter a valid middle initial: "
                                       "(single case upper letter, if none enter nothing).").capitalize()

        # Checks and formats id to 2 letters followed by 4 digits with regex.
        id = id.upper()
        while not re.match(r'^[A-Z]{2}\d{4}$', id):
            print(f"Invalid ID format: {id}")
            id = input("Please enter a valid ID: (2 letters followed by 4 digits): ").upper()

        # Check and format phone number to form "xxx-xxx-xxxx" with x being digits.
        while not re.match(r'^\d{3}-\d{3}-\d{4}$', phone):
            print(f"Invalid phone number format: {phone}")
            phone = input("Please enter a valid phone number: (xxx-xxx-xxxx): ")

        # Check for duplicates and add to dictionary
        person = Person(last, first, mi, id, phone)
        if id in persons:
            print(f"Duplicate ID detected: {id}. Please enter a valid ID: (2 letters followed by 4 digits).")
        else:
            persons[id] = person
    return persons


"""
    class Person:
    parameters:
         self: self call to function
         last: last name, capital first letter, alphabet only.
         first: first name, initial letter, , alphabet only.
         mi: middle initial, one letter, capital letter, alphabet only.
         id: 2 letters followed by 4 digits, numbers only.
         phone: (xxx-xxx-xxxx), numbers only. 
     functions:
         display: a dict of persons with id as the key.
     """

class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    # Function displays employee data
    def display(self):
        print(f"Employee id: {self.id}")
        print(f"\t{self.first} {self.mi} {self.last}")
        print(f"\t{self.phone}")

# Main function
if __name__ == '__main__':
    if len(sys.argv) < 2:       #Checks if user has system arg
        print('Please enter a filename as a system arg')
        quit()

    # Gets the second part of the sys arg, which is the file name. File name is opened
    # Text_in is a list that reads lines of the .csv, and has employee data.
    rel_path = sys.argv[1]
    with open(pathlib.Path.cwd().joinpath(rel_path), 'r') as f:
            text_in = f.read().splitlines()

    employees = process_employee(text_in[0:])

    #Pickle the employees
    pickle.dump(employees, open('employees.pickle', 'wb'))

    #read the pickle back in
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    #Output employees
    for employee_id in employees_in.keys():
        employees_in[employee_id].display()

