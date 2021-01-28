"""
Φόρτωση των load_problem και solve_problem των αρχείων
load_problem.py και solve_problem.py αντίστοιχα.

Φόρτωση του mass_solve που βρίσκεται στο solve_problem.py
"""
from load_problem import load_problem
from solve_problem import solve_problem
from solve_problem import mass_solve


def menu():
    """
    Function η οποία εκτυπώνει τα επιθυμητά μηνύματα στην οθόνη, αποθηκεύει
    στο choice την επιλογή την οποία εισάγουμε και καλεί το αντίστοιχο function.
    Σε κάθε if αυτό που θα εισαχθεί από τον χρήστη αποθηκεύεται στην μεταβλητή
    buffer και το buffer χρησιμοποιείται ως όρισμα της αντίστοιχης function.
    Πατώντας την επιλογή νούμερο 4 γίνεται τερματισμός.
    """

    print("Welcome, \n 1. Load Problem \n 2. Solve Problem \n 3. Mass Solve \n 4. Exit")
    choice = int(input("Enter --> "))  # Μετατροπή του εισαχθέντος στοιχείου σε αριθμό

    if choice == 1:
        buffer = input('Enter the file name: ')
        load_problem(buffer)
        menu()  # Κλήση ξανά της menu() για να εμφανιστούν ξανά οι διαθέσιμες επιλογές

    if choice == 2:
        buffer = input('Enter the file name: ')
        solve_problem(buffer)
        menu()  # Κλήση ξανά της menu() για να εμφανιστούν ξανά οι διαθέσιμες επιλογές

    if choice == 3:
        mass_solve()
        menu()  # Κλήση ξανά της menu() για να εμφανιστούν ξανά οι διαθέσιμες επιλογές

    if choice == 4:
        return()


menu()
